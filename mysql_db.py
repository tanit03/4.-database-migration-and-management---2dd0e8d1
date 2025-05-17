import pymysql

def get_mysql_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='yourpass',
        database='legacy_db'
    )
