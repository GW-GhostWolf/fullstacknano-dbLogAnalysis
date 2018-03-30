#!/usr/bin/env python3

import psycopg2
from sys import exit

try:
    db = psycopg2.connect("dbname=news")
except:
    print("Unable to connect to the database")
    exit(0)

try:
    c = db.cursor()
    c.execute("select * from authors;")
    data = c.fetchall()
except:
    print("Unable to query the database")
    exit(0)

print(c.rowcount)
for row in data:
    print(row)

db.close()


# select a.title, a.author, count(l.id)
# from articles a 
# join log l on position(a.slug in l.path) > 0
# where l.status like '200%'
# group by a.title 
# order by count desc 
# limit 3;


# select w.name, count(l.id)
# from articles a 
# join log l on position(a.slug in l.path) > 0
# join authors w on w.id = a.author
# where l.status like '200%'
# group by w.name
# order by count desc;


# select total.date, total.count, error.count, 100.0 * error.count / total.count as errorRate
# from 
# (select date_trunc('day', time) as date, count(*) from log group by date) total,
# (select date_trunc('day', time) as date, count(*) from log where status not like '200%' group by date) error
# where total.date = error.date and 100.0 * error.count / total.count > 1.0
# order by total.date;

