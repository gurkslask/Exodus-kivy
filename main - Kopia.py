from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import *
from random import randint
from kivy.uix.button import Button
from kivy.uix.label import Label
from ExodusTrade import ExodusTrade
from kivy.uix.floatlayout import *
from kivy.base import runTouchApp
from kivy.uix.checkbox import CheckBox


class Exodus(FloatLayout):
    txt_inpt2 = StringProperty('')
    enint = NumericProperty(1)
    exo = ExodusTrade()
    txt_inpt = StringProperty('')
    act_turn = NumericProperty(0)

    def on_checkbox_active(self, checkbox, value):
        '''method for toggling advanced trading
        the method in exodustrade isnt ready yet, but this works , it is a toggle!'''
        if value and self.exo.AdvancedTrading:
            self.exo.AdvancedTrading = 0
        elif value and not self.exo.AdvancedTrading:
            self.exo.AdvancedTrading = 1

    def action(self, cmd):
        if cmd == 'bg':
            try:
                self.exo.BuyGreen()
                self.txt_inpt2 = str(self.exo.GetPlayerStash())
            except:
                self.txt_inpt2 = 'Wrong turn!'
        elif cmd == 'br':
            try:
                self.exo.BuyRed()
                self.txt_inpt2 = str(self.exo.GetPlayerStash())
            except:
                self.txt_inpt2 = 'Wrong turn!'
        elif cmd == 'sr':
            try:
                self.exo.SellRed()
                self.txt_inpt2 = str(self.exo.GetPlayerStash())
            except:
                self.txt_inpt2 = 'Wrong turn!'        
        elif cmd == 'sg':
            try:
                self.exo.SellGreen()
                self.txt_inpt2 = str(self.exo.GetPlayerStash())
            except:
                self.txt_inpt2 = 'Wrong turn!'

class PongApp(App):
    def build(self):
        return Exodus()
if __name__ == '__main__':
    PongApp().run()
