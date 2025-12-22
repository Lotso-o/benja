import flet as ft

class App:
    def __init__(self, page: ft.Page):
        self.page =page 
        self.page.title = "hola mundo"
        
        self.input_nombre = ft.TextField(hint_text="ingrese tu nombre ")
        self.button_saludar = ft.Button(text="saludar", on_click=self.handle_saludo)
        self.text_saludo = ft.Text(value="")

    def build(self):
        self.page.add(
            self.input_nombre,
            self.button_saludar,
            self.text_saludo
        )
        self.page.update()

    def handle_saludo(self,e):
        nombre = (self.input_nombre.value or "").estrip()
        if nombre:
            self.text_saludo.value = f"hola ,{nombre}"
        else:
            self.text_saludo.value = "ingrese un nombre"
        self.page.update()


if __name__ == "__main__":
    ft.app(target=App)
 



