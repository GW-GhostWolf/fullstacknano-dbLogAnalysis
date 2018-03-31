#!/usr/bin/env python3
# Run analysis on the website logs stored in the news database
# Database is expected to be running on the local server

import psycopg2


def connect():
    """
    Connect to the news PostgreSQL database.
    Returns a database connection.
    """
    return psycopg2.connect("dbname=news")


def getPopularArticles(dbcon):
    """
    Returns the top 3 article titles and the number of lifetime views.
    Takes an open database connection.
    """
    c = dbcon.cursor()
    c.execute("""
        select a.title, count(l.id)
        from articles a
        join log l on position(a.slug in l.path) > 0
        where l.status like '200%'
        group by a.title
        order by count desc
        limit 3;
    """)
    return c.fetchall()


def getPopularAuthors(dbcon):
    """
    Returns all authors with number of lifetime views of all articles.
    Takes an open database connection.
    """
    c = dbcon.cursor()
    c.execute("""
        select w.name, count(l.id)
        from articles a
        join log l on position(a.slug in l.path) > 0
        join authors w on w.id = a.author
        where l.status like '200%'
        group by w.name
        order by count desc;
    """)
    return c.fetchall()


def getHighErrorDays(dbcon):
    """
    Returns the dates with more than 1% error rate.
    Includes date and error rate.
    Takes an open database connection.
    """
    c = dbcon.cursor()
    c.execute("""
        select total.date, 100.0 * error.count / total.count as errorRate
        from
            (select date_trunc('day', time) as date, count(*)
                from log group by date) total,
            (select date_trunc('day', time) as date, count(*)
                from log where status not like '200%' group by date) error
        where total.date = error.date
            and 100.0 * error.count / total.count > 1.0
        order by total.date;
    """)
    return c.fetchall()


def printResults(results, formatString):
    """
    Prints out the results using the format string
    Input results: data set to print. assumes it has 2 fields
    Input formatString: format string to use for printing
    """
    for row in results:
        print(formatString.format(row[0], row[1]))
    print("")


# Connect to the database
db = connect()
# Run Popular Articles analysis
print("")
results = getPopularArticles(db)
formatString = "{:<40}{:>10}"
print("Most Popular Articles (lifetime)")
print(formatString.format("Article", "View Count"))
print("{:=^50}".format(""))
printResults(results, formatString)
# Run Popular Author analysis
results = getPopularAuthors(db)
formatString = "{:<30}{:>10}"
print("Most Popular Authors (lifetime)")
print(formatString.format("Author", "View Count"))
print("{:=^40}".format(""))
printResults(results, formatString)
# Run High Error analysis
results = getHighErrorDays(db)
formatString = "{:%Y-%m-%d}{:9.2f}%"
print("High Error Days")
print("{:<10}{:>10}".format("Date", "Error %"))
print("{:=^20}".format(""))
printResults(results, formatString)
# Close the connection to the database
db.close()
