import threading
import datetime

def worker(nomor):
    waktu = datetime.datetime.now()
    print "{} Saya worker nomor {} \n" . format(waktu,nomor)
    return


threads = []
for i in range(5):
    t = threading.Thread(target=worker,args=(i,))
    threads.append(t)
    t.start()


