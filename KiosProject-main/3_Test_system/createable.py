from sqlite3 import connect
from sys import exit

sql_getwayhanet = """
    CREATE TABLE IF NOT EXISTS datahanet (
        aliasID text PRIMARY KEY,
        name text,
        avatar text,
        title text, 
        personID text NOT NULL
    );
"""

sql_person = """
    CREATE TABLE IF NOT EXISTS dataperson (
        id integer NOT NULL,
        maNV text PRIMARY KEY,
        tenNV text,
        chucVu text, 
        donVi text
    );
"""

sql_backup_info = """
    CREATE TABLE IF NOT EXISTS dataallsaving (
        ID text ,
        Temperature text ,
        Date text
    );
"""

sql_error_add = """
    CREATE TABLE IF NOT EXISTS dataerrordata (
        Datas text ,
        Types text ,
        Content text,
        Scritp text
    );
"""

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

if __name__ == "__main__":

    namefile = "databaseA.db"
    conn = create_connection(namefile)
    if  conn is not None:
        create_tables(conn, sql_getwayhanet)
        create_tables(conn, sql_person)
        create_tables(conn, sql_backup_info)
        create_tables(conn, sql_error_add)
    else:
        print("Error!, cannot create the database connection.") 
        exit() 
