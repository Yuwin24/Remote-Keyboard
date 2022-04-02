import threading
import socket
import json
from threading import Thread
from kivy.uix.gridlayout import GridLayout
from kivy.uix.vkeyboard import VKeyboard
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.app import App
from kivy.config import Config
import kivy
kivy.require("1.11.1")
Config.set('kivy', 'keyboard_mode', 'systemandmulti')


SERVER = None
PORT = 8000
IP_ADDRESS = "192.168.0.111"

BUFFER_SIZE = 4096


class MyApp(App):
    def build(self):
        layout = GridLayout(cols=1)
        keyboard = VKeyboard(on_key_up=self.key_up)
        self.label = Label(text="Selected key : ", font_size="50sp")

        layout.add_widget(self.label)
        layout.add_widget(keyboard)
        return layout

    def key_up(self, keyboard, keycode, *args):
        global SERVER
        if isinstance(keycode, tuple):
            keycode = keycode[1]
        self.label.text = "Selected key : "+str(keycode)
        print(str(keycode))
        SERVER.send((str(keycode)).encode('ascii'))

    def setup():
        global SERVER
        global PORT
        global IP_ADDRESS
        global remote_mouse
        PORT = 8000
        IP_ADDRESS = "192.168.0.111"

        try:
            SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            SERVER.connect((IP_ADDRESS, PORT))

            return True
        except:
            return False

    setup_thread = threading.Thread(target=setup)
    setup_thread.start()


if __name__ == '__main__':
    MyApp().run()
