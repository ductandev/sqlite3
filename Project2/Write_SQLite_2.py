# from msilib.schema import Error
from unittest import signals
from requests import post
from sqlite3 import connect
from json import dumps, load
from sys import exit
import  data_update as in_up

## Tham so 

# aliasID PRIMARY KEY là duy nhất.
# PersonID NOT NULL không duy nhất. Cho phép thay đổi.
# Các key còn lại được phép thay đổi, và null.
sql_create_table = """
    CREATE TABLE IF NOT EXISTS datahanet (
        aliasID text PRIMARY KEY,
        name text,
        avatar text,
        title text, 
        personID text NOT NULL
    );
"""

## Define  request method
def post_data():
    url_hanet       = "https://gateway.systemkul.com/api/Gateway/GetListPeopleByUnit"
    string_post     = "66540EEE-61D6-48E2-B9B6-61BA0228B0FD"
    string_unicode  = "nguyenvancu"

    string_infor = {\
            "requestKey"    : string_post,      \
            "unitCode"      : string_unicode    \
        }
    r = post(\
            url_hanet,  \
            data    = dumps(string_infor),      \
            headers = {'Content-Type': 'application/json-patch+json', }
        )
    return  r.json()

# Create connect to table
def create_connection(path_file):
    conn = None
    try:
        conn = connect(path_file) 
        return conn
    except Exception as e:
        print(e)
    return conn

# Create structe for table     
def create_tables(conn, data_tables_sql):
    try:
        c = conn.cursor()
        c.execute(data_tables_sql)
    except Exception as e:
        print(e)

# Insert data to projects
def create_project(conn, data):
    sql = ''' INSERT INTO datahanet (aliasID,name,avatar,title,personID)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid
    
# Update database
def update_data(conn, data):
    sql = ''' UPDATE datahanet
              SET name = ? ,
                  avatar = ? ,
                  title = ?,
                  personID = ?
              WHERE aliasID = ?'''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
# Dinh nghia ham del
def delete_task(conn, data):
    sql = 'DELETE FROM datahanet WHERE aliasID=?'
    cur = conn.cursor()
    cur.execute(sql, (data,))
    conn.commit()

# Dinh nghia ham main
if __name__=="__main__":
    try:
        data_hanet  = post_data()
        # print(data_hanet[:4])
    except Exception as e:
        print("Thong tin lai loai cho he thong!!!!")
        exit()
    path_data_file = r"2hanetdatabase.db"
    conn = create_connection(path_data_file)
    if  conn is not None:
        create_tables(conn, sql_create_table)
    else:
        print("Error!, cannot create the database connection.") 
        exit() 
    project_id = None
    while True:
        try:
            signalS = str(input("Input statue connect!  "))
            if signalS == "ins":
                ff = open("data_insert.json", "r")
                dataf = load(ff)
                for s in dataf:
                    project1 = (s["aliasID"], s["name"], s["avatar"], s["title"], s["personID"])
                    try:
                        project_id = create_project(conn, project1)
                    except Exception as e:
                        print(e)
                        pass 
            elif signalS == "del":
                print("Nhap vao aliasID can so:")
                fdata1 = input() 
                with conn:
                    delete_task(conn, str(fdata1))
            elif signalS == "upd":
                with conn:
                    update_data(conn, in_up.dataupdate)
            else:
                pass
        except Exception as e:
            print(e)
            break
