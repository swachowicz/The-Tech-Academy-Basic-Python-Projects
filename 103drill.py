
import sqlite3
import os


#   create connection & database:

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    create_connection("C:\\sqlite\db\pythonsqlite.db")

#   create tbl_JobApps

conn = sqlite3.connect('pythonsqlite.db')

with conn:
    #cur = cursor, operates on actual database
    cur = conn.cursor()
    #sql code in string w/ integer primary key autoincrement
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_JobApps( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_company TEXT, \
        col_jobtitle TEXT, \
        col_datesubmitted TEXT \
        )")
    conn.commit()
conn.close()

#   insert data into tbl_JobApps

conn = sqlite3.connect('pythonsqlite.db')

with conn:
    #cur = cursor, operates on actual database
    cur = conn.cursor()
    #sql code in string
    cur.execute("INSERT INTO tbl_JobApps(col_company, col_jobtitle, col_datesubmitted) VALUES (?,?,?)", \
                ('Amazon', 'Software Engineer', '01/09/2019'))
    cur.execute("INSERT INTO tbl_JobApps(col_company, col_jobtitle, col_datesubmitted) VALUES (?,?,?)", \
                ('Intel', 'Software Engineer', '01/16/2019'))
    cur.execute("INSERT INTO tbl_JobApps(col_company, col_jobtitle, col_datesubmitted) VALUES (?,?,?)", \
                ('Boeing', 'Software Engineer', '01/31/2019'))
    cur.execute("INSERT INTO tbl_JobApps(col_company, col_jobtitle, col_datesubmitted) VALUES (?,?,?)", \
                ('UHaul', 'Business Analyst', '02/04/2019'))
    conn.commit()
conn.close()

conn = sqlite3.connect('pythonsqlite.db')

#   create tbl_TextDocs

with conn:
    #cur = cursor, operates on actual database
    cur = conn.cursor()
    #sql code in string w/ integer primary key autoincrement
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_TextDocs( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_name TEXT \
        )")
    conn.commit()
conn.close()

# grab .txt files & insert into tbl_TextDocs

fPath = 'C:\\A\\'
      

items = os.listdir(fPath)

newlist = []
for names in items:
    if names.endswith(".txt"):
        newlist.append(names)
        abPath = os.path.join(fPath + names)

        print(names)

        conn = sqlite3.connect('pythonsqlite.db')

        with conn:
            #cur = cursor, operates on actual database
            cur = conn.cursor()
            #sql code in string
            cur.execute("INSERT INTO tbl_TextDocs(col_name) VALUES (?)", \
                        [names])
            conn.commit()
        conn.close()

#   insert data into TextDocs Table





