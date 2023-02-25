from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.core.window import Window

from random import random

from kivy.graphics import (Color, Ellipse, Rectangle, Line)

class painterWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            Color(random(),random(),random(),1)
            rad = 15
            Ellipse(pos = (touch.x - rad / 2,touch.y - rad / 2),size = (rad,rad))
            touch.ud['line'] = Line(pos =(touch.x,touch.y), width = 15)
    
    def on_touch_move(self, touch):
        touch.ud['line'].points += (touch.x,touch.y)

class PaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = painterWidget()
        parent.add_widget(self.painter)

        parent.add_widget(Button(text='Очистить', on_press = self.clear_canvas, size = (200,100)))
        parent.add_widget(Button(text='Сохранить', on_press = self.save, size = (200,100), pos = (200,0)))
        parent.add_widget(Button(text='Скриншот', on_press = self.screen, size = (200,100), pos = (400,0)))


        return parent
    

    def clear_canvas(self, instance):
        self.painter.canvas.clear()

    def save(self,instace):
        self.painter.size = (Window.size[0],Window.size[1])
        self.painter.export_to_png('image.png')

    def screen(self,instace):
        Window.screenshot('screen.png')



if __name__ == '__main__':
    PaintApp().run()