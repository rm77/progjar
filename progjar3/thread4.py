import threading
import time
import datetime

class Worker(threading.Thread):
    def __init__(self,nomor):
        self.nomor = nomor
        self.aktif = 1
        threading.Thread.__init__(self)
        self.daemon=True
    def stop(self):
        self.aktif = 0

    def run(self):
        while (True and (self.aktif==1)):
           waktu = datetime.datetime.now()
           print("{} Saya worker nomor {} \n".format(waktu, nomor))
           time.sleep(1)

def main():
    worker1 = Worker(1)
    worker2 = Worker(2)
    worker3 = Worker(3)
    worker4 = Worker(4)
    
    worker1.start()
    worker2.start()
    worker3.start()
    worker4.start()

    worker4.stop()


if __name__ == "__main__":
    try: 
      main()
      while True:
        pass
    except KeyboardInterrupt:
      print('Program stop')
