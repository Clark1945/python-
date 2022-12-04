# 模組PySQLSql SQLAlchemy連線資料庫時所指定的MySQL資料庫驅動程式。
# 模組SQLAlchemy用於連線資料庫
import sqlalchemy as sa
dbc= 'mysql+pymysql://root:hello@localhost:3306'
con = sa.create_engine(dbc)
# 資料庫類型+驅動程式://使用者名稱:密碼@主機名稱[:MySQL的port號]/資料庫名稱
con.execute("CREATE DATABASE school")# 創建
con.execute("use school") # 使用db
sql = """CREATE TABLE stu(
    stu_id INTEGER PRIMARY KEY,
    name VARCHAR(20) not null,
    pid VARCHAR(10) not null,
    phone VARCHAR(20) not null
)""" #加入資料表
con.execute(sql)
sql = "INSERT INTO stu VALUES(1003,'Clarie','10746025','0659337')" #加入值
con.execute(sql)
result = con.execute("SELECT * FROM stu") #顯示全部
rows = result.fetchall()
print(rows)
con.execute("DROP TABLE stu")
con.execute("DROP DATABASE school")

# row=result.fetchall() #取出所有資料
