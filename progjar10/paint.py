from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line, Rectangle
from kivy.properties import StringProperty
from kivy.clock import  Clock
import queue

import sys

cwarna = dict()
cwarna["yellow"]=[1,1,0]
cwarna["red"]=[1,0,0]
cwarna["blue"]=[0,0,1]
cwarna["green"]=[0,1,0]

import socket
import logging
import json

class ClientInterface:
    def __init__(self,idplayer='1',warna="red"):
        self.cwarna = cwarna[warna]
        print(self.cwarna)
        self.idplayer=idplayer
        self.server_address=('0.0.0.0',6666)

    def send_command(self,command_str=""):
        global server_address
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(self.server_address)
        logging.warning(f"connecting to {self.server_address}")
        try:
            logging.warning(f"sending message ")
            command_str = f"{command_str} \r\n"
            #print(command_str.encode())
            sock.sendall(command_str.encode())
            # Look for the response, waiting until socket is done (no more data)
            data_received="" #empty string
            while True:
                #socket does not receive all data at once, data comes in part, need to be concatenated at the end of process
                data = sock.recv(16)
                if data:
                    #print(data)
                    #data is not empty, concat with previous content
                    data_received += data.decode()
                    if "\r\n\r\n" in data_received:
                        break
                else:
                    # no more data, stop the process by break
                    break
            # at this point, data_received (string) will contain all data coming from the socket
            # to be able to use the data_received as a dict, need to load it using json.loads()
            hasil = json.loads(data_received)
            logging.warning("data received from server:")
            return hasil
        except:
            logging.warning("error during data receiving")
            return False

    def set_location(self,x=100,y=100,eventname='mousedown'):
        player = self.idplayer
        w = " ".join([str(x) for x in self.cwarna])
        command_str=f"set_location {player} {eventname} {x} {y} {w}"
        #print(command_str)
        hasil = self.send_command(command_str)
        print(hasil)
        if (hasil['status']=='OK'):
            return True
        else:
            return False

    def get_location(self):
        player = self.idplayer
        command_str=f"get_location {player}"
        hasil = self.send_command(command_str)
        if (hasil['status']=='OK'):
            data = hasil['data']
            return data
        else:
            return False

    def get_location_other(self,idplayer='1'):
        player = idplayer
        command_str=f"get_location {player}"
        hasil = self.send_command(command_str)
        if (hasil['status']=='OK'):
            data = hasil['data']
            return data
        else:
            return False


    def get_players(self):
        command_str=f"get_players"
        hasil = self.send_command(command_str)
        print(hasil)
        if (hasil['status']=='OK'):
            data = hasil['jumlah']
            return data
        else:
            return False

    def player_register(self,player_num=1):
        command_str=f"player_register {player_num}"
        hasil = self.send_command(command_str)
        if (hasil['status']=='OK'):
            return True
        else:
            return False


class MyPaintWidget(Widget):
    idplayer=StringProperty("idplayer")
    warna=StringProperty("warna")
    def __init__(self,*args,**kwargs):
        self.warna = kwargs.get('warna') or 'red'
        self.idplayer = kwargs.get('idplayer') or '1'
        self.client_interface = ClientInterface(idplayer=self.idplayer,warna=self.warna)
        self.client_interface.player_register(self.idplayer)
        super().__init__(**kwargs)
        self.q = queue.Queue()
        Clock.schedule_interval(self.refresh, 1/60 )


    def refresh(self,callback):
        for i in range(self.client_interface.get_players()):
            data = self.client_interface.get_location_other(str(i+1))
            for d in data:
                #(d)
                try:
                    playernum, j, x,y,r,g,b = d
                    #print(d)
                    with self.canvas:
                        Color(int(r), int(g), int(b))
                        Rectangle(pos=(int(x),int(y)),size=(10,10))
                except:
                    pass

    def on_touch_down(self, touch):
        with self.canvas:
            #a,b,c = cwarna[self.warna]
            #Color(int(a),int(b),int(c))
            #touch.ud['line'] = Line(points=(touch.x, touch.y))
            self.client_interface.set_location(int(touch.x),int(touch.y),'mousedown')

    def on_touch_move(self, touch):
        #touch.ud['line'].points += [touch.x, touch.y]
        self.client_interface.set_location(int(touch.x), int(touch.y),eventname='mousemove')


class MyPaintApp(App):
    idplayer=StringProperty("idplayer")
    warna=StringProperty("warna")
    players = []
    def __init__(self,**kwargs):
        super().__init__(**kwargs)



    def build(self):
        return MyPaintWidget(idplayer=self.idplayer,warna=self.warna)


if __name__ == '__main__':
    idplayer = '1'
    warna = 'red'
    try:
        idplayer = sys.argv[1]
        warna = sys.argv[2]
    except:
        pass
    MyPaintApp(idplayer=idplayer, warna=warna).run()

