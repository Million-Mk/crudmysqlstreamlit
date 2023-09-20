import pymysql

# สร้าง fnสำหรับการเชื่อมต่อฐานข้อมูล


def connectdb():
    # # local
    # connection = pymysql.connect(
    #     host='localhost',
    #     user='root',
    #     password='',
    #     db='pythondb',
    #     port=3306,
    #     cursorclass=pymysql.cursors.DictCursor)
    # return connection

    connection = pymysql.connect(
        host='baos8wlctwnopyxpcphs-mysql.services.clever-cloud.com',
        user='uxknmercewdinymf',
        password='CbrcoKfho8zL1tbGQL4u',
        db='baos8wlctwnopyxpcphs',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor)
    return connection

# ทดสอบการเรียกใช้งาน fn


print("Connect Database : ", connectdb())
