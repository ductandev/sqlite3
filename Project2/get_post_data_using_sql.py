import sqlite3
from sqlite3 import Error
from requests import get, post
from sqlite3 import connect
from json import dumps
from sys import exit

#================================== MY SQL ==============================================
## Tham so 

# aliasID PRIMARY KEY là duy nhất.
# PersonID NOT NULL không duy nhất. Cho phép thay đổi.
# Các key còn lại được phép thay đổi, và null.
sql_create_data3_table = """
    CREATE TABLE IF NOT EXISTS data3 (
        aliasID text PRIMARY KEY,
        name text,
        avatar text,
        title text, 
        personID text NOT NULL
    );
"""
sql_create_data5_table = """
    CREATE TABLE IF NOT EXISTS data5 (
        id integer PRIMARY KEY,
        maNV text,
        tenNV text NOT NULL,
        chucVu text,
        donVi text
    );
"""


## Define  request method
def get_data():
    url_hanet       = "https://api-vietthang.systemkul.com/v1/NhanVien/Kiosk"

    #---------GET DATA5--------------
    r = get(url_hanet, \
            headers = {'Content-Type': 'application/json-patch+json', }
        )
    # print(r.json())
    return  r.json()['data']    # chỉ lấy cục 'data': [{ }]
    
def post_data():

    ulr_getway      = "https://gateway.systemkul.com/api/Gateway/GetListPeopleByUnit"
    string_post     = "66540EEE-61D6-48E2-B9B6-61BA0228B0FD"
    string_unicode  = "VT"
    
    #---------GET DATA3--------------
    string_infor = {\
            "requestKey"    : string_post,      \
            "unitCode"      : string_unicode    \
        }
    r_getway = post(\
            ulr_getway,  \
            data    = dumps(string_infor),      \
            headers = {'Content-Type': 'application/json-patch+json', }
        )
    return r_getway.json()

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

# Insert data3 to database
def create_data3(conn, data):
    sql = ''' INSERT INTO data3 (aliasID,name,avatar,title,personID)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

# Insert data5 to database
def create_data5(conn, data1):
    sql = ''' INSERT INTO data5 (id,maNV,tenNV,chucVu,donVi)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data1)
    conn.commit()
    return cur.lastrowid

def main():
    global data3_id, data5_id
    
    
    #---------GET DATA3--------------
    try:
        data3_hanet  = post_data()
        print("GET DATA 3 DONE")
        # print(data3_hanet[:4])
    except Exception as e:
        print("GET DATA 3 FAILLLLLLLL !!!!")
        exit()
    #---------GET DATA5--------------
    try:
        data5_api    = get_data()
        print("GET DATA 5 DONE")
        # print(data5_api[:4])
    except Exception as e:
        print("GET DATA 5 FAILLLLLLLL !!!!")
        exit()


    # create a database connection
    path_data_file = r"database.db"
    conn = create_connection(path_data_file)
    
    # create tables
    if  conn is not None:
        # create data3 table
        create_tables(conn, sql_create_data3_table)
        # create data5 table
        create_tables(conn, sql_create_data5_table)
    else:
        print("Error!, cannot create the database connection.") 
        exit()
        
    data3_id = None
    with conn:
        for s in data3_hanet[:4]:
            data3 = (s["aliasID"], s["name"], s["avatar"], s["title"], s["personID"])
            try:
                data3_id = create_data3(conn, data3)
            except Exception as e:
                print(e)
                pass

        for s in data5_api[:4]:
            data5 = (s["id"], s["maNV"], s["tenNV"], s["chucVu"], s["donVi"])
            try:
                data5_id = create_data5(conn, data5)
            except Exception as e:
                print(e)
                pass

#----Run Main-----
main()