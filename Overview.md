# SQLite Python

This section shows you step by step how to work with the SQLite database using Python programming language.

Python provides two popular interfaces for working with the SQLite database library: PySQLite and APSW. Each interface targets a set of different needs.
## PySQLite

The PySQLite provides a standardized Python DBI API 2.0 compliant interface to the SQLite database. If your application needs to support not only the SQLite database but also other databases such as MySQL, PostgreSQL, and Oracle, the PySQLite is a good choice.

PySQLite is a part of the Python Standard library since Python version 2.5
## APSW

If your application needs to support only the SQLite database, you should use the APSW module, which is known as Another Python SQLite Wrapper.

The APSW provides the thinnest layer over the SQLite database library. The APSW is designed to mimic the native SQLite C, therefore, whatever you can do in SQLite C API, you can do it also from Python.

Besides covering the SQLite library, the APSW provides many low-level features including the ability to create user-defined aggregate, function, and collations from Python. It even allows you to write a virtual table implementation using Python.
SQLite Python

We will use the PySQLite wrapper to demonstrate how to work with SQLite database library using Python.

- Creating an SQLite database from a Python program: shows you how to create a new SQLite database from a Python program using the sqlite3 module.
- Create tables in SQLite database using Python: shows you step by step how to create tables in an SQLite database from a Python program.
- Inserting data into the SQLite database in Python: walks you through the steps of inserting data into a table in SQLite database using Python.
- Updating data in the SQLite database using Python: learns how to update existing data in the SQLite database using Python.
- Selecting data: this tutorial shows you how to query data in an SQLite database from a Python program.
- Deleting data from a Python program: guides you how to delete one or more rows in a table from a table using Python sqlite3 module API.