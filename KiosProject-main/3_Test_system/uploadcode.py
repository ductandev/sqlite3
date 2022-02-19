from time import sleep
from csv import reader, DictWriter
from json import dumps, loads, dump, load

from requests import ConnectionError, HTTPError
from requests import get, post
from datetime import datetime
from requests.exceptions import ConnectionError, HTTPError, Timeout, RequestException

from PIL import Image, ImageDraw, ImageFont
import os
import configupload as cfg

import urllib.request

from threading import Thread


def load_imgage(M1111):
    try:
        f_img = open(cfg.json_data3, 'r')
        data_infor = load(f_img)
        if not os.path.exists('../imageskios'):
            os.makedirs('../imageskios')
        pathht = os.listdir("../imageskios")
        for id_ald in data_infor:
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
                    urllib.request.urlretrieve(id_ald["avatar"], "../imageskios/{}/{}.jpg".format(id_ald["aliasID"], id_ald["aliasID"]))
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
                infor_s_Imgae1 = Thread(target=save_statu_bug, args=(datetime.now(), "Anh error1", id_ald["aliasID"], e, ))
                infor_s_Imgae1.start() 
                print("Erorr 1 {}".format(e))
    except Exception as e:
        infor_s_Imgae2 = Thread(target=save_statu_bug, args=(datetime.now(), "Anh error2", "Anh error2", e, ))
        infor_s_Imgae2.start() 
        print("Erorr 2 {}".format(e))

def call_json():
    r = get(cfg.url_hanet, \
            headers={'Content-Type': 'application/json-patch+json', })
    data1 = r.json()['data']
    with open(cfg.json_data5, 'w') as f:
        dump(data1, f)  

    string_infor = { \
        "requestKey": cfg.string_post, \
        "unitCode": cfg.string_unitCode \
        }
    r_getway = post(cfg.ulr_getway,\
                    data=dumps(string_infor), \
            headers={'Content-Type': 'application/json-patch+json', })
    data_getway = r_getway.json()
    with open(cfg.json_data3, 'w') as f_getway:
        dump(data_getway, f_getway)
    infor_s_ConnectionError = Thread(target=save_statu_bug, args=(datetime.now(),"Download json","Download json", "Download json Successful", ))
    infor_s_ConnectionError.start() 
    infor_s_Image = Thread(target=load_imgage, args=("M", ))
    infor_s_Image.start() 

def save_statu_bug(dateTime, statueerr,data_request_new_text, erroText):
    with open (cfg.history_csv, mode = "+a") as re_csv_file1:
        fieldnames = ['date','statu', 'data_request_new' , 'erroText']
        writer = DictWriter(re_csv_file1, fieldnames=fieldnames)
        writer.writerow({'date':dateTime,'statu': statueerr, 'data_request_new': str(data_request_new_text), 'erroText': erroText}) 
        re_csv_file1.close()

def post_data():
    # pass
    with open(cfg.tamthoi_csv, 'r') as read_obj:
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
                        "deviceId": cfg.uuid_device
                        }

                    print(data_request_new)
                    r = post(cfg.url_upload_data, timeout=10, data=dumps(data_request_new), headers={'Content-Type': 'application/json-patch+json', })
                    print(r.status_code)
                    xstaute = r.status_code
                    try:
                        r.raise_for_status()
                    except HTTPError as errh:
                        print ("Http Error:",errh.response.text)
                        infor_s_Error = Thread(target=save_statu_bug, args=(data, xstaute, data_request_new, errh.response.text, ))
                        infor_s_Error.start() 
                    except ConnectionError as errc:
                        print ("Error Connecting:",errc)
                        infor_s_ConnectionError = Thread(target=save_statu_bug, args=(data, xstaute, data_request_new, errc, ))
                        infor_s_ConnectionError.start() 
                    except Timeout as errt:
                        print ("Timeout Error:",errt)
                        infor_s_Timeout = Thread(target=save_statu_bug, args=(data, xstaute, data_request_new, errt, ))
                        infor_s_Timeout.start() 
                    except RequestException as err:
                        print ("OOps: Something Else",err)
                        infor_s_RequestException = Thread(target=save_statu_bug, args=(data, xstaute, data_request_new, err, ))
                        infor_s_RequestException.start() 
                except ConnectionError:
                    print("No internet connection available.")
                    infor_s_ConnectionError = Thread(target=save_statu_bug, args=(data,"No_internet",data_request_new, "No internet connection available", ))
                    infor_s_ConnectionError.start() 
                    statu_network = 1
                    return 1
                except Exception as e:
                    print("error 1 ",e)
                    pass 
            if  statu_network == 0:   
                with open (cfg.tamthoi_csv, mode = "w") as re_csv_file:
                    fieldnames = ['ID', 'Temperature', 'Date' ]
                    writer = DictWriter(re_csv_file, fieldnames=fieldnames)
        except Exception as e :
            print("error 2 ",e)

if __name__ == "__main__":
    timeconut = 900    #21600
    start = datetime.now()
 
    try:
        call_json()
        sleep(10)
    except Exception as e:
        print("hello2 ",e)
    while True:
        value_net = post_data()
        sleep(5)
        if value_net == 1:
            while True:
                try:
                    if get('https://google.com').ok:
                        print("You're Online")
                        infor_s_Connections = Thread(target=save_statu_bug, args=(datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f'),"Connet_internet", "okie connect", "Connet internet {}".format(datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')), ))
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
            if (now - start).total_seconds() > timeconut:
                call_json()
                start = now
        except Exception as e:
            print(e)
            pass
