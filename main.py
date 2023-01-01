import os
from kivy import Config

Config.set("graphics", "width", "960")
Config.set("graphics", "height", "720")
Config.set("graphics", "minimum_width", "960")
Config.set("graphics", "minimum_height", "720")
from kivy.lang import Builder
from kivymd.uix.scrollview import MDScrollView
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory
import pyrebase

from kivymd.uix.transition.transition import MDFadeSlideTransition


firebaseConfig = {
    "apiKey": "AIzaSyAyNHQdLavkZrorZr-OdQ0Px3DKtvnrwmc",
    "authDomain": "healthbudd-initial.firebaseapp.com",
    "databaseURL": "https://healthbudd-initial-default-rtdb.firebaseio.com",
    "projectId": "healthbudd-initial",
    "storageBucket": "healthbudd-initial.appspot.com",
    "messagingSenderId": "198554498567",
    "appId": "1:198554498567:web:4decf44af73786ebb29ca2",
    "measurementId": "G-W2SL219Z50",
}
firebase = pyrebase.initialize_app(firebaseConfig)


# main app class for kaki app with kivymd modules
class HealthBudd(MDApp, App):
    """Hi Windows users"""

    DEBUG = 1  # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "screens/login_screen/loginscreen.kv"),
        os.path.join(os.getcwd(), "screens/cadastro_screen/cadastro_screen.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "screens.screenmanager",
        "LoginScreen": "screens.login_screen.loginscreen",
        "CadastroScreen": "screens.cadastro_screen.cadastro_screen",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
        self.theme_cls.primary_palette = "Green"
        return Factory.MainScreenManager()

    def tema_light(self):
        self.theme_cls.theme_style = "Light"

    def tema_dark(self):
        self.theme_cls.theme_style = "Dark"


# finally, run the app
if __name__ == "__main__":
    HealthBudd().run()
