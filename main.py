import kivy
from kivy.app import App

from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


KV = '''
Screen:
    MDBoxLayout:
        orientation:'vertical'
        MDTopAppBar:
            title: 'SintProEdu'
            left_action_items: [['menu', lambda x: x]]
            right_action_items: [['dots-vertical', lambda x: x]]
        TelaLogin:
    
<SenhaCard>:
    orientation:'vertical'
    id: card
    size_hint: .9,.9
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    MDLabel:
        pos_hint: {'center_x': .5, 'center_y': .9}
        size_hint_x: .8
        text: 'Enviar link para redefinição de senha:'
        font_size: 15
    MDTextField:
        pos_hint: {'center_x': .5, 'center_y': .5}
        size_hint_x: .8
        text: 'Email cadastrado'
        icon_right: 'email'    
    MDRaisedButton:    
        text: 'Enviar'
        pos_hint: {'center_x': .5, 'center_y': .9}
        
    
<TelaLogin>:
    

    Image:
        source:'logo_nutri_lab.png'
        size_hint: 0.6, 0.6
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        allow_stretch: True
        
    MDTextField:
        size_hint_x: .8
        hint_text: 'Email:'
        id: Email
        icon_right: "account"
        pos_hint:  {'center_x': .5, 'center_y': .6}
        mode: "round"
    MDTextField:
        size_hint_x: .8
        hint_text: 'Senha:'
        id: Senha
        icon_right: "lock"
        pos_hint: {'center_x': .5, 'center_y': .5}
        mode: "round"
    MDRaisedButton:
        size_hint_x: .8
        pos_hint:  {'center_x': .5, 'center_y': .38}
        text: 'Login'
        font_size: 15
    MDRaisedButton:
        size_hint_x: .8
        pos_hint:  {'center_x': .5, 'center_y': .29}
        text: 'Cadastrar'
        font_size: 15
    MDLabel:
        pos_hint: { 'center_y': .20}
        halign: 'center'
        text: 'Esqueceu sua senha?'
        
    MDTextButton:
    
        pos_hint:  { 'center_x': .5, 'center_y': .15}
        
        text: 'Clique Aqui!'
        font_size: 12
        on_release: root.abrir_card()
'''


class SenhaCard(MDCard):
    pass


class TelaLogin(FloatLayout):
    def abrir_card(self):
        self.add_widget(SenhaCard())


class MyApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'Cyan'
        self.theme_cls.theme_style = 'Dark'
        return Builder.load_string(KV)


MyApp().run()