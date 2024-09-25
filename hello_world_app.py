import flet as ft
# NOTE: Estrutura padrão
def main(page: ft.page):
    page.title = "Olá Mundo!"
    page.scroll = "adaptive"

# declaracao de variavais
    nome = ft.TextField(label="Nome:") # NOTE: campo de escrita

    page.add(
        ft.Text("Olá, Mundo", size=30, font_family="Arial", color="blue", weight="bold", ),
        nome,
        ft.TextButton("Clique aqui")
    )
    page.update() # NOTE: return

ft.app(main)

