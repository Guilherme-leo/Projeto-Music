from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

KV = """
<Main>:
    orientation:'horizontal'
    Button:
        text: 'Salve salve comparsa'
    Button:
"""

Builder.load_string(KV)


class Main(BoxLayout):
    pass


class Programa(App):
    def build(self):
        return Main()


if __name__ == "__main__":
    Programa().run()
