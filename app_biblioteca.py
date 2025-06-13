import flet as ft
from flet import *
import requests


def main(page: ft.Page):
    # Configuração de página
    page.title = "Exemplo de Rotas"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 700

    progress = ft.ProgressRing(visible=False)

    # inputs de usuario
    input_nome = ft.TextField(label="Nome")
    input_cpf = ft.TextField(label="CPF")
    input_codigo = ft.TextField(label="Código")
    input_email = ft.TextField(label="E-mail")

    input_cadastronome = ft.TextField(label="coloque seu nome")
    input_cadastroemail = ft.TextField(label="coloque seu email")
    input_cadastrosenha = ft.TextField(label="coloque sua senha")
    input_senha = ft.TextField(label="Senha")

    # inputs de livro
    input_titulo = ft.TextField(label="Título")
    input_autor = ft.TextField(label="Autor")
    input_resumo = ft.TextField(label="Resumo")
    input_isbn = ft.TextField(label="ISBN")

    listaview = ft.ListView(
        height=500,
        spacing=1,
        divider_thickness=1
    )

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
        progress.visible = True
        url = "http://10.135.232.34:5000/cadastrar_livro"

        novo_livro = {
            "titulo": input_titulo.value,
            "autor": input_autor.value,
            "resumo": input_resumo.value,
            "isbn": input_isbn.value
        }
        response = requests.post(url, json=novo_livro)
        if response.status_code == 201:
            # progress.visible = False
            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()
        else:
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()

    realizar_cadastro_livro = ft.ElevatedButton(text="Cadastrar", on_click=cadastrar_livro)

    def get_usuarios():
        url = "http://10.135.232.34:5000/usuarios"

        response = requests.get(url)
        if response.status_code == 200:
            print("Info Usuarios", response.json())
            return response.json()
        else:
            return response.json()

    def exibir_usuarios():
        usuarios = get_usuarios()
        listaview.controls.clear()
        for usuario in usuarios:
            listaview.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(f"Nome: {usuario['nome']}"),
                    subtitle=ft.Text(f"Email: {usuario['email']}"),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text=f"CPF: {usuario['cpf']}"),
                        ]
                    )
                )
            )

    def get_livros():
        url = "http://10.135.232.34:5000/livros"

        response = requests.get(url)
        if response.status_code == 200:
            print("Info Livros", response.json())
            return response.json()
        else:
            return response.json()


    def exibir_livro():
        livros = get_livros()
        listaview.controls.clear()
        for livro in livros:
            listaview.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.BOOK),
                    title=ft.Text(f"Livro: {livro['titulo']}"),
                    subtitle=ft.Text(f'Autor: {livro["autor"]}'),
                    trailing=ft.PopupMenuButton(
                        icon=ft.Icons.MORE_VERT,
                        items=[
                            ft.PopupMenuItem(text=f'resumo - {livro["resumo"]}'),
                            ft.PopupMenuItem(text=f'ISBN - {livro["isbn"]}'),
                        ]
                    ),
                )
            )
        page.update()


    # def editar_livro(e, id):
    #     url = f"http://10.135.232.34:5000/editar_livro/{id}"
    #
    #     nova_post = {
    #         "id": id,
    #         "titulo": input_titulo.value,
    #         "autor": input_autor.value,
    #         "resumo": input_resumo.value,
    #         "isbn": input_isbn.value
    #     }
    #     response_post = requests.put(url, json=nova_post)

    cadastro_usuario = ft.ElevatedButton(text="Cadastrar Usuario", on_click=lambda _: page.go("/cadastro_usuario"))
    def cadastrar_usuario(e):
        progress.visible = True
        url = "http://10.135.232.34:5000/cadastrar_usuario"

        novo_usuario = {
            "nome": input_nome.value,
            "cpf": input_cpf.value,
            "email": input_email.value,
        }
        response = requests.post(url, json=novo_usuario)
        if response.status_code == 201:

            page.overlay.append(msg_sucesso)
            msg_sucesso.open = True
            page.update()
        else:
            page.overlay.append(msg_erro)
            msg_erro.open = True
            page.update()

    realizar_cadastro_usuario = ft.ElevatedButton(text="Cadastrar", on_click=cadastrar_usuario)

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
                        input_cadastronome,
                        alignment=ft.alignment.top_center,
                    ),
                    Container(
                        input_cadastroemail,
                        alignment=ft.alignment.top_center,
                    ),
                    Container(
                        input_cadastrosenha,
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
        listar_usuarios_botao = ft.ElevatedButton(text="listar_usuarios",
                                                  on_click=lambda _: page.go("/listar_usuarios"))
        if page.route=="/cadastro":
            page.views.append(
                View(
                    "/cadastro",
                    [
                        AppBar(title=Text("Cadastrar"), bgcolor=Colors.PRIMARY_CONTAINER),
                        input_nome,
                        input_email,
                        input_senha,
                        ElevatedButton(text="Cadastrar", bgcolor=Colors.BLUE_ACCENT_100, color=Colors.BLACK),
                    ]
                )
            )
        if page.route=="/detalhes":
            page.views.append(
                View(
                    "/detalhes",
                    [
                        AppBar(title=Text("Detalhes"), bgcolor=Colors.PURPLE),
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
                        realizar_cadastro_livro,
                        ft.ElevatedButton(
                            text="lista",
                            on_click=lambda _: page.go("/listar_livros"),
                        ),
                    ]
                )
            )
        if page.route=="/cadastro_usuario":
            page.views.append(
                View(
                    "/cadastro_usuario",
                    [
                        AppBar(title=Text("Cadastro Livro"), bgcolor=Colors.PRIMARY_CONTAINER),
                        input_nome,
                        input_cpf,
                        input_email,
                        realizar_cadastro_usuario,
                        listar_usuarios_botao,

                    ]
                )
            )
        if page.route=="/listar_usuarios":
            exibir_usuarios()
            page.views.append(
                View(
                    "/listar_usuarios",
                    [
                        AppBar(title=Text("Listar Usuarios"), bgcolor=Colors.PRIMARY_CONTAINER),
                        listaview
                    ]
                )
            )
        elif page.route == "/listar_livros":
            exibir_livro()
            page.views.append(
                View(
                    "/listar_livro",
                    [
                        AppBar(title=Text("Listar"), bgcolor=Colors.PRIMARY_CONTAINER),
                        listaview
                    ]
                )
            )
        if page.route=="/editar_livro":
            page.views.append(

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
                                                f"Livros arquivados: {len(get_livros())}"
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
                                                f"Usuarios arquivados: {len(get_usuarios())}"
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

