import logging
import requests
import os
import time
import datetime


def get_url_list():
    urls = dict()
    urls['kompas']='https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg'
    urls['its']='https://www.its.ac.id/wp-content/uploads/2017/10/logo-its-1.png'
    urls['detik']='https://akcdn.detik.net.id/community/media/visual/2021/04/22/detikcom-ramadan-desktop-1.gif?d=1'
    urls['file1']='https://file-examples-com.github.io/uploads/2018/04/file_example_MOV_480_700kB.mov'
    #urls['file2']='https://file-examples-com.github.io/uploads/2018/04/file_example_MOV_1280_1_4MB.mov'
    urls['file3']='https://file-examples-com.github.io/uploads/2017/02/zip_2MB.zip'
    return urls


def download_gambar(url=None,tuliskefile=False):
    waktu_awal = datetime.datetime.now()
    if (url is None):
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/gif']='gif'
    tipe['image/jpeg']='jpg'
    tipe['application/zip']='jpg'
    tipe['video/quicktime']='mov'
    time.sleep(2) #untuk simulasi, diberi tambahan delay 2 detik

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        if (tuliskefile):
            fp = open(f"{namafile}.{ekstensi}","wb")
            fp.write(ff.content)
            fp.close()
        waktu_process = datetime.datetime.now() - waktu_awal
        waktu_akhir =datetime.datetime.now()
        logging.warning(f"writing {namafile}.{ekstensi} dalam waktu {waktu_process} {waktu_awal} s/d {waktu_akhir}")
        return waktu_process
    else:
        return False




if __name__=='__main__':
    #check fungsi
    k = download_gambar('https://asset.kompas.com/crops/qz_jJxyaZgGgboomdCEXsfbSpec=/0x0:998x665/740x500/data/photo/2020/03/01/5e5b52f4db896.jpg')
    print(k)