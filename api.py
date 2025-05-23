import requests

def livros_get():
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

def livros_post():
    url = "http://10.135.232.34:5000/cadastrar_livro"

    nova_post = {
        "Titulo": "first title",
        "Autor": "Post Body",
        "Resumo": "batmam, o cavaleiro das trevas, ataca coringa",
        "ISBN": "01234567200"
    }

    response_post = requests.post(url, json=nova_post)

    if response_post.status_code == 201:
        dados_post = response_post.json()
        print(dados_post)
        print(dados_post["mensagem"])

    else:
        print(f'Erro: {response_post.status_code}')
        print(f'Erro: {response_post.json()}')


#     exemplo_post()

def livros_put(id):
    url = f"http://10.135.232.34:5000/editar_livro/{id}"

    nova_post = {
        "id": id,
        "Titulo": "new title",
        "Autor": "novo body",
        "Resumo": "batmam",
        "ISBN": "01234567201"
    }

    response_post = requests.put(url, json=nova_post)

    if response_post.status_code == 200:
        dados_post = response_post.json()
        print(f"Titulo: {dados_post['mensagem']}\n")
    else:
        print(f'Erro: {response_post.status_code}')
        # print(response_post.json())


livros_put(1)
