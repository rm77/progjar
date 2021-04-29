import asyncio
from library import download_gambar,get_url_list
import time
import datetime
import threading




async def download_semua():
    texec = dict()
    urls = await get_url_list()

    catat_awal = datetime.datetime.now()
    for k in urls:
        print(f"mendownload {urls[k]}")
        waktu = time.time()
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download gambar secara multithread
        texec[k] = await download_gambar(urls[k]) #tanpa await, tidak akan melakukan apa apa


    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")


#fungsi download_gambar akan dijalankan secara multithreading

if __name__=='__main__':
    asyncio.run(download_semua())