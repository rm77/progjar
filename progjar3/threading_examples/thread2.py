import threading
import time
import datetime
import logging

def worker(nomor):
    counter = 0
    while True:
        counter = counter + 1
        waktu = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%s")
        logging.warning(f"{waktu} saya adalah worker {nomor} counter {counter}")
        time.sleep(1)
    return


for i in range(5):
    t = threading.Thread(target=worker,args=(i,))
    t.start()


