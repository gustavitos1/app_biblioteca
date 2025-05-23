import flet as ft
from flet import *


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

    cadastro_livro = ft.ElevatedButton(text="Cadastro Livro", icon="book")
    editar_livro = ft.ElevatedButton(text="Editar Livro", icon="book")
    deletar_livro = ft.ElevatedButton(text="Deletar Livro", icon="book")

    msg_sucesso = ft.SnackBar(
        content=ft.Text("Informações salvas com sucesso!"),
        bgcolor=Colors.GREEN,
    )
    msg_erro = ft.SnackBar(
        content=ft.Text("Preencha todos os campos!"),
        bgcolor=Colors.RED,
    )


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
                        input_senha,
                        alignment=ft.alignment.top_center,
                    ),
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

        if page.route=="/opcoes":
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

