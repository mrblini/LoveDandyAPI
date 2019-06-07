
# Stuff we require to build our first REST API
# Python *
# Flask *
# Flask-SQLAlchemy
# Flask-Restful *
# SQlite3
# Jsonify *

# ------------------------------------------------------------------ CONNECTION
POST /test/demo_form.php HTTP/1.1
Host: w3schools.com
name1=value1&name2=value2
# ------------------------------------------------------------------
import psycopg2

conn = psycopg2.connect(database="testdb", user="postgres",
                        password="pass123", host="127.0.0.1", port="5432")

print "Opened database successfully"

cur = conn.cursor()

cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
print "Total number of rows updated :", cur.rowcount

cur.execute("SELECT id, name, address, salary  from COMPANY")
rows = cur.fetchall()
for row in rows:
   print "ID = ", row[0]
   print "NAME = ", row[1]
   print "ADDRESS = ", row[2]
   print "SALARY = ", row[3], "\n"

print "Operation done successfully"
conn.close()


# ------------------------------------------------------------------ 
# This API opens a connection to the PostgreSQL database. If database is opened successfully, it returns a connection object.
import psycopg2
psycopg2.connect(database="testdb", user="postgres",
                 password="cohondob", host="127.0.0.1", port="5432")

# This routine creates a cursor which will be used throughout of your database programming with Python.
connection.cursor()

# This routine executes an SQL statement. The SQL statement may be parameterized (i.e., placeholders instead of SQL literals). The psycopg2 module supports placeholder using %s sign
For example: cursor.execute("insert into people values (%s, %s)", (who, age))
cursor.execute(sql[, optional parameters])

# This routine executes an SQL command against all parameter sequences or mappings found in the sequence sql.
cursor.executemany(sql, seq_of_parameters)

# This routine executes a stored database procedure with the given name. The sequence of parameters must contain one entry for each argument that the procedure expects.
cursor.callproc(procname[, parameters])

# This read-only attribute which returns the total number of database rows that have been modified, inserted, or deleted by the last last execute*().
cursor.rowcount

# This method commits the current transaction. If you do not call this method, anything you did since the last call to commit() is not visible from other database connections.
connection.commit()

# This method rolls back any changes to the database since the last call to commit().
connection.rollback()

connection.close()
# # importing the module
# import MySQLdb


# ---------------------------- Connecting to Database
#!/usr/bin/python
conn = psycopg2.connect(database="testdb", user="postgres",
                        password="pass123", host="127.0.0.1", port="5432")

print "Opened database successfully"


# ---------------------------- create a table
#!/usr/bin/python
conn = psycopg2.connect(database="testdb", user="postgres",
                        password="pass123", host="127.0.0.1", port="5432")
print "Opened database successfully"

cur = conn.cursor()
cur.execute('''CREATE TABLE COMPANY
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      ADDRESS        CHAR(50),
      SALARY         REAL);''')
print "Table created successfully"

conn.commit()
conn.close()


# ---------------------------- insert operation
conn = psycopg2.connect(database="testdb", user="postgres",
                        password="pass123", host="127.0.0.1", port="5432")
print "Opened database successfully"

cur = conn.cursor()

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

conn.commit()
print "Records created successfully"
conn.close()

















# # opening a database connection
# db = MySQLdb.connect("localhost", "testprog", "stud", "PYDB")

# # define a cursor object
# cursor = conn.cursor

# # drop table if exists
# Cursor.execute("IF STUDENT TABLE EXISTS DROP IT")

# # query
# sql = "CREATE TABLE STUDENT (NAME CHAR(30) NOT NULL, CLASS CHAR(5), AGE INT, GENDER CHAR(8), MARKS INT"

# # execute query
# cursor.execute(sql)

# # close object
# cursor.close()

# # close connection
# conn.close()





# ------------------------------------------------------- concept:
# from flask import Flask, request
# from flask_restful import Resource, Api
# from sqlalchemy import create_engine
# from json import dumps
# from flask.ext.jsonpify import jsonify

# db_connect = create_engine('sqlite:///chinook.db')
# app = Flask(__name__)
# api = Api(app)

# class Employees(Resource):
#     def get(self):
#         conn = db_connect.connect() # connect to database
#         query = conn.execute("select * from employees") # This line performs query and returns json result
#         return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

# class Tracks(Resource):
#     def get(self):
#         conn = db_connect.connect()
#         query = conn.execute("select trackid, name, composer, unitprice from tracks;")
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)

# class Employees_Name(Resource):
#     def get(self, employee_id):
#         conn = db_connect.connect()
#         query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
#         result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
#         return jsonify(result)

# -------------------------------------------------------


# GET Request - Retrieve data from PurpleAir

# import MySQLdb
# conn = MySQLdb.connect(host='localhost', user='root', passwd='')
# cursor = conn.cursor()

    # Database access information

# POST REQUEST - Update LoveDandy's database in Postcress

    # Database access information

# Pass parameters

    # For loop constantly updating database 

    # Response
