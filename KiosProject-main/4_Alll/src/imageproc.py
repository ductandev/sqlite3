from PIL import Image, ImageDraw
import src.codefun as codf
from urllib.request import urlretrieve
from os import  makedirs, listdir
from os.path import join, exists
from datetime import datetime 
from threading import Thread
"""
Tai lieu huong dan su dung kios
"""
## Chech image having to folder. 
def check_Image(conn, id_ald, path_file, pathht):
    """
    Check cac thong tin co trong folder
    1. Check da co folder cua AliasID chua.
    2. Check da co image  trong folder do chua.
    """
    if id_ald["aliasID"] in pathht:
        if "{}.jpg".format(id_ald["aliasID"]) in listdir(join(path_file, id_ald["aliasID"])):
            return False
        else:
            return True
    else:
        return True

## Edit image from rang to  cicle!! 
def edit_image(conn, pathfile, id_img):
    """
    Edit lai Image tu hinh chu nhat thanh  hinh trong.
    """
    if not exists(join(pathfile,id_img["aliasID"])):
        makedirs(join(pathfile,id_img["aliasID"]))
    urlretrieve(id_img["avatar"], pathfile+"/{}/{}.jpg".format(id_img["aliasID"], id_img["aliasID"]))
    img_save_4 = Image.open(join(pathfile,id_img["aliasID"],"{}.jpg".format(id_img["aliasID"] )))
    width, height = img_save_4.size
    x = (width - height) // 2
    img_cropped = img_save_4.crop((x, 0, x + height, height))
    mask = Image.new('L', img_cropped.size)
    mask_draw = ImageDraw.Draw(mask)
    width, height = img_cropped.size
    mask_draw.ellipse((10, 10, width-10, height-10), fill=255)
    img_cropped.putalpha(mask)
    img_save_4 = img_cropped.resize((512, 512), Image.ANTIALIAS)
    img_save_4.save(join(pathfile,id_img["aliasID"],"{}.png".format(id_img["aliasID"] )))
def load_imgage(conn, datah):
    """
    Load anh, kiem tra kios  images. 
    1. Check co folder imageskios chua.
    2. Download chinh sua anh.
    3. Lỗi 3000 edit và download ảnh.
    """
    try:
        path_file_image = "../../imageskios"
        if not exists(path_file_image):
            makedirs(path_file_image)
        pathht = listdir(path_file_image)
        for id_ald in datah[:4]:
            try:
                if check_Image(conn, id_ald, path_file_image, pathht):
                    edit_image(conn, path_file_image, id_ald)
                else:
                    continue     
            except Exception as e:
                infor_s_Imgae1 = Thread(target=codf.save_statu_bug, args=(conn, datetime.now(), "3000", id_ald["aliasID"], e, ))
                infor_s_Imgae1.start() 
                print("Erorr types 3000 {}".format(e))
    except Exception as e:
        print("Erorr fix path {}".format(e))