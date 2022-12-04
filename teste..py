from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

KV = '''
ScrollView:

    MDList:
        id: container

'''


class alunos(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        alunos = ["Fulano","Sicrano", "Beltrano" ]
        for i in alunos:
            self.root.ids.container.add_widget(
                OneLineListItem(text=f"Nome: {i}")
            )

alunos().run()