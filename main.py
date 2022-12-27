import os
from kivy import Config

Config.set("graphics", "width", "960")
Config.set("graphics", "height", "720")
Config.set("graphics", "minimum_width", "960")
Config.set("graphics", "minimum_height", "720")
from kivymd.app import MDApp
from kaki.app import App
from kivy.factory import Factory

# main app class for kaki app with kivymd modules
class LiveApp(MDApp, App):
    """Hi Windows users"""

    DEBUG = 1  # set this to 0 make live app not working

    # *.kv files to watch
    KV_FILES = {
        os.path.join(os.getcwd(), "screens/screenmanager.kv"),
        os.path.join(os.getcwd(), "screens/login_screen/loginscreen.kv"),
    }

    # class to watch from *.py files
    CLASSES = {
        "MainScreenManager": "screens.screenmanager",
        "LoginScreen": "screens.login_screen.loginscreen",
    }

    # auto reload path
    AUTORELOADER_PATHS = [
        (".", {"recursive": True}),
    ]

    def build_app(self):
        self.theme_cls.primary_palette = "Green"
        return Factory.MainScreenManager()


# finally, run the app
if __name__ == "__main__":
    LiveApp().run()
