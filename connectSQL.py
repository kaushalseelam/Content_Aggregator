import mysql.connector
from datetime import datetime
import os
import re
from cryptoDaily import crytoDailyInfo


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