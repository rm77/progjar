import threading
import time
import datetime

def worker(nomor):
    while True:
        waktu = datetime.datetime.now()
        print("{} Saya worker nomor {} \n".format(waktu, nomor))
        time.sleep(1)
    return


threads = []
for i in range(5):
    t = threading.Thread(target=worker,args=(i,))
    threads.append(t)
    
for thr in threads:
    thr.start()
	


