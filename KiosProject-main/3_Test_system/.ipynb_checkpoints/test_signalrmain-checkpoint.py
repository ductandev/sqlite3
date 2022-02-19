import logging
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
from signalrcore.hub_connection_builder import HubConnectionBuilder

# def input_with_default(input_text, default_value):
#     value = input(input_text.format(default_value))
#     return default_value if value is None or value.strip() == "" else value

UUID = cfg.uuid_device                  # "2db5af4f-ed76-390e-9b71-e5704b0fd1a8"
def token():
    return cfg.token


def prinfile(msg):
    if (str(msg[0]) == "lam"):
        call_json()


def checkHealth(msg):
    hub_connection.invoke("CheckHealth")


def call_json():
    r = get(cfg.url_hanet, \
            data=dumps(cfg.string_post), \
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
                    if "{}.jpg".format(id_ald["aliasID"]) in os.listdir(os.path.join("imageskios", id_ald["aliasID"])):
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

# --------------------------------------------------------------------------------
#                           MAIN
# --------------------------------------------------------------------------------
if __name__ == '__main__':
    # server_url = input_with_default('Enter your server url(default: {0}): ', "https://gateway-staging.systemkul.com/signalR")
    # username = input_with_default('Enter your username (default: {0}): ', "mandrewcito")
    server_url = cfg.url_signalR                        # link url ****
    hub_connection = HubConnectionBuilder() \
        .with_url(server_url, options={ "skip_negotiation": False,"verify_ssl": True,\
             "access_token_factory": token }) \
        .configure_logging(logging.DEBUG) \
        .with_automatic_reconnect({
           "type": "interval",
           "keep_alive_interval": 100,
           "reconnect_interval": 100,
           "max_attempts": 100
        }).build()

    hub_connection.on("ABC", prinfile)
    hub_connection.on("CheckHealth", checkHealth)
    hub_connection.on_open(lambda: print("connection opened and handshake received ready to send messages"))
    hub_connection.on_close(lambda: print("connection closed"))
    hub_connection.start()
    message = None
    # Do login
    while message != "exit()":
        message = input(">> ")
        # if message is not None and message is not "" and message is not "exit()":
        #     hub_connection.send("ABC", [username, message])
    # hub_connection.stop()
