import mysql.connector
from datetime import datetime
import os
import re

from numpy import record
from cryptoDaily import crytoDailyInfo

def import_data():
    cryptoDaily = crytoDailyInfo()

    for item in cryptoDaily.items():
        print(item[0])
        print(item[1])


    conn = mysql.connector.connect(host='127.0.0.1',
                                            user='root',
                                            password='password',
                                            db='content_agregator',
                                            charset='utf8')


    cursor = conn.cursor()

    for item in cryptoDaily.items():
        sql = "INSERT INTO links (name, link) VALUES (%s, %s)"
        #val = ("John", "Highway 21")
        cursor.execute(sql, item)

        #cursor.execute(f"INSERT INTO links (name, link) VALUES (({item[0]}, {item[1]})")

        conn.commit()
    cursor.close()
    conn.close()

def read_data(): 
    conn = mysql.connector.connect(host='127.0.0.1',
                                            user='root',
                                            password='password',
                                            db='content_agregator',
                                            charset='utf8')

    cursor = conn.cursor()
    sql_select_Query = "select * from links"
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)
    for record in records: 
        print("ID: ", record[0])
        print("link: ", record[1])
        print("\n")
    return records