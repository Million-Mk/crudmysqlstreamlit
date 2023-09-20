import pymysql

# สร้าง fnสำหรับการเชื่อมต่อฐานข้อมูล


def connectdb():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='pythondb',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor)
    return connection

# ทดสอบการเรียกใช้งาน fn


print("Connect Database : ", connectdb())
