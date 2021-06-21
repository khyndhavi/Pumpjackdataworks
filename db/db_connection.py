import os
os.system('pip install mysql-connector')
import mysql.connector


class DBConnector(object):
    def __init__(self):
        self.connection_config_dict = {
           'user': 'root',
           'password': 'admin',
           'host': '127.0.0.1',
           'database': 'employee_schema',
           'raise_on_warnings': True,
           'autocommit': True,
           'pool_size': 5
        }
        self.dbconn = None

    # creates new connection
    def create_connection(self):
        connection = mysql.connector.connect(**self.connection_config_dict)
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Successfully connected to database: ", record)
        return connection

    # For explicitly opening database connection
    def __enter__(self):
        self.dbconn = self.create_connection()
        return self.dbconn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.dbconn.close()


class DBConnection(object):
    connection = None

    @classmethod
    def get_connection(cls, new=False):
        """Creates return new Singleton database connection"""
        if new or not cls.connection:
            cls.connection = DBConnector().create_connection()
        return cls.connection

    @classmethod
    def execute_insert_query(cls, query, params=()):
        """execute query on singleton db connection"""
        try:
            connection = cls.get_connection()
            cursor = connection.cursor()
            result = cursor.execute(query, params)
            connection.commit()
            return result
        except mysql.connector.Error as error:
            connection.rollback()
            print("Failed to execute insert query {}".format(error))

    @classmethod
    def execute_select_query(cls, query, params=()):
        """execute query on singleton db connection"""
        try:
            connection = cls.get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, params)
            result = cursor.fetchall()
            row_count = cursor.rowcount
            return result, row_count
        except mysql.connector.Error as error:
            connection.rollback()
            print("Failed to execute select query {}".format(error))
