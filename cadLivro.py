import requests
import json
import customtkinter as ctk

appCadLivro = ctk.CTk()

appCadLivro.title('Cadastrar Livros')
appCadLivro.resizable(False, False)
appCadLivro.geometry("375x387")

# Funções

def obter_todos_livros():
    url = "http://localhost:5000/livros"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def enviar_novo_livro(titulo, autor, editora, ano):
    url = "http://localhost:5000/livros"
    novo_livro = {
        'titulo': titulo,
        'autor': autor,
        'editora': editora,
        'ano': ano
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(novo_livro), headers=headers)
    if response.status_code == 201:
        return response.json()['livro']
    else:
        return None
    
def on_btnEnviar_click():
    # Obter dados da interface gráfica
    titulo = tituloEntry.get()
    autor = autorEntry.get()
    editora = editoraEntry.get()
    ano = anoEntry.get()

    # Enviar novo livro para a API
    novo_livro = enviar_novo_livro(titulo, autor, editora, ano)

    if novo_livro:
        # Atualizar interface gráfica ou exibir mensagem de sucesso
        print("Livro adicionado com sucesso:", novo_livro)
    else:
        # Exibir mensagem de erro
        print("Erro ao adicionar livro")

lista_livros = obter_todos_livros()

# Frames

frameBG = ctk.CTkFrame(appCadLivro,
                       width=375,
                       height=387,
                       bg_color="#EFD8F6",
                       fg_color="#EFD8F6",
                       )
frameBG.place(x=0,y=0)

frameHeader = ctk.CTkFrame(appCadLivro,
                       width=375,
                       height=58,
                       bg_color="#CC66EE",
                       fg_color="#CC66EE",
                       corner_radius=0,
                       )
frameHeader.place(x=0,y=0)

# Labels

labelHeader = ctk.CTkLabel(appCadLivro,
                           text="Cadastro de Livros",
                           text_color="#FFFFFF",
                           font=("Arial Bold", 30),
                           bg_color="#CC66EE",
                           )

labelHeader.place(x=60,y=13)

labelTitulo = ctk.CTkLabel(appCadLivro,
                           text="Título:",
                           text_color="#8000AD",
                           font=("Arial Bold", 15),
                           bg_color="#EFD8F6",
                           )

labelTitulo.place(x=30,y=77)

labelAutor = ctk.CTkLabel(appCadLivro,
                           text="Autor:",
                           text_color="#8000AD",
                           font=("Arial Bold", 15),
                           bg_color="#EFD8F6",
                           )

labelAutor.place(x=30,y=140)

labelEditora = ctk.CTkLabel(appCadLivro,
                           text="Editora:",
                           text_color="#8000AD",
                           font=("Arial Bold", 15),
                           bg_color="#EFD8F6",
                           )

labelEditora.place(x=30,y=201)

labelAno = ctk.CTkLabel(appCadLivro,
                           text="Ano:",
                           text_color="#8000AD",
                           font=("Arial Bold", 15),
                           bg_color="#EFD8F6",
                           )

labelAno.place(x=30,y=262)

# Entrys

tituloEntry = ctk.CTkEntry(appCadLivro,
                           width=244,
                           height=37,
                           placeholder_text_color="#FFFFFF",
                           bg_color="#EFD8F6",
                           border_color="#8000AD",
                           fg_color="#E3ADF5",
                           corner_radius=15,
                           )

tituloEntry.place(x=101,y=72)

autorEntry = ctk.CTkEntry(appCadLivro,
                           width=244,
                           height=37,
                           placeholder_text_color="#FFFFFF",
                           bg_color="#EFD8F6",
                           border_color="#8000AD",
                           fg_color="#E3ADF5",
                           corner_radius=15,
                           )

autorEntry.place(x=101,y=133)

editoraEntry = ctk.CTkEntry(appCadLivro,
                           width=244,
                           height=37,
                           placeholder_text_color="#FFFFFF",
                           bg_color="#EFD8F6",
                           border_color="#8000AD",
                           fg_color="#E3ADF5",
                           corner_radius=15,
                           )

editoraEntry.place(x=101,y=193)

anoEntry = ctk.CTkEntry(appCadLivro,
                           width=244,
                           height=37,
                           placeholder_text_color="#FFFFFF",
                           bg_color="#EFD8F6",
                           border_color="#8000AD",
                           fg_color="#E3ADF5",
                           corner_radius=15,
                           )

anoEntry.place(x=101,y=254)

# Button

btnEnviar = ctk.CTkButton(appCadLivro,
                          text="Enviar",
                          text_color="#8000AD",
                          width=315,
                          height=53,
                          bg_color="#EFD8F6",
                          fg_color="#D080EB",
                          border_color="#8000AD",
                          border_width=1,
                          corner_radius=30,
                          hover_color="#CC79EA",
                          command=on_btnEnviar_click
                          )

btnEnviar.place(x=30,y=315)

appCadLivro.mainloop()
