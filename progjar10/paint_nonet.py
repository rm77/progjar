from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from kivy.properties import StringProperty
import sys

cwarna = dict()
cwarna["yellow"]=[1,1,0]
cwarna["red"]=[1,0,0]
cwarna["blue"]=[0,0,1]
cwarna["green"]=[0,1,0]

class MyPaintWidget(Widget):
    idplayer=StringProperty("idplayer")
    warna=StringProperty("warna")
    def __init__(self,*args,**kwargs):
        self.warna = kwargs.get('warna') or 'red'
        super().__init__(**kwargs)

    def on_touch_down(self, touch):
        with self.canvas:
            a,b,c = cwarna[self.warna]
            Color(a,b,c)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):
    idplayer=StringProperty("idplayer")
    warna=StringProperty("warna")
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

