# Diseases Map - IDQBRN

## About
Code related to an interactive map of diseases in Brazil, developed for IDQBRN

## Install - Web
Check dependecies:
> python -V
> python -m django --version

This project uses Python 3.9.2 and Django 4.0.4.
Open terminal in \web\diseasesmap and type the following commands: 
> python manage.py runserver

## Install - Database
Check dependencies:
> python -V

Create a database 'diseasesmapdb' and create a new user for this database:
> mysql -h localhost -u root -p
> mysql > CREATE USER 'diseasesmapadmin'@'localhost' IDENTIFIED BY 'diseasesmap';
> mysql > GRANT ALL PRIVILEGES ON diseasesmapdb . * TO 'diseasesmapadmin'@'localhost';

To create and update tables, open terminal in \web\diseasesmap and type the following commands:
> pip install
> python manage.py makemigrations server
> python manage.py migrate server 