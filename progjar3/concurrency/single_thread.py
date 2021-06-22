from library import download_gambar, get_url_list
import time
import datetime

def download_semua():
    urls = get_url_list()

    catat = datetime.datetime.now()
    for k in urls:
        print(f"mendownload {urls[k]}")
        waktu_proses = download_gambar(urls[k])
        print(f"completed {waktu_proses} detik")
    selesai = datetime.datetime.now() - catat
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik")


#fungsi download_gambar akan dijalankan secara berurutan

if __name__=='__main__':
    download_semua()