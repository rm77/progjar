from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle, Line
from functools import partial
from kivy.clock import  Clock

import socket
import logging
import json


class Player:
    def __init__(self,idplayer='1',r=1,g=0,b=0):
        self.current_x = 100
        self.current_y = 100
        self.warna_r = r
        self.warna_g = g
        self.warna_b = b
        self.idplayer = idplayer
        self.widget = Widget()
        self.buttons = None
        self.inisialiasi()
        #self.draw(self.widget,self.warna_r,self.warna_g,self.warna_b)
    def get_idplayer(self):
        return self.idplayer
    def set_xy(self,x=100,y=100):
        self.current_x = x
        self.current_y = y
        self.draw()
        #self.draw(self.widget, self.warna_r, self.warna_g, self.warna_b)

    def get_widget(self):
        return self.widget
    def get_buttons(self):
        return self.buttons

    def draw(self):
        #self.current_x, self.current_y = self.client_interface.get_location()
        wid = self.widget
        r = self.warna_r
        g = self.warna_g
        b = self.warna_b

        with wid.canvas:
            Color(r,g,b)
            Line(rectangle=(self.current_x,self.current_y, 200, 200))

    def move(self,wid, arah,*kwargs):
        #self.draw(wid,0,0,0)
        if (arah=='right'):
            self.current_x = self.current_x + 10
        if (arah=='left'):
            self.current_x = self.current_x - 10
        if (arah=='up'):
            self.current_y = self.current_y + 10
        if (arah=='down'):
            self.current_y = self.current_y - 10
        #self.client_interface.set_location(self.current_x,self.current_y)
        #self.draw(wid,self.warna_r,self.warna_g,self.warna_b)

    def inisialiasi(self):
        wid = self.widget
        btn_left = Button(text='left',on_press=partial(self.move, wid, 'left'))
        btn_up = Button(text='up',on_press=partial(self.move, wid, 'up'))
        btn_down = Button(text='down',on_press=partial(self.move, wid, 'down'))
        btn_right = Button(text='right',on_press=partial(self.move, wid, 'right'))

        self.buttons = BoxLayout(size_hint=(1, None), height=50)
        self.buttons.add_widget(btn_left)
        self.buttons.add_widget(btn_up)
        self.buttons.add_widget(btn_down)
        self.buttons.add_widget(btn_right)



class MyApp(App):
    players = []
    def refresh(self,callback):
        for i in self.players:
            i.get_widget().canvas.clear()
            i.draw()

    def build(self):

        p1 = Player('1',1,0,0)
        p1.set_xy(100,100)
        widget1 = p1.get_widget()
        buttons1 = p1.get_buttons()
        self.players.append(p1)


        p2 = Player('2',0,1,0)
        p2.set_xy(100,200)
        widget2 = p2.get_widget()
        buttons2 = p2.get_buttons()
        self.players.append(p2)

#        p3 = Player('3',0,1,0)
#        p3.set_xy(150,150)
#        widget3 = p3.get_widget()
#        buttons3 = p3.get_buttons()
#        self.players.append(p3)

#        p4 = Player('4',0,1,1)
#        p4.set_xy(150,150)
#        widget4 = p4.get_widget()
#        buttons4 = p4.get_buttons()
#        self.players.append(p4)

        root = BoxLayout(orientation='horizontal')
        root.add_widget(widget1)
        root.add_widget(buttons1)
        root.add_widget(widget2)
        root.add_widget(buttons2)
#        root.add_widget(widget3)
#        root.add_widget(buttons3)
#        root.add_widget(widget4)
#        root.add_widget(buttons4)


        Clock.schedule_interval(self.refresh,1/60)

        return root

if __name__ == '__main__':
    MyApp().run()