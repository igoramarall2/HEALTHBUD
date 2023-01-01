from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kaki.app import App
import pyrebase
from main import firebaseConfig
from kivy.uix.screenmanager import FadeTransition

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()


class LoginScreen(MDScreen):
    def sign_up(self):
        email = self.manager.ids.login.ids.email.text
        password = self.manager.ids.login.ids.senha.text
        auth.create_user_with_email_and_password(email, password)

    def sign_in(self):
        email = self.manager.ids.login.ids.email.text
        password = self.manager.ids.login.ids.senha.text
        auth.sign_in_with_email_and_password(email, password)
        self.manager.current = "CadastroScreen"
