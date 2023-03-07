from library import download_gambar,get_url_list
import time
import datetime
from concurrent.futures import ThreadPoolExecutor



def download_semua():
    texec = dict()
    urls = get_url_list()

    catat_awal = time.perf_counter()

    with ThreadPoolExecutor() as executor:
        for k in urls:
            print(f"mendownload {urls[k]}")
            #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multithread
            executor.submit(download_gambar,urls[k])

    catat_akhir = time.perf_counter()
    selesai = round(catat_akhir - catat_awal,2)
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


#fungsi download_gambar akan dijalankan secara multithreading

if __name__=='__main__':
    download_semua()