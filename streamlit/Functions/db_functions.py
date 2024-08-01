import sqlite3
import pandas as pd
import os
from datetime import  datetime 
import streamlit as st



def get_db(db):
    # eastablish connection with db
    # parent directory
    current_path = os.getcwd()
    parent = os.path.dirname(current_path)
    db_path = current_path + "/streamlit/database/{}".format(db)
    # db_path = current_path + "/database/{}".format(db)

    conn = sqlite3.connect(db_path,check_same_thread=False)
    cursor = conn.cursor()
    return conn, cursor


# check user in DB
def check_username_taken(username):
    # conect to db
    conn, cur = get_db("auth_data.db")
    # checks if username exists in table
    res = cur.execute(f"SELECT username FROM users WHERE users.username = '{username}'")
    check = res.fetchone()
    # Close the database connection
    conn.close()

    if check == None:
        return False
    else:
        return True
    

# Get password for a given username
def get_password(username):
    # connect to db
    conn, cur = get_db("auth_data.db")
    # get password of given username
    res = cur.execute(f"SELECT password FROM users WHERE users.username = '{username}'")
    password = res.fetchone()
    # Close the database connection
    conn.close()
    if password == None:
        return False
    return password[0]

# log data in db
def log_data(username,timestamp,message):
    # connect to db
    conn, cur = get_db("auth_data.db")
     # get joining time
    timestamp = datetime.now()
    # Execute the INSERT query to add the row to the table
    query = "INSERT INTO logs (username, timestamp, message) VALUES (?, ?, ?)"
    cur.execute(query, (username, timestamp, message))
    # Commit the changes to the database
    conn.commit()
    # Close the database connection
    conn.close()
    return {"status":f"{username} logged in Successfully!"}

# get user data
def user_data(username):
    # conect to db
    conn, cur = get_db("auth_data.db")
    # get user data
    df = pd.read_sql_query(f"SELECT * FROM logs WHERE logs.username = '{username}'", conn)
    # Close the database connection
    conn.close()
    return df