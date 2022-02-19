from requests import post, get
from time import sleep
from sqlite3 import connect
from json import dumps, load
from csv import reader, DictWriter
from datetime import datetime
from requests.exceptions import ConnectionError, HTTPError, Timeout, RequestException
from requests import ConnectionError, HTTPError
# from sys import exit
from threading import Thread
from PIL import Image, ImageDraw
import os
from urllib.request import urlretrieve

url_upload_data = "https://api-hr.systemkul.com/api/Attendances/AttendanceByDevice"
uuid_device = "2db5af4f-ed76-390e-9b71-e5704b0fd1a8"

# Loading image function:
def load_imgage(conn, datah):
    try:
        if not os.path.exists('../imageskios'):
            os.makedirs('../imageskios')
        pathht = os.listdir("../imageskios")
        for id_ald in datah[:4]:
            demtam = 0
            try:
                if id_ald["aliasID"] in pathht:
                    if "{}.jpg".format(id_ald["aliasID"]) in os.listdir(os.path.join("../imageskios", id_ald["aliasID"])):
                        continue
                    else:
                        demtam = 1
                else:
                    demtam = 1
                if demtam == 1:
                    if not os.path.exists(os.path.join("../imageskios",id_ald["aliasID"])):
                        os.makedirs(os.path.join("../imageskios",id_ald["aliasID"]))
                    urlretrieve(id_ald["avatar"], "../imageskios/{}/{}.jpg".format(id_ald["aliasID"], id_ald["aliasID"]))
                    img_save_4 = Image.open(os.path.join("../imageskios",id_ald["aliasID"],"{}.jpg".format(id_ald["aliasID"] )))
                    width, height = img_save_4.size
                    x = (width - height) // 2
                    img_cropped = img_save_4.crop((x, 0, x + height, height))
                    mask = Image.new('L', img_cropped.size)
                    mask_draw = ImageDraw.Draw(mask)
                    width, height = img_cropped.size
                    mask_draw.ellipse((10, 10, width-10, height-10), fill=255)
                    img_cropped.putalpha(mask)
                    img_save_4 = img_cropped.resize((512, 512), Image.ANTIALIAS)
                    img_save_4.save(os.path.join("../imageskios",id_ald["aliasID"],"{}.png".format(id_ald["aliasID"] )))
            except Exception as e:
                infor_s_Imgae1 = Thread(target=save_statu_bug, args=(conn, datetime.now(), "Anh error1", id_ald["aliasID"], e, ))
                infor_s_Imgae1.start() 
                print("Erorr 1 {}".format(e))
    except Exception as e:
        infor_s_Imgae2 = Thread(target=save_statu_bug, args=(conn, datetime.now(), "Anh error2", "Anh error2", e, ))
        infor_s_Imgae2.start() 
        print("Erorr 2 {}".format(e))

# Create connect to table
def create_connection(path_file):
    conn = None
    try:
        conn = connect(path_file, check_same_thread=False) 
        return conn
    except Exception as e:
        # print(e)
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

# Insert datahanet to projects
def insert_dataperson(conn, data):
    sql = ''' INSERT INTO dataperson (id,maNV,tenNV,chucVu,donVi)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

# Insert datahanet to projects
def insert_dataerrordata(conn, data):
    sql = ''' INSERT INTO dataperson (Datas,Types,Content,Scritp)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

# Insert datahanet to projects
def insert_dataallsaving(conn, data):
    sql = ''' INSERT INTO dataallsaving (ID,Temperature,Date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

# Insert datahanet to projects
def insert_dataerrordata(conn, data):
    sql = ''' INSERT INTO dataerrordata (Datas,Types,Content,Scritp)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid

def save_statu_bug(conn, dateTime, statueerr,data_request_new_text, erroText):
    project1 = (str(dateTime), str(statueerr), str(erroText), str(data_request_new_text) )
    try:
        insert_dataerrordata(conn, project1)
    except Exception as e:
        print(e)
        pass 

