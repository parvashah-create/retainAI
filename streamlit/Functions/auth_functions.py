import bcrypt
import sqlite3
from datetime import datetime
from Functions.db_functions import get_db, check_username_taken
import streamlit as st
from decouple import config

def verify_password(username, password):
    # Connect to the SQLite database
    conn, cur = get_db("auth_data.db")

    # Retrieve the user's hashed password from the database
    cur.execute("SELECT password FROM users WHERE username='{0}'".format(username))
    hashed_password = cur.fetchone()[0]
    
    # Close the database connection
    conn.close()
    # Verify the user's input password with the hashed password
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False
    


def login_user(username,password):
 # if block checks if username or password is incorrect and raises an error    
    if (not check_username_taken(username)) or ( not verify_password(username, password)):#<------ Function verify_user needed
        st.error("Username/Password Invalid!")
        return False
    st.success("User logged in successfully!")
    return True

# register user
def register_user(name,username,password,plan):
    salt = bcrypt.gensalt()
    hash_pass = bcrypt.hashpw(password.encode('utf-8'), salt)
    # connect to DB
    conn, cur = get_db("auth_data.db")
    # get joining time
    join_date = datetime.now()
    if check_username_taken(username):#<------ Function verify_user needed
        return False
    # Execute the INSERT query to add the row to the table
    query = "INSERT INTO users (name,username, password, plan, role, join_date, calls_per_hour) VALUES (?, ?, ?, ?, ?,?,?)"
    cur.execute(query, (name,username, hash_pass,plan,"user",join_date,0))
    # Commit the changes to the database
    conn.commit()
    # Close the database connection
    conn.close()
    return True
