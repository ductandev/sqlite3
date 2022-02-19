# **Datatypes In SQLite**

## **1. Datatypes In SQLite**

Most SQL database engines (every SQL database engine other than SQLite, as far as we know) uses static, rigid typing. With static typing, the datatype of a value is determined by its container - the particular column in which the value is stored.

SQLite uses a more general dynamic type system. In SQLite, the datatype of a value is associated with the value itself, not with its container. The dynamic type system of SQLite is backwards compatible with the more common static type systems of other database engines in the sense that SQL statements that work on statically typed databases work the same way in SQLite. However, the dynamic typing in SQLite allows it to do things which are not possible in traditional rigidly typed databases. Flexible typing is a feature of SQLite, not a bug.

## **2. Storage Classes and Datatypes**

Each value stored in an SQLite database (or manipulated by the database engine) has one of the following storage classes:
| Type | Discription |
| ---- | -------------------------- |
|NULL. | The value is a NULL value.|
| INTEGER. | The value is a signed integer, stored in 0, 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.|
|REAL. | The value is a floating point value, stored as an 8-byte IEEE floating point number.|
|TEXT.  | The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).|
| BLOB.| The value is a blob of data, stored exactly as it was input.|

A storage class is more general than a datatype. The INTEGER storage class, for example, includes 7 different integer datatypes of different lengths. This makes a difference on disk. But as soon as INTEGER values are read off of disk and into memory for processing, they are converted to the most general datatype (8-byte signed integer). And so for the most part, "storage class" is indistinguishable from "datatype" and the two terms can be used interchangeably.

Any column in an SQLite version 3 database, except an INTEGER PRIMARY KEY column, may be used to store a value of any storage class.

All values in SQL statements, whether they are literals embedded in SQL statement text or parameters bound to precompiled SQL statements have an implicit storage class. Under circumstances described below, the database engine may convert values between numeric storage classes (INTEGER and REAL) and TEXT during query execution. 

### **2.1. Boolean Datatype**

SQLite does not have a separate Boolean storage class. Instead, Boolean values are stored as integers 0 (false) and 1 (true).

SQLite recognizes the keywords "TRUE" and "FALSE", as of version 3.23.0 (2018-04-02) but those keywords are really just alternative spellings for the integer literals 1 and 0 respectively.
2.2. Date and Time Datatype

SQLite does not have a storage class set aside for storing dates and/or times. Instead, the built-in Date And Time Functions of SQLite are capable of storing dates and times as TEXT, REAL, or INTEGER values:

- TEXT as ISO8601 strings ("YYYY-MM-DD HH:MM:SS.SSS").
- REAL as Julian day numbers, the number of days since noon in Greenwich on November 24, 4714 B.C. according to the proleptic Gregorian calendar.
- INTEGER as Unix Time, the number of seconds since 1970-01-01 00:00:00 UTC. 

Applications can choose to store dates and times in any of these formats and freely convert between formats using the built-in date and time functions.

## Tài liệu tham khảo:

1. https://www.sqlite.org/datatype3.html