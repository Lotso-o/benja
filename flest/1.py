import flet as ft

class App :
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "hola mundo"

        self.build()

    def build(self):
        self.page.add(
            ft.Text("hola mundo")
        )

if __name__ == "__main__":
    ft.app(target=App)

