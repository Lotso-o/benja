from ecotech import Auth , Database , Finance 
from dotenv import load_dotenv
import flet as ft
import os


class App :

    def __init__(self,page : ft.Page):
        self.page = page
        self.page.title =""
        self.db =Database(
            username=os.getenv("oracle_user"),
            password=os.getenv("oracle_pasword"),
            dsn=os.getenv("oracle_dsn"),
        )
        pass

    def page_register(self):
        self.page.controls.clear()

        


        self.page.update()

    def page_login(self):
        self.page.controls.clear()
        self.page.update()
    
    def page_main_menu(self):
        self.page.controls.clear()
        self.page.update()
    
    def page_indicador_menu(self):
        self.page.controls.clear()
        self.page.update()

    def page_history_menu(self):
        self.page.controls.clear()
        self.page.update()

    
    