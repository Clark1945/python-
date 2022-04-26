import mysql.connector

connection= mysql.connector.connect(
    host='localhost',
    port='3306',
    user='root',
    password='rup wu0 d9 g3SQL',
    database='sql_tutorial'
    )#host 為 位置 port 為通道 user password 為帳密

cursor=connection.cursor()

# cursor.execute("use `sql_tutorial`;")
# # cursor.close()
# # connection.close()
# cursor.execute("show databases;")
# records=cursor.fetchall()
# for x in records:
#     print(x)
    
# cursor.execute("use `company_data`;")
# cursor.execute("create table `extra_list`(danger varchar(20));")



#Update資料一定要使用 connection.commit()
cursor.close()
connection.close()