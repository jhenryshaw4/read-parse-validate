import mysql.connector

#connection string
cnx = mysql.connector.connect(user='root',
    password='intermuraltennis',
    host='127.0.0.1',
    database = 'sys',
    auth_plugin='mysql_native_password')

#query
cursor = cnx.cursor()
query = ('SHOW DATABASES')
cursor.execute(query)

#loop throgh data
for row in cursor.fetchall():
    print(row)

#clean up
cursor.close()
cnx.close()