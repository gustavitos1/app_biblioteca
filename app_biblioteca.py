import flet as ft
from flet import *
import requests


def main(page: ft.Page):
    # Configuração de página
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    # inputs de usuario e admin
    input_nome = ft.TextField(label="Nome")
    input_senha = ft.TextField(label="Senha")
    input_codigo = ft.TextField(label="Código")
    input_email = ft.TextField(label="E-mail")

    # inputs de livro
    input_titulo = ft.TextField(label="Título")
    input_autor = ft.TextField(label="Autor")
    input_resumo = ft.TextField(label="Resumo")
    input_isbn = ft.TextField(label="ISBN")



    cadastro_usuario = ft.ElevatedButton(text="Cadastrar")
    cadastro_emprestimo = ft.ElevatedButton(text="Cadastrar")
    editar_usuario = ft.ElevatedButton(text="Editar")
    editar_livro = ft.ElevatedButton(text="Editar")
    editar_emprestimo = ft.ElevatedButton(text="Editar")

    # mensagens de erro e sucesso
    msg_sucesso = ft.SnackBar(
        content=ft.Text("Informações salvas com sucesso!"),
        bgcolor=Colors.GREEN,
    )
    msg_erro = ft.SnackBar(
        content=ft.Text("Preencha todos os campos!"),
        bgcolor=Colors.RED,
    )

    # funções de cadastro de livro
    cadastro_livro = ft.ElevatedButton(text="Cadastrar Livro", on_click=lambda _: page.go("/cadastro_livro"))
    def cadastrar_livro(e):
        url = "http://10.135.232.34:5000/cadastrar_livro"

        novo_livro = {
            "Titulo": input_titulo.value,
            "senha": input_autor.value,
            "Resumo": input_resumo.value,
            "ISBN": input_isbn.value
        }
        response = requests.post(url, json=novo_livro)
        if response.status_code == 201:
            page.overlay.append(msg_sucesso)
        else:
            page.overlay.append(msg_erro)

    realizar_cadastro_livro = ft.ElevatedButton(text="Cadastrar", on_click=cadastrar_livro)

    # funções de listar livro
    def listar_livros():
        url = f"http://10.135.232.34:5000/livros"
        livro_get = requests.get(url)

        if livro_get.status_code == 200:
            dados_get_postagem = livro_get.json()
            for livros in dados_get_postagem:
                print(f"titulo: {livros['Titulo']}")
                print(f"autor: {livros['Autor']}")
                print(f"resumo: {livros['Resumo']}")
                print(f"ISBN: {livros['ISBN']}")
                print("-" * 40)
        else:
            print(f'Erro: {livro_get.status_code}')

    lv_livros = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1
    )



    # cadastro de usuario base se não tiver cadastrado
    def cadastro():
        page.go("/cadastro")
    cadastrar = ft.Text(
        spans=[
            ft.TextSpan("NÃO É CADASTRADO, ", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
            ft.TextSpan(
                "CADASTRE-SE",
                style=ft.TextStyle(color="blue", weight=ft.FontWeight.BOLD),
                on_click=lambda _: cadastro()
            ),
        ]
    )
    botao_voltar = ft.ElevatedButton(text="Voltar", on_click=lambda _: page.go("/"))


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
                    Container(
                        input_nome,
                        alignment=ft.alignment.top_center,
                    ),
                    Container(
                        input_email,
                        alignment=ft.alignment.top_center,
                    ),
                    Container(
                        input_senha,
                        alignment=ft.alignment.top_center,
                    ),
                    ft.Text("é Funcionário? Insira seu código de administrador", color="yellow", weight=ft.FontWeight.BOLD),
                    Container(
                        input_codigo,
                        alignment=ft.alignment.top_center,
                        expand=True,
                    ),
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
                    cadastrar
                ],
            )
        )
        if page.route=="/cadastro":
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

        if page.route=="/cadastro_livro":
            page.views.append(
                View(
                    "/cadastro_livro",
                    [
                        AppBar(title=Text("Cadastro Livro"), bgcolor=Colors.PRIMARY_CONTAINER),
                        input_titulo,
                        input_autor,
                        input_resumo,
                        input_isbn,
                        realizar_cadastro_livro
                    ]
                )
            )

        if page.route=="/listar_livros":
            page.views.append(
                View(
                    "/listar_livros",
                    [
                        AppBar(title=Text("Lista de Livros"), bgcolor=Colors.PRIMARY_CONTAINER),

                    ]
                )
            )

        if page.route=="/opcoes":
            page.views.append(
                View(
                    "/opcoes",
                    [
                        AppBar(Image(src="free-user-icon-3296-thumb.png", ), title=Text("Perfil"), bgcolor=Colors.PRIMARY_CONTAINER),
                        ListTile(
                            leading=ft.Icon(Icons.VERIFIED_USER),
                            title=ft.Text(f"Nome: {input_nome.value}"),
                            subtitle=ft.Column(
                                [
                                    ft.Text(f"Email: {input_email.value}"),
                                    ft.Text(f"Senha: {input_senha.value}"),
                                    ft.Text(f"Código: {input_codigo.value}"),
                                ]
                            )
                        ),
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.ListTile(
                                            leading=ft.Icon(ft.Icons.BOOK),
                                            title=ft.Text("Livros"),
                                            subtitle=ft.Text(
                                                f"Livros arquivados:"
                                            ),
                                        ),
                                        ft.Row(
                                            [cadastro_livro, editar_livro],
                                            alignment=ft.MainAxisAlignment.END,
                                        ),
                                    ]
                                ),
                                width=400,
                                padding=10,
                            )
                        ),
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.ListTile(
                                            leading=ft.Icon(ft.Icons.PERSON),
                                            title=ft.Text("Usuários"),
                                            subtitle=ft.Text(
                                                f"Usuarios arquivados:"
                                            ),
                                        ),
                                        ft.Row(
                                            [cadastro_usuario, editar_usuario],
                                            alignment=ft.MainAxisAlignment.END,
                                        ),
                                    ]
                                ),
                                width=400,
                                padding=10,
                            )
                        ),
                        ft.Card(
                            content=ft.Container(
                                content=ft.Column(
                                    [
                                        ft.ListTile(
                                            leading=ft.Icon(ft.Icons.ARROW_UPWARD),
                                            title=ft.Text("Empréstimos"),
                                            subtitle=ft.Text(
                                                f"Empréstimos arquivados:"
                                            ),
                                        ),
                                        ft.Row(
                                            [cadastro_emprestimo, editar_emprestimo],
                                            alignment=ft.MainAxisAlignment.END,
                                        ),
                                    ]
                                ),
                                width=400,
                                padding=10,
                            )
                        ),
                        botao_voltar
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

