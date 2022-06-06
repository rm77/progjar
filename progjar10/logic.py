import os
import json
import base64
from glob import glob
import shelve
import time
import threading, queue

class Singleton:
    def __init__(self, cls):
        self._cls = cls
    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._cls()
            return self._instance
    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')
    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)

class QueueServer(threading.Thread):
    def __init__(self,idplayer='1'):
        self.idplayer = idplayer
        self.q = list()
        threading.Thread.__init__(self)
    def run(self):
        while True:
            pass
            #
            #print(self.idplayer)
            #time.sleep(0.1)

    def getall(self):
        h = list()
        for i in range(len(self.q)):
            h.append(self.q[i])
        return h

    def put(self,value=[]):
        self.q.append(value)
        return True
#player harus di register

@Singleton
class PlayerServerInterface:
    def __init__(self):
        self.queues = dict()
    def player_register(self,params=[]):
        idplayer = params[0]
        if (idplayer not in self.queues):
            self.queues[idplayer]=QueueServer(idplayer)
            self.queues[idplayer].start()
        return dict(status='OK')

    def get_players(self,params=[]):
        return dict(status='OK',jumlah=len(self.queues))

    def set_location(self,params=[]):
        pnum = params[0]
        #x = params[1]
        #y = params[2]
        try:
            self.queues[pnum].put(params)
            return dict(status='OK', player=pnum)
        except Exception as ee:
            print(str(ee))
            return dict(status='ERROR')

    def get_location(self,params=[]):
        pnum = params[0]
        try:
            h = self.queues[pnum].getall()
            return dict(status='OK',data=h)
        except Exception as ee:
            print(str(ee))
            return dict(status='ERROR')



if __name__=='__main__':
    p = PlayerServerInterface.Instance()
    #p.player_register(["1"])
    #p.player_register(["2"])
    #print(p.set_location(["1",100,100]))
    #print(p.set_location(["2",120,100]))
    #print(p.get_location('1'))
    #print(p.get_location('2'))
    #print(p.get_players())
