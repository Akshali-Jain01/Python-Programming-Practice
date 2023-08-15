#Python Database connectivity
# db is an object name of sqlite whihc helps in connecting to database
import sqlite3
db = sqlite3.connect("mayank1.db")
cr = db.cursor()
# cr.execute("create table student (UNAME TEXT , PASSWORD TEXT)")
# cr.execute("insert INTO student values ('VIJAY','12345')")
# name = input("enter name")
# password = input("enter password")
# cr.execute("insert INTO student values ('"+name+"','"+password+"')")
# cr.execute("DELETE FROM Student WHERE UNAME = 'VIJAY'")
# cr.execute("DELETE FROM Student WHERE UNAME = '"+name+"'")
cr.execute("update student set PASSWORD =43  where UNAME = 'VIJAY'")
rows =cr.execute("select * from student")
for row in rows:
    print(row[0],row[1])

db.commit()
print("databse created")
db.close()
