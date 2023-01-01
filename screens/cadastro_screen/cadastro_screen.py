from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDatePicker
import pyrebase
from main import firebaseConfig

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()


class CadastroScreen(MDScreen):
    def on_save(self, instance, value, date_range):
        """
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;
        :param value: selected date;
        :type value: <class 'datetime.date'>;
        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        """
        print(value)

    def on_cancel(self, instance, value):
        pass

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def Entrada_de_Dados(self):
        nome = self.manager.ids.cadastroscreen.ids.nome.text
        sobrenome = self.manager.ids.cadastroscreen.ids.sobrenome.text
        idade = self.manager.ids.cadastroscreen.ids.idade.text
        email = self.manager.ids.cadastroscreen.ids.email.text
        celular = self.manager.ids.cadastroscreen.ids.celular.text

        data = {
            "nome": nome,
            "sobrenome": sobrenome,
            "idade": idade,
            "email": email,
            "celular": celular,
        }
        db.push(data)
        print(data)
