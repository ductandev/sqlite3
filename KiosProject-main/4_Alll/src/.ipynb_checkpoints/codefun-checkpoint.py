import src.codefilesql as sql3

def save_statu_bug(conn, dateTime, statueerr,data_request_new_text, erroText):
    project1 = (str(dateTime), str(statueerr), str(erroText), str(data_request_new_text) )
    try:
        sql3.insert_dataerrordata(conn, project1)
    except Exception as e:
        print(e)
        pass 