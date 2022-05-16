import curses
import threading
from curses.textpad import Textbox, rectangle
import threading
import shlex
from library import *
import random

class MyIRCClient(threading.Thread):
    def __init__(self,ircserver='irc.undernet.org',ircport=6669):
        self.ircserver = ircserver
        self.ircport = ircport
        self.sock = None
        self.win = None
        self.jalan = True
        self.sock = make_socket(self.ircserver, self.ircport)
        threading.Thread.__init__(self)
    def setwin(self,win):
        self.win = win
    def auth(self,params):
        username = params[0]
        realname=params[1]
        kirim = f"\nNICK {username}\n\nUSER {username} * * {realname}\n"
        self.win.addstr(kirim)
        self.sock.sendall(kirim.encode())
    def join(self,params):
        namachannel = params[0]
        kirim = f"JOIN {namachannel}\n"
        self.win.addstr(kirim)
        self.sock.sendall(kirim.encode())
    def sendmessage(self,params):
        tujuan=params[0]
        message=params[1]
        kirim = f"PRIVMSG {tujuan} :{message} \n"
        self.win.addstr(kirim)
        self.sock.sendall(kirim.encode())
    def ping(self,params):
        kirim = f"PING {random.randint(10000,12000)} \n"       
        self.win.addstr(kirim)
        self.sock.sendall(kirim.encode())
    def stopit(self):
        self.jalan = False
    def run(self):
        data_received = ""
        baris = []
        while self.jalan == True:
            data = self.sock.recv(32)
            if data:
                # data is not empty, concat with previous content
                data_received += data.decode()
                #logging.warning(data_received)
            for g in data_received.splitlines():
                self.win.addstr(f"{g}\n")
            self.win.refresh()


class MyInputProcessor:
    def __init__(self, irc_client_thread):
        self.irc_client_thread = irc_client_thread
    def execute(self,s):
        c = shlex.split(s)
        try:
            command = c[0]
            params = [x for x in c[1:]]
            cl = getattr(self.irc_client_thread,command)(params)
            return cl
        except Exception as ee:
            return f"ERROR: {str(ee)}"








class MyUI(threading.Thread):
    def __init__(self):
        self.irc_client = None
        self.input_processor = None
        threading.Thread.__init__(self)
    def run(self):
        curses.wrapper(self.interaksi)
    def interaksi(self,stdscr):
        stdscr = curses.initscr()
        curses.echo()
        stdscr.clear()
        stdscr.refresh()
        stdscr.border(0)
        height, width = stdscr.getmaxyx()
        boxwin = curses.newwin(height,width)
        boxwin.scrollok(True)
        stdscr.addstr(height-2, 0, "Masukkan perintah")
        boxwin.refresh()
        #boxwin.box()
        self.irc_client = MyIRCClient()
        self.irc_client.setwin(boxwin)
        self.input_processor = MyInputProcessor(self.irc_client)
        self.irc_client.start()

        while True:
            #stdscr.clear()
            s = stdscr.getstr(height-1,0,90)
            boxwin.addstr(f"[C]---> {s.decode()}\n")
            boxwin.refresh()
            if s.decode()=="quit":
                curses.endwin()
                self.irc_client.stopit()
                break
            result = self.input_processor.execute(s.decode())
            #boxwin.clear()
            if (type(result) is str):
                if result.startswith("ERROR"):
                    stdscr.addstr(height-2,0,result)
            #boxwin.refresh()
            stdscr.refresh()

if __name__=='__main__':
    t = MyUI()
    t.start()
    t.join(timeout=5)

