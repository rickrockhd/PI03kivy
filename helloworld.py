# -*- coding: utf-8 -*-
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
# caso não iniciar e der o erro de OpenGL remova as '#' que servem da add comentario!!!!
#from kivy import Config
#Config.set('graphics', 'multisamples', '0')
#import os
#os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'


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
        layout = BoxLayout(orientation='vertical', padding=[40, 20, 40, 20])
        layout.add_widget(Label(text='PI03'))
        btn = Button(text='Login', size=(100, 25))
        btn2 = Button(text='Cadastro', size=(100, 25))
        btn.bind(on_press=soma_um)
        btn2.bind(on_press=test)
        layout.add_widget(btn)
        layout.add_widget(btn2)
        return layout


if __name__ == '__main__':
    MeuApp().run()


