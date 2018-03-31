# fullstacknano-dbLogAnalysis
Database Analysis project for Udacity Full Stack Nanodegree

## Scenario
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.

The program you write in this project will run from the command line. It won't take any input from the user. Instead, it will connect to that database, use SQL queries to analyze the log data, and print out the answers to some questions.

#### Required Software
* Install [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
* Install [Vagrant](https://www.vagrantup.com/downloads.html)
* Download or Clone this repository and open a command prompt to the new folder with the project files

## Usage
TLDR - Run the Vagrant VM, log in, and use python to run the dbLogAnalysis.py. 

Start the VM - this may take a few minutes

    vagrant up

Login to the VM

    vagrant ssh

Install the database with data

    unzip -d / /vagrant/newsdata.zip
    psql -d news -f /vagrant/newsdata.sql

Run the program using python. The program assumes the [PostgreSQL](https://www.postgresql.org/) database is running on the localhost.

    python3 /vagrant/dbLogAnalysis.py


Optionally, view the output file from the [GitHub repository](https://github.com/GW-GhostWolf/fullstacknano-dbLogAnalysis/blob/master/dbLogAnalysis.txt).
