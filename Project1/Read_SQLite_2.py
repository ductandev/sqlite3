from sqlite3 import connect
from tkinter import E

# Connection with database file
def create_connection(db_file):
    conn = None
    try:
        conn = connect(db_file)
        return  conn
    except Exception as e:
        print(e)
    return conn

## Find to  aliasID
def select_aliasID(conn, data):

    cur = conn.cursor()
    cur.execute("SELECT * FROM datahanet WHERE aliasID=?", (data,))

    rows = cur.fetchall()
    return rows
 
## Find to personID   
def select_personID(conn, data):

    cur = conn.cursor()
    cur.execute("SELECT * FROM datahanet WHERE personID=?", (data,))

    rows = cur.fetchall()
    return rows

if __name__=="__main__":
    path_database = r"2hanetdatabase.db"
    conn = create_connection(path_database)
    while True:
        try:
            print("Thong tin aliasID cua nguoi dung:\n")
            aliasID_test = str(input())
            with conn:
                print("1. Query task by aliasID:")
                for row in select_aliasID(conn, aliasID_test):
                    print(row) 
        except Exception as e:
            print(e)
            break