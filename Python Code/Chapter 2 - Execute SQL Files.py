# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 07:11:30 2024

@author: Jeff Miller
"""

# # =============================================================================
# # Chapter 2 - Execute SQL Files.py
# # =============================================================================

import pyodbc
import os

# Define the connection details
server = 'server name'  # Your SQL Server name
database = 'Automate_Everything_With_Python'  # Database name where SQL files will be executed
sql_username = 'username'  # Replace with your SQL Server username
password = 'password'  # Replace with your SQL Server password


# Get the username
pc_username = os.getlogin()

# Path to the directory containing SQL files
sql_directory = r"C:\\Users\\" + pc_username + "\\Desktop\\Automate_Everything_With_Python\\SQL Code"

# List of SQL file names to execute
sql_files = [f for f in os.listdir(sql_directory) if (f.startswith("dbo") or f.startswith("CDC Covid19 Staff"))and f.endswith(".sql")]

# Define the connection string
connection_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={sql_username};PWD={password}'

# Function to execute SQL file
def execute_sql_file(file_path):
    try:
        # Establish a connection and execute the SQL script
        with pyodbc.connect(connection_string) as conn:
            with open(file_path, 'r') as file:
                sql_script = file.read()
                with conn.cursor() as cursor:
                    cursor.execute(sql_script)
                    print(f"SQL script {os.path.basename(file_path)} executed successfully.")
    except pyodbc.Error as e:
        print(f"Error executing {os.path.basename(file_path)}: {e}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred with {os.path.basename(file_path)}: {e}")

# Execute each SQL file
for sql_file in sql_files:
    sql_file_path = os.path.join(sql_directory, sql_file)
    execute_sql_file(sql_file_path)