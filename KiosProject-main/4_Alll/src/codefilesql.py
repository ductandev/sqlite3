from sqlite3 import connect

# Create connect to table
def create_connection(path_file):
    conn = None
    try:
        conn = connect(path_file, check_same_thread=False) 
        return conn
    except Exception as e:
        print(e)
        pass
    return conn

# Insert datahanet to projects
def insert_datahanet(conn, data):
    sql = ''' INSERT INTO datahanet (aliasID,name,avatar,title,personID)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

# Insert dataperson to projects
def insert_dataperson(conn, data):
    sql = ''' INSERT INTO dataperson (id,maNV,tenNV,chucVu,donVi)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

# Insert dataerrordata to projects
def insert_dataerrordata(conn, data):
    sql = ''' INSERT INTO dataerrordata (Datas,Types,Content,Scritp)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

# Insert dataallsaving to projects
def insert_dataallsaving(conn, data):
    sql = ''' INSERT INTO dataallsaving (ID,Temperature,Date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid