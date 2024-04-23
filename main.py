from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

VAR_1 = 0
VAR_2 = 0
VAR_3 = 0


class KIVYApp(App):

    def build(self):
        bl = BoxLayout(orientation='vertical', padding=[50, 50], spacing=20)
        bl.add_widget(Button(text='Кнопка 1', on_press=self.clic_1))
        bl.add_widget(Button(text='Кнопка 2', on_press=self.clic_2))
        bl.add_widget(Button(text='Кнопка 3', on_press=self.clic_3))
        return bl

    def clic_1(self, instance):
        global VAR_1
        VAR_1 += 1
        instance.text = f'{VAR_1}'

    def clic_2(self, instance):
        global VAR_2
        VAR_2 += 1
        instance.text = f'{VAR_2}'

    def clic_3(self, instance):
        global VAR_3
        VAR_3 += 1
        instance.text = f'{VAR_3}'


if __name__ == "__main__":
    kivy_app = KIVYApp()
    kivy_app.run()
