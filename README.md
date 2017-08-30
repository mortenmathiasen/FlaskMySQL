# FlaskMySQL

This repository is an example that shows how to create a web application using Flask with MySQL as backend

## Installation

- Setup [MySQL](https://www.mysql.com/) server 
- Pull or copy [repository](https://github.com/mortenmathiasen/FlaskMySQL.git)
- Install [Python](https://www.python.org/) and [PIP](https://pypi.python.org/pypi/pip) package manager
- Install [Flask](https://pypi.python.org/pypi/Flask/0.12.2) and (flask-mysqldb)[http://flask-mysqldb.readthedocs.io/en/latest/] with [PIP](https://pypi.python.org/pypi/pip) package manager

## Prepare MySQL database

In order to connect Flask MySQL, we would need to install Flask-MySQL which is an extension, which allows us to connect to MySQL database.

First boot up the MySQL server. In order to install data into the database get to your terminal and type

```
mysql -u  -p
```

and then enter your password when prompted. Now, create a new database called EmpData and a table called User with 3 columns – UserId, Username, Password.

```
mysql> CREATE DATABASE EmpData;
 
mysql> CREATE TABLE User(
 userId INT NOT NULL AUTO_INCREMENT,
 userName VARCHAR(100) NOT NULL,
 password VARCHAR(40) NOT NULL,
 PRIMARY KEY(userId)
 );
 ```

Now, insert some data into the table User

```
mysql> insert into User values('','Admin','admin');
```

So, we are all set with the MySQL database content.

## Running the application

- Boot up the MySQL server
- Boot up the Python Flask application and go to [http://localhost:5000](http://localhost:5000)
