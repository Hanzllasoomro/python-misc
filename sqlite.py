import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Successfully connected to database")
        return conn
    except Error as e:
        print(e)

    return conn

def close_connection(conn):
    if(conn):
        conn.close()
        print("Successfully closed")

def create_table_in_db(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)

def create_table():
    database = sqlite3.connect("test.db")
    create_table_sql = """ CREATE TABLE IF NOT EXISTS STUDENTS(
                           id integer PRIMARY KEY,
                           name text NOT NULL,
                           age integer NOT NULL,
                           gpa integer NOT NULL,
                           admission_date text NOT NULL);"""

    conn = create_connection("test.db")
    if conn is not None:
        create_table_in_db(conn, create_table_sql)
    else:
        print("Error! cannot create the database connection.")
    close_connection(conn)

def add_student(conn, student):
    sql = """ INSERT INTO STUDENTS(name, age, gpa, admission_date) VALUES  (?,?,?,?);"""

    cursor = conn.cursor()
    cursor.execute(sql, student)

    return cursor.lastrowid

def main():
    database = sqlite3.connect("test.db")

    conn = create_connection("test.db")
    with conn:

        student = ("Hanzlla Soomro", 21, 3.74, '2022-11-25')
        student_id = add_student(conn, student)

    print("Student id: ",student_id)
    close_connection(conn)

def read_db():
    sqlite3.connect("test.db")
    conn = create_connection("test.db")

    try:
        cursor = conn.cursor()
        table = "STUDENTS"
        sql_string = "SELECT * FROM " + table
        sqlite_select_query = sql_string

        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()

        cursor.close()
    except Error as e:
        print(e)
    finally:
        close_connection(conn)
    print(records)


read_db()