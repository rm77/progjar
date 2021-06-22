import threading
import datetime
import logging

def worker(nomor):
    waktu = datetime.datetime.now()
    logging.warning(f"saya worker nomor {nomor}")
    return


threads = []
for i in range(5):
    t = threading.Thread(target=worker,args=(i,))
    t.start()


