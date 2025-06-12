import requests

def livros_get():
    url = f"http://10.135.232.34:5000/livros"
    livro_get = requests.get(url)

    if livro_get.status_code == 200:
        dados_get_postagem = livro_get.json()
        for livros in dados_get_postagem:
            print(f"titulo: {livros['titulo']}")
            print(f"autor: {livros['autor']}")
            print(f"resumo: {livros['resumo']}")
            print(f"isbn: {livros['isbn']}")
            print("-" * 40)
            print(livros)

    else:
        print(f'Erro: {livro_get.status_code}')

def livros_post():
    url = "http://10.135.232.34:5000/cadastrar_livro"

    nova_post = {
        "titulo": "first title",
        "autor": "Post Body",
        "resumo": "batmam, o cavaleiro das trevas, ataca coringa",
        "isbn": "01234567200"
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
        "titulo": "new title",
        "autor": "novo body",
        "resumo": "batmam",
        "isbn": "01234567201"
    }

    response_post = requests.put(url, json=nova_post)

    if response_post.status_code == 200:
        dados_post = response_post.json()
        print(f"titulo: {dados_post['mensagem']}\n")
    else:
        print(f'Erro: {response_post.status_code}')
        # print(response_post.json())

def usuarios_get():
    url = f"http://10.135.232.34:5000/usuarios"

    usuarios_get = requests.get(url)
    if usuarios_get.status_code == 200:
        dados_get_postagem = usuarios_get.json()
        for usuarios in dados_get_postagem:
            print(usuarios)
    else:
        print(f'Erro: {usuarios_get.status_code}')

def usuarios_post():
    url = "http://10.135.232.34:5000/cadastrar_usuario"

    nova_post = {
        "nome": "maurição",
        "cpf": "34265663",
        "email": "jajaja@gmail.com",
    }

    response_post = requests.post(url, json=nova_post)
    if response_post.status_code == 201:
        dados_post = response_post.json()
        print(dados_post)
        print(dados_post["mensagem"])
    else:
        print(f'Erro: {response_post.status_code}')
        print(f'Erro: {response_post.json()}')


def usuarios_put(id):
    url = f"http://10.135.232.34:5000/editar_usuario/{id}"

    nova_post = {
        "id": id,
        "nome": "renato cariani",
        "cpf": "34265993",
        "email": "sasasasa@gmail.com",
    }

    response_post = requests.put(url, json=nova_post)
    if response_post.status_code == 200:
        dados_post = response_post.json()
        print(f"nome: {dados_post['mensagem']}\n")
    else:
        print(f'Erro: {response_post.status_code}')

def emprestimos_get():
    url = f"http://10.135.232.34:5000/emprestimos"

    emprestimos_get = requests.get(url)
    if emprestimos_get.status_code == 200:
        dados_get_postagem = emprestimos_get.json()
        for emprestimos in dados_get_postagem:
            print(emprestimos)
    else:
        print(f'Erro: {emprestimos_get.status_code}')

def emprestimos_post():
    url = "http://10.135.232.34:5000/cadastrar_emprestimo"

    nova_post = {
        "data_emprestimo": "12-05-2025",
        "data_devolucao": "29-05-2025",
        "id_usuario": "1",
        "id_livro": "1",
    }

    response_post = requests.post(url, json=nova_post)
    if response_post.status_code == 200:
        dados_post = response_post.json()
        print(dados_post)
        print(dados_post["mensagem"])
    else:
        print(f'Erro: {response_post.status_code}')
        print(f'Erro: {response_post.json()}')

def emprestimos_put(id):
    url = f"http://10.135.232.34:5000/editar_emprestimo/{id}"

    nova_post = {
        "data_emprestimo": "12-05-2025",
        "data_devolucao": "29-05-2025",
        "id_usuario": "1",
        "id_livro": "1",
    }

    response_post = requests.put(url, json=nova_post)
    if response_post.status_code == 200:
        dados_post = response_post.json()
        print(f"data_emprestimo: {dados_post['mensagem']}\n")
    else:
        print(f'Erro: {response_post.status_code}')

livros_post()
