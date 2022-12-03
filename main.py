import kivy
from kivy.app import App

#from kivy import Config
#Config.set('graphics', 'multisamples', '0')
#import os
#os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciadora(ScreenManager):
    pass


class SenhaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)


class TelaLogin(Screen):
    def abrir_card(self):
        self.add_widget(SenhaCard())


class TelaCadastro(Screen):
    pass


class TelaCadastroAluno(Screen):
    pass

class TelaCadastroEmpresa(Screen):
    pass

class TelaConfirmacaoCadastro(Screen):
    pass

class TelaBemVindo(Screen):
    pass
class TelaProjetos(Screen):
    pass

class MyApp(MDApp):

    def build(self):
        self.title = 'SintProEdu'
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_file('sintproedu.kv')

    def fechar(self):
        self.stop()


MyApp().run()