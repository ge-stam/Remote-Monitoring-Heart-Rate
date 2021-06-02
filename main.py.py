from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.popup import Popup
import heart_rate_calculator_application
import time
from kivy.uix.button import Button
from kivy.uix.label import Label
from pathlib import Path
from kivy.base import runTouchApp
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

import os


class FirstWindow(Screen):
    pass

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class ResultDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    text_input = ObjectProperty(None)

class MyPopup(Popup):
    pass

class SecondWindow(Screen):
    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
        self._popup.open()


    def load(self, path, filename):
        self._popup.dismiss()
        result = heart_rate_calculator_application.calculation(os.path.abspath(filename[0]))
        result = int(result)
        content = GridLayout(cols=1)
        content_cancel = Button(text='Return to Main Page', size_hint_y=None, height=40)
        if result < 100:
            content.add_widget(Label(text=f'Your heart rate is {result} bpm!',font_size='20sp', color=(0, 1, 0, 1)))
        else:
            content.add_widget(Label(text=f'Your heart rate is {result} bpm!',font_size='20sp', color=(1, 0, 0, 1)))
        content.add_widget(content_cancel)
        self._popup = Popup(title='Heart Rate Calculation',
                      size_hint=(None, None), size=(512, 512),
                      content=content, disabled=False)
        content_cancel.bind(on_release=self._popup.dismiss)
        self._popup.open()



class Editor(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)



class WindowManager(ScreenManager):
    pass



kv = Builder.load_file("kivy_manager.kv")


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyMainApp().run()
