import os
import json
import base64
from glob import glob
import shelve

#asumsi, hanya ada player 1, 2 , 3
class PlayerServerInterface:
    def __init__(self):
        self.players = shelve.open('g.db',writeback=True)
        self.players['1']= "100,100"
        self.players['2']= "100,100"
        self.players['3']= "100,100"
        self.players_face=dict()
        self.players_face['1']=base64.b64encode(open('images/red.png',"rb").read())
        self.players_face['2']=base64.b64encode(open('images/pink.png',"rb").read())
        self.players_face['3']=base64.b64encode(open('images/cyan.png',"rb").read())

    def get_all_players(self,params=[]):
        return dict(status='OK',players=list(self.players_face.keys()))

    def get_players_face(self, params=[]):
        pnum=params[0]
        try:
            return dict(status='OK',face=self.players_face[pnum].decode())
        except Exception as ee:
            return dict(status='ERROR')

    def set_location(self,params=[]):
        pnum = params[0]
        x = params[1]
        y = params[2]
        try:
            self.players[pnum]=f"{x},{y}"
            self.players.sync()
            return dict(status='OK', player=pnum)
        except Exception as e:
            return dict(status='ERROR')

    def get_location(self,params=[]):
        pnum = params[0]
        try:
            return dict(status='OK',location=self.players[pnum])
        except Exception as ee:
            return dict(status='ERROR')



if __name__=='__main__':
    p = PlayerServerInterface()
    p.set_location(['1',100,100])
    print(p.get_location('1'))
    p.set_location(['2',120,100])
    print(p.get_location('2'))
    print(p.get_players_face('1'))
    print(p.get_all_players())
