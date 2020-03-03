import threading
import time
import datetime
from random import randint

def cls():
    for n in range(0, 64, 1): print("\r\n")

def locate(user_string="*", x=0, y=0):
	x=int(x)
	y=int(y)
	if x>=255: x=255
	if y>=255: y=255
	if x<=0: x=0
	if y<=0: y=0
	HORIZ=str(x)
	VERT=str(y)
	print("\033["+VERT+";"+HORIZ+"f"+user_string)


class Star(threading.Thread):
    def __init__(self,baris):
        self.baris = baris
        self.kolom = 1
        threading.Thread.__init__(self)
        self.daemon=True

    def run(self):
        while True:
           for x in range(1,50):
               locate(' ',x,self.baris)
           locate(' *',self.kolom,self.baris)
           self.kolom = self.kolom + 1 
           if (self.kolom>=50):
              self.kolom = 1
           time.sleep(randint(1,3))

def main():
    star1 = Star(1)
    star2 = Star(10)
    star3 = Star(15)
    star4 = Star(20)
    
    star1.start()
    star2.start()
    star3.start()
    star4.start()   

if __name__ == "__main__":
    try: 
      cls()
      main()
      while True:
        pass
    except KeyboardInterrupt:
      print(" Program Stop ..")
