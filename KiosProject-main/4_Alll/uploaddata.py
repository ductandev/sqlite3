import src.codefilesql as sql3
import config.cofig as coff
import src.imageproc as img
import src.codefun as codf
from requests import get, post
from json import dumps
from csv import reader, DictWriter
from threading import Thread
from datetime import datetime
from time import sleep

from requests.exceptions import ConnectionError, HTTPError, Timeout, RequestException
from requests import ConnectionError, HTTPError


def post_data(conn):
    """
    """
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
                        "time": str(data),
                        "deviceId": coff.uuid_device
                        }

                    print(data_request_new)
                    r = post(coff.url_upload_data, timeout=10, data=dumps(data_request_new), headers={'Content-Type': 'application/json-patch+json', })
                    print(r.status_code)
                    xstatues = str(r.status_code)
                    try:
                        r.raise_for_status()
                    except Exception as e:
                        infor_post_Error = Thread(target=codf.save_statu_bug, args=(conn, data, xstatues, e, "Error post data", ))
                        infor_post_Error.start() 
                        print("Error {}: {}".format(xstatues, e))
                except ConnectionError as e:
                    print("No internet connection available.")
                    infor_s_ConnectionError = Thread(target=codf.save_statu_bug, args=(conn, data,'600',e, "No internet connection available", ))
                    infor_s_ConnectionError.start() 
                    statu_network = 1
                    return 1
                except Exception as e:
                    infor_s_Error = Thread(target=codf.save_statu_bug, args=(conn, data,'3001',e, "No structure correctly", ))
                    infor_s_Error.start() 
                    print("error 3001 ",e)
                    pass 
            if  statu_network == 0:   
                with open ("data/recognization.csv", mode = "w") as re_csv_file:
                    fieldnames = ['ID', 'Temperature', 'Date' ]
                    writer = DictWriter(re_csv_file, fieldnames=fieldnames)
        except Exception as e :
            print("error 2 ",e)

def call_data(conn):
    string_infor = {\
            "requestKey"    : coff.string_post,      \
            "unitCode"      : coff.string_unicode    \
        }
    # hanet
    rh = post(\
            coff.url_hanet,  \
            data    = dumps(string_infor),      \
            headers = {'Content-Type': 'application/json-patch+json', }
        )
    datah = rh.json()
    for s in datah:
        project1 = (s["aliasID"], s["name"], s["avatar"], s["title"], s["personID"])
        try:
            sql3.insert_datahanet(conn, project1)
        except Exception as e:
            print(e)
            pass 
    # company
    rc = get(coff.url_company, \
        headers={'Content-Type': 'application/json-patch+json', })
    datac = rc.json()['data']
    for s in datac:
        project1 = (s["id"], s["maNV"], s["tenNV"], s["chucVu"], s["donVi"])
        try:
            sql3.insert_dataperson(conn, project1)
        except Exception as e:
            print(e)
            pass 
    # Download images
    infor_s_Image = Thread(target=img.load_imgage, args=(conn, datah, ))
    infor_s_Image.start() 

if __name__ == "__main__":
    conn = sql3.create_connection(coff.namefile)
    call_data(conn)
    while True:
        value_net = post_data(conn)
        sleep(5)
        if value_net == 1:
            while True:
                try:
                    if get('https://google.com').ok:
                        print("You're Online")
                        break
                except Exception as e:
                    print(e)
                    pass