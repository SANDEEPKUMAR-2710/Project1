import sqlite3

con = sqlite3.connect("sample.db",check_same_thread=False);

def getAll():
    query = "select * from college"
    cur = con.cursor()
    cur.execute(query)
    all_data = cur.fetchall()
    con.commit()
    return(all_data)

def insert(data):
    query1 = "create table if not exists college(RollNo varchar(10), Name varchar(20))"
    params = (data["Rollno"],data["Name"])
    query = "insert into college values(?,?)"
    cur = con.cursor()
    cur.execute(query1)
    cur.execute(query, params)
    con.commit()

