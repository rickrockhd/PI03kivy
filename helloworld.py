# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
kivy.require('1.9.1')
var = 0
def soma_um(instance):
    global var
    var += 1
    instance.text = str(var)

def test(instance):
    instance.text = 'Teste'

class MeuApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical',
                padding=[40, 20, 40, 20])
        layout.add_widget(Label(text='Olá do Kivy!'))
        btn = Button(text='Login', size=(100,25))
        btn2 = Button(text='Cadastro', size=(100,25))
        btn.bind(on_press=soma_um)
        btn2.bind(on_press=test)
        layout.add_widget(btn)
        layout.add_widget(btn2)
        return layout
if __name__ == '__main__':
    MeuApp().run()


