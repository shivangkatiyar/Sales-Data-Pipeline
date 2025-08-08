import mysql.connector
from resources.dev import config

def get_mysql_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=config.database_password,
        database=config.database_name
    )
    return connection

