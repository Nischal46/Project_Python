import mysql.connector
from mysql.connector import Error

def get_mysql_data():
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            database = 'practicingQuery',
            user = 'root',
            password = ''
        )

        if(connection.is_connected()):
            cursor = connection.cursor()

            user_query = "SELECT * FROM BLOGUSER"


            cursor.execute(user_query)
            user_record = cursor.fetchall()

            print('User of BLOG USER Table')
            for row in user_record:
                print(row)

    except Error as e:
        print('Error occured while connecting to database: ', e)

    finally: 
        if(connection.is_connected()):
            cursor.close()
            connection.close()
            print('Mysql connection is closed')

if __name__ == "__main__":
    get_mysql_data()

                