import random


# Cau hinh hanet
broker = '192.168.0.102'                               #****
port = 1883
topic = "/topic/detected/C21284M101"                    #****
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'lam'
password = '1234'

# Cau hinh file data
# APJsonI Systemschools
pathdata5 = 'hrdata/data/data5.json'
# API json getway
pathdata3 = 'hrdata/data/data3.json'
# File csv tam thoi config
save_tamthoi = "hrdata/data/recognization.csv"
# File csv backup config 
sav_packup = "hrdata/data/recognizationbakup.csv"

# Cau hinh file GUI 
image_title = "Image/1.png"                          #****
string_image_title = "welcometo_image"
# Cau hinh ten truong 
image_tentruong = "Image/2.png"                      #****
string_image_tentruong = "img_tentruong_and_website"    #****
# Neu khong co nguoi dem danh
logo_big = 'Image/3.png'                             #****
# Cau hinh anh nhan khong dung 
logo_unknow = 'Image/nguoila.png'
# Cau hinh file GUI  cho title 
# Cau hinh khai bao y te
image_khaibao = "Image/khaibaoyte_.png"              #****
string_image_khaibao = "hinh_qr_khaibaoyte"
# Cau hinh hotline
image_hotline = "Image/titkul_hotline3.png"
string_image_hotline = "titkul_hotline"
# Cau hinh title 
string_title_main = "VT_001_test"                           #****

#########################################################
uuid_media = "a22049f1-0682-3c90-af23-dd497e2a063d"     #****
