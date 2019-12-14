import sqlite3
conn = sqlite3.connect(#server name with user and password)
c=conn.cursor()

def create_table():
    c.execute("CREATE TABLE  mydata(Name varchar(255), Email varchar(255), phoneNo int, Skills varchar(455)")

def data_entry():
    c.execute("INSERT INTO mydata VALUES('Aritra Dutta','dutta94aritra24@gmail.com','9123948859', 'Basic of Python, Basic of OOPs , Basic of Core Java , Basic of C Language'")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()

