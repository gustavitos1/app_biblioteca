import flet as ft
import requests  # Certifique-se de que a biblioteca requests está instalada
from flet import *

API_URL = "http://sua-api.com/livros"  # Substitua pela URL da sua API

def main(page: ft.Page):
    # Configuração de página
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    input_nome = ft.TextField(label="Nome")
    input_senha = ft.TextField(label="Senha")
    input_codigo = ft.TextField(label="Código")
    input_email = ft.TextField(label="E-mail")
    input_isbn = ft.TextField(label="ISBN")  # Campo para ISBN

    cadastro_livro = ft.ElevatedButton(text="Cadastro Livro", icon="book", on_click=lambda _: cadastrar_livro())
    editar_livro = ft.ElevatedButton(text="Editar Livro", icon="book", on_click=lambda _: editar_livro())
    deletar_livro = ft.ElevatedButton(text="Deletar Livro", icon="book", on_click=lambda _: deletar_livro())

    msg_sucesso = ft.SnackBar(
        content=ft.Text("Informações salvas com sucesso!"),
        bgcolor=Colors.GREEN,
    )
    msg_erro = ft.SnackBar(
        content=ft.Text("Preencha todos os campos!"),
        bgcolor=Colors.RED,
    )

    def cadastrar_livro():
        # Coleta os dados do livro
        livro_data = {
            "nome": input_nome.value,
            "senha": input_senha.value,
            "codigo": input_codigo.value,
            "email": input_email.value,
            "isbn": input_isbn.value
        }
        response = requests.post(API_URL, json=livro_data)
        if response.status_code == 201:
            page.show_snack(msg_sucesso)
        else:
            page.show_snack(msg_erro)

    def editar_livro():
        # Coleta os dados do livro
        livro_data = {
            "nome": input_nome.value,
            "senha": input_senha.value,
            "codigo": input_codigo.value,
            "email": input_email.value
        }
        response = requests.put(f"{API_URL}/{input_isbn.value}", json=livro_data)
        if response.status_code == 200:
            page.show_snack(msg_sucesso)
        else:
            page.show_snack(msg_erro)

    def deletar_livro():
        response = requests.delete(f"{API_URL}/{input_isbn.value}")
        if response.status_code == 204:
            page.show_snack(msg_sucesso)
        else:
            page.show_snack(msg_erro)

    def gerencia_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/",
                [
                    Container(
                        ft.Icon(name="PERSON_PIN_SHARP", size=100),
                        alignment=ft.alignment.top_center,
                        expand=True,
                    ),
                    Container(input_nome, alignment=ft.alignment.top_center),
                    Container(input_senha, alignment=ft.alignment.top_center),
                    Container(input_codigo, alignment=ft.alignment.top_center, expand=True),
                    Container(input_isbn, alignment=ft.alignment.top_center, expand=True),  # Campo ISBN
                    Container(
                        ElevatedButton(
                            text="Entrar",
                            bgcolor=Colors.BLUE_ACCENT_100,
                            color=Colors.BLACK,
                            on_click=lambda _: page.go("/opcoes")
                        ),
                        alignment=ft.alignment.top_center,
                        expand=True
                    ),
                    cadastrar_livro,
                    editar_livro,
                    deletar_livro
                ],
            )
        )
        if page.route == "/cadastro":
            page.views.append(
                View(
                    "/cadastro",
                    [
                        AppBar(title=Text("Cadastrar"), bgcolor=Colors.PRIMARY_CONTAINER),
                        input_nome,
                        input_email,
                        input_senha,
                        ElevatedButton(text="Cadastrar", bgcolor=Colors.BLUE_ACCENT_100, color=Colors.BLACK)
                    ]
                )
            )

        if page.route == "/opcoes":
            page.views.append(
                View(
                    "/opcoes",
                    [
                        AppBar(Image(src="free-user-icon-3296-thumb.png"), title=Text("Perfil"), bgcolor=Colors.PRIMARY_CONTAINER),
                        ListTile(
                            leading=ft.Icon(Icons.VERIFIED_USER),
                            title=ft.Text(f"Nome: {input_nome.value}"),
                            subtitle=ft.Column(
                                [
                                    ft.Text(f"Senha: {input_senha.value}"),
                                    ft.Text(f"Código: {input_codigo.value}"),
                                ]
                            )
                        ),
                        cadastro_livro
                    ]
                )
            )

        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = gerencia_rotas
    page.on_view_pop = voltar
    page.go(page.route)

ft.app(main)
