from sqlite3 import connect

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
    aliasID_test = "9021"
    personID_test = "2056962459106680824"
    with conn:
        print("1. Query task by aliasID:")
        for row in select_aliasID(conn, aliasID_test):
            print(row) 
        print("1. Query task by personID:")
        for row in select_personID(conn, personID_test):
            print(row)
