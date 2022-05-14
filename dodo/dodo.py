import mysql.connector

cnx = mysql.connector.connect(user='root', password='example',
                              host='db',
                              database='nenene')
cnx.close()
