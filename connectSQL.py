import mysql.connector
from datetime import datetime
import os
import re
from cryptoDaily import crytoDailyInfo


cryptoDaily = crytoDailyInfo()

conn = mysql.connector.connect(host='127.0.0.1',
                                        user='root',
                                        password='password',
                                        db='dentalce',
                                        charset='utf8')


cursor = conn.cursor()

sqlInsert = """ INSERT INTO links (name, link)
                            VALUES (%(name_IN)s, %(link_IN)s); """

item_Dict = {}
for item in cryptoDaily.items():
    if ''.join(item).strip():
        item_Dict['name_IN'] = item[0]
        item_Dict['link_in'] = item[1]
        cursor.execute(sqlInsert, item_Dict)

    conn.commit()
    cursor.close()
    conn.close()