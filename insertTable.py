import mysql.connector
from mysql.connector import Error
from datetime import datetime

def insertVariblesIntoTable(bookingId, telephone, referenceCode, timeStamp):
    try:
        connection = mysql.connector.connect(host='localhost',
                                         database='reservation',
                                         user='root',
                                         password="")
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO booking (bookingId, telephone, referenceCode, timeStamp) 
                                VALUES (%s, %s, %s, %s) """

        recordTuple = (bookingId, telephone, referenceCode, timeStamp)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            

current_Date = datetime.now()
# convert date in the format you want
formatted_date = current_Date.strftime('%Y-%m-%d %H:%M:%S')

insertVariblesIntoTable(1, '0777572498', 4561, current_Date)
insertVariblesIntoTable(2, '0657894520', 7365, current_Date)
