import streamlit as st
import pymysql as sql
import connectmysql as con

st.title("CRUD MySQL APP with Streamlit")

# สร้าง obj เพื่อเชื่อมต่อฐานข้อมูล
connection = con.connectdb()
cursor = connection.cursor()

# สร้าง fn สำหรับอ่านข้อมูลจากตาราง person


def read_person():
    cursor.execute("SELECT * from person ORDER BY id ASC")
    persons = cursor.fetchall()
    return persons


# สร้าง fn สำหรับเพิ่มข้อมูล
def create_person(fullname, email, age):
    try:
        cursor.execute(
            " INSERT INTO person (fullname, email,age) VALUES(%s,%s,%s)", (fullname, email, age))
        connection.commit()
        st.success("บันทึกสำเร็จ")
    except sql.Error:
        st.error(f'เกิดข้อผิดพลาด : {sql.Error}')

# สร้าง fn สำหรับแก้ไขข้อมูล


def update_person(fullname, email, age=0, id=0):
    try:
        cursor.execute(
            " Update person set fullname = %s, email = %s,age = %s where id = %s", (fullname, email, age, id))
        connection.commit()
        st.success("บันทึกสำเร็จ")
    except sql.Error:
        st.error(f'เกิดข้อผิดพลาด : {sql.Error}')


def delete_person(id=0):
    try:
        cursor.execute(
            " Delete from  person where id = %s", (id))
        connection.commit()
        st.success("ลบข้อมูลสำเร็จ")
    except sql.Error:
        st.error(f'เกิดข้อผิดพลาด : {sql.Error}')


# สร้างเมนู sidebar
menu = ["Home", "Insert", "Update", "Delete"]
# สร้างตัวเลือกใน sidebar
choice = st.sidebar.selectbox("Menu", menu)


# เมื่อผู้ใช้เลือกเมนู home
if choice == "Home":
    st.write("Home Person List")

    # เรียกการใช้งาน fn read_person()
    persons = read_person()
    # loop แสดงข้อมูลจากตาราง persons ในฐานข้อมูล
    table_data = []
    if persons:
        for person in persons:
            row = person
            table_data.append(row)
        st.table(table_data)
    else:
        st.write(" ## No Data ##")


elif choice == "Insert":
    st.write("Insert Person")
    fullname = st.text_input("Fullname :")
    email = st.text_input("Email :")

    # lable , min ,max, value default
    age = st.number_input("Age :", 1, 100, 1)

    # button create
    if st.button("Create"):
        if fullname and email and age:
            create_person(fullname, email, age)
            st.write("ข้อมูลครบถ้วน")
        else:
            st.write("กรุณากรอกข้อมูลให้ครบถ้วน")


elif choice == "Update":
    st.write("Update Person")
    id = st.number_input("Id :", 1, 100, 1)
    fullname = st.text_input("Fullname :")
    email = st.text_input("Email :")
    # lable , min ,max, value default
    age = st.number_input("Age :", 1, 100, 1)

    # button create
    if st.button("Update"):
        if id and fullname and email and age:
            update_person(fullname, email, age, id)
            st.write("ข้อมูลครบถ้วน")
        else:
            st.write("กรุณากรอกข้อมูลให้ครบถ้วน")


elif choice == "Delete":
    st.write("Delete Person")
    id = st.number_input("Id :", 1, 100, 1)

    # button create
    if st.button("Delete"):
        if id:
            delete_person(id)
            st.write("ลบข้อมูลครบถ้วน")
        else:
            st.write("กรุณากรอกข้อมูลให้ครบถ้วน")
