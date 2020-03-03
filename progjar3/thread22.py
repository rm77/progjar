import threading
import time
import datetime

def fungsi3():
    while True:
        waktu = datetime.datetime.now()
        print("{} saya adalah fungsi 3 yang berjalan \n" . format(waktu))
        time.sleep(4)
    return

def fungsi2():
    while True:
        waktu = datetime.datetime.now()
        print("{} saya adalah fungsi 2 yang berjalan \n" . format(waktu))
        time.sleep(2)
    return

def fungsi1():
    while True:
        waktu = datetime.datetime.now()
        print("{} saya adalah fungsi 1 yang berjalan \n".format(waktu))
        time.sleep(1)
    return


f1 = threading.Thread(target=fungsi1)
f1.start()

f2 = threading.Thread(target=fungsi2)
f2.start()

f3 = threading.Thread(target=fungsi2)
f3.start()
	