def call_data(conn):
    url_hanet       = "https://gateway.systemkul.com/api/Gateway/GetListPeopleByUnit"
    url_company     = "https://api-hr.systemkul.com/v1/NhanVien/Kiosk"
    string_post     = "66540EEE-61D6-48E2-B9B6-61BA0228B0FD"
    string_unicode  = "titkul"

    string_infor = {\
            "requestKey"    : string_post,      \
            "unitCode"      : string_unicode    \
        }
    # hanet
    rh = post(\
            url_hanet,  \
            data    = dumps(string_infor),      \
            headers = {'Content-Type': 'application/json-patch+json', }
        )
    datah = rh.json()
    for s in datah:
        project1 = (s["aliasID"], s["name"], s["avatar"], s["title"], s["personID"])
        try:
            insert_datahanet(conn, project1)
        except Exception as e:
            # print(e)
            pass 
    # company
    rc = get(url_company, \
        headers={'Content-Type': 'application/json-patch+json', })
    datac = rc.json()['data']
    for s in datac:
        project1 = (s["id"], s["maNV"], s["tenNV"], s["chucVu"], s["donVi"])
        try:
            insert_dataperson(conn, project1)
        except Exception as e:
            # print(e)
            pass 
    # Download images
    infor_s_Image = Thread(target=load_imgage, args=(conn, datah, ))
    infor_s_Image.start() 

def post_data(conn):
    # pass
    with open("data/recognization.csv", 'r') as read_obj:
        csv_reader = reader(x.replace('\0', '') for x in read_obj)
        try:
            statu_network = 0
            for row in csv_reader:
                try:
                    date = datetime.strptime(str(row[2]).split("+")[0], '%Y-%m-%d %H:%M:%S')
                    data = datetime.strftime(date, '%Y-%m-%dT%H:%M:%S.%f')
                    name_student_recognite = row[0]
                    tempt_student = row[1]
                    data_request_new = {
                        "employeeCode": name_student_recognite,
                        "temperature": float(tempt_student),
                        "time": str(date),
                        "deviceId": uuid_device
                        }

                    print(data_request_new)
                    r = post(url_upload_data, timeout=10, data=dumps(data_request_new), headers={'Content-Type': 'application/json-patch+json', })
                    print(r.status_code)
                    xstaute = r.status_code
                    try:
                        r.raise_for_status()
                    except HTTPError as errh:
                        print ("Http Error:",errh.response.text)
                        infor_s_Error = Thread(target=save_statu_bug, args=(conn, data, xstaute, data_request_new, errh.response.text, ))
                        infor_s_Error.start() 
                    except ConnectionError as errc:
                        print ("Error Connecting:",errc)
                        infor_s_ConnectionError = Thread(target=save_statu_bug, args=(conn, data, xstaute, data_request_new, errc, ))
                        infor_s_ConnectionError.start() 
                    except Timeout as errt:
                        print ("Timeout Error:",errt)
                        infor_s_Timeout = Thread(target=save_statu_bug, args=(conn, data, xstaute, data_request_new, errt, ))
                        infor_s_Timeout.start() 
                    except RequestException as err:
                        print ("OOps: Something Else",err)
                        infor_s_RequestException = Thread(target=save_statu_bug, args=(conn, data, xstaute, data_request_new, err, ))
                        infor_s_RequestException.start() 
                except ConnectionError:
                    print("No internet connection available.")
                    infor_s_ConnectionError = Thread(target=save_statu_bug, args=(conn, data,"No_internet",data_request_new, "No internet connection available", ))
                    infor_s_ConnectionError.start() 
                    statu_network = 1
                    return 1
                except Exception as e:
                    print("error 1 ",e)
                    pass 
            if  statu_network == 0:   
                with open ("data/recognization.csv", mode = "w") as re_csv_file:
                    fieldnames = ['ID', 'Temperature', 'Date' ]
                    writer = DictWriter(re_csv_file, fieldnames=fieldnames)
        except Exception as e :
            print("error 2 ",e)


if __name__=="__main__":
    namefile = "databaseA.db"
    conn = create_connection(namefile)
    call_data(conn)
    while True:
        value_net = post_data(conn)
        sleep(5)
        if value_net == 1:
            while True:
                try:
                    if get('https://google.com').ok:
                        print("You're Online")
                        infor_s_Connections = Thread(target=save_statu_bug, args=(conn, datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),"Connet_internet", "okie connect", "Connet internet {}".format(datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')), ))
                        infor_s_Connections.start() 
                        break
                except Exception as e:
                    print(e)
                    pass
        try:    
            now = datetime.now()
            # if (now.strftime("%X") >= cfg.timeshutshown):
            #     print("Tat kios")
            #     sleep(180)                              # cho sleep 3 phút đợi có phản hồi hay tác động gì hay không
            #     os.system("systemctl poweroff -i")      # tắt kios 
            # if (now - start).total_seconds() > timeconut:
            #     call_json()
            #     start = now
        except Exception as e:
            print(e)
            pass