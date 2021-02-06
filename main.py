from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition


VALUE = 0.0575

size_x1, size_y1 = 1, 0.498
size_x2, size_y2 = 1, 0.498

pos_x2, pos_y2 = 0, 0.502


class Main(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def buts(self, n):
        if n == 1:
            self.but_1.id = "yes"
            # print(self.but_1.id)
        if n == 2:
            self.but_2.id = "yesSir"
            # print(self.but_2.id)
        elif self.but_1.id == "yes" and self.but_2.id == "yesSir":
            self.manager.transition = NoTransition()
            self.but_1.id = "no"
            self.but_2.id = "ynoSir"
            self.manager.current = 'third'




class Third(Screen, FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def logic(self, button):
        global size_x1, size_x2, size_y1, size_y2, pos_x2, pos_y2
        if button == 1:
            size_y1 += VALUE
            size_y2 -= VALUE
            pos_y2 += VALUE
            self.but1.size_hint = (size_x1, size_y1)
            self.but2.size_hint = (size_x2, size_y2)
            self.but2.pos_hint = {"x":pos_x2, "y":pos_y2}
            if size_y1 >= 1:
                print("Player 1 WIN")
                size_x1, size_y1 = 1, 0.498
                size_x2, size_y2 = 1, 0.498
                pos_x2, pos_y2 = 0, 0.502
                self.but1.size_hint = (size_x1, size_y1)
                self.but2.size_hint = (size_x2, size_y2)
                self.but2.pos_hint = {"x": pos_x2, "y": pos_y2}
                self.manager.current = 'fourth'

        elif button == 2:
            size_y1 -= VALUE
            pos_y2 -= VALUE
            size_y2 += VALUE
            self.but1.size_hint = (size_x1, size_y1)
            self.but2.size_hint = (size_x2, size_y2)
            self.but2.pos_hint = {"x":pos_x2, "y":pos_y2}
            if pos_y2 <= 0:
                size_x1, size_y1 = 1, 0.498
                size_x2, size_y2 = 1, 0.498
                pos_x2, pos_y2 = 0, 0.502
                self.but1.size_hint = (size_x1, size_y1)
                self.but2.size_hint = (size_x2, size_y2)
                self.but2.pos_hint = {"x": pos_x2, "y": pos_y2}
                print("Player 2 WIN")
                self.manager.current = 'five'


class Fourth(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Five(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class MyApp(App):

    def build(self):

        sm = ScreenManager()
        sm.add_widget(Main(name='first'))
        sm.add_widget(Third(name='third'))
        sm.add_widget(Fourth(name='fourth'))
        sm.add_widget(Five(name='five'))

        return sm


if __name__ == "__main__":
    MyApp().run()
