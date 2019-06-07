
# Stuff we require to build our first REST API
# Python *
# Flask *
# Flask-SQLAlchemy
# Flask-Restful *
# SQlite3
# Jsonify *

# importing the module
import MySQLdb

# opening a database connection
db = MySQLdb.connect("localhost", "testprog", "stud", "PYDB")

# define a cursor object
cursor = conn.cursor

# drop table if exists
Cursor.execute("IF STUDENT TABLE EXISTS DROP IT")

# query
sql = "CREATE TABLE STUDENT (NAME CHAR(30) NOT NULL, CLASS CHAR(5), AGE INT, GENDER CHAR(8), MARKS INT"

# execute query
cursor.execute(sql)

# close object
cursor.close()

# close connection
conn.close()





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
