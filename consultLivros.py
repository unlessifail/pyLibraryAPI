import requests
import json
import customtkinter as ctk

appLivroConsult = ctk.CTk()

appLivroConsult.title('Consultar Livros')
appLivroConsult.resizable(False, False)
appLivroConsult.geometry("800x400")

# Funções

def on_pesquisar_btn_click():
    id_pesquisa = idEntry.get()
    titulo_pesquisa = tituloEntry.get()

    # Lógica para pesquisar os dados com base no ID ou título
    if id_pesquisa:
        url = f"http://localhost:5000/livros/{id_pesquisa}"
    elif titulo_pesquisa:
        url = f"http://localhost:5000/livros?titulo={titulo_pesquisa}"
    else:
        # Caso não seja fornecido ID nem título, não faz a pesquisa
        return

    response = requests.get(url)

    if response.status_code == 200:
        livro = response.json()
        # Atualizar labels com os dados obtidos
        labelID.configure(text=f"ID: {livro['id']}")
        labelAutor.configure(text=f"{livro['autor']}")
        labelTituloPlaceholder.configure(text=f"{livro['titulo']}")
        labelAnoPlaceholder.configure(text=f"{livro['ano']}")
        labelEditoraPlaceholder.configure(text=f"{livro['editora']}")
    else:
        # Exibir mensagem de erro ou limpar labels
        labelID.configure(text="ID")
        labelAutor.configure(text="Autor")
        labelTituloPlaceholder.configure(text="Título")
        labelAnoPlaceholder.configure(text="Ano")
        labelEditoraPlaceholder.configure(text="Editora")

def atualizar_livro(id, campo, novo_valor):
    url = f"http://localhost:5000/livros/{id}"
    novo_dado = {campo: novo_valor}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(url, data=json.dumps(novo_dado), headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False
    
def on_btn_autor_update_click():
    novo_valor = entryAutor.get()
    if novo_valor:
        id_livro = labelID.cget("text").split(":")[1].strip()
        if atualizar_livro(id_livro, "autor", novo_valor):
            labelAutor.configure(text=f"{novo_valor}")
        else:
            print("Erro ao atualizar o Autor.")

def on_btn_titulo_update_click():
    novo_valor = entryTitulo.get()
    if novo_valor:
        id_livro = labelID.cget("text").split(":")[1].strip()
        if atualizar_livro(id_livro, "titulo", novo_valor):
            labelTituloPlaceholder.configure(text=f"{novo_valor}")
        else:
            print("Erro ao atualizar o Título.")

def on_btn_ano_update_click():
    novo_valor = entryAno.get()
    if novo_valor:
        id_livro = labelID.cget("text").split(":")[1].strip()
        if atualizar_livro(id_livro, "ano", novo_valor):
            labelAnoPlaceholder.configure(text=f"{novo_valor}")
        else:
            print("Erro ao atualizar o Ano.")

def on_btn_editora_update_click():
    novo_valor = entryEditora.get()
    if novo_valor:
        id_livro = labelID.cget("text").split(":")[1].strip()
        if atualizar_livro(id_livro, "editora", novo_valor):
            labelEditoraPlaceholder.configure(text=f"{novo_valor}")
        else:
            print("Erro ao atualizar a Editora.")

# Frames

frameBackground = ctk.CTkFrame(appLivroConsult,
                               width=800,
                               height=400,
                               bg_color="#ECC8F9",
                               fg_color="#ECC8F9",
                               )

frameBackground.place(x=0,y=0)

framePlaceholder = ctk.CTkFrame(appLivroConsult,
                               width=380,
                               height=300,
                               bg_color="#ECC8F9",
                               fg_color="#D28CEA",
                               )

framePlaceholder.place(x=391,y=60)

# Labels

headerLabel = ctk.CTkLabel(appLivroConsult,
                           text="Consultar Livros",
                           font=("Arial Italic", 30),
                           text_color="#CC66EE",
                           bg_color="#ECC8F9",
                           )

headerLabel.place(x=90,y=84)

idEntryLabel = ctk.CTkLabel(appLivroConsult,
                           text="ID:",
                           font=("Arial Italic", 20),
                           text_color="#CC66EE",
                           bg_color="#ECC8F9",
                           )

idEntryLabel.place(x=60,y=155)

tituloEntryLabel = ctk.CTkLabel(appLivroConsult,
                           text="Titulo:",
                           font=("Arial Italic", 20),
                           text_color="#CC66EE",
                           bg_color="#ECC8F9",
                           )

tituloEntryLabel.place(x=60,y=230)

altEntryLabel = ctk.CTkLabel(appLivroConsult,
                           text="OU PESQUISAR POR:",
                           font=("Arial Italic", 20),
                           text_color="#CC66EE",
                           bg_color="#ECC8F9",
                           )

altEntryLabel.place(x=60,y=195)

# Entrys

idEntry = ctk.CTkEntry(appLivroConsult,
                       width=251,
                       height=25,
                       border_color="#CC66EE",
                       border_width=1,
                       bg_color="#ECC8F9",
                       fg_color="#D28CEA",
                       corner_radius=30,
                       )

idEntry.place(x=99,y=158)

tituloEntry = ctk.CTkEntry(appLivroConsult,
                       width=192,
                       height=25,
                       border_color="#CC66EE",
                       border_width=1,
                       bg_color="#ECC8F9",
                       fg_color="#D28CEA",
                       corner_radius=30,
                       )

tituloEntry.place(x=158,y=232)

# Btn

pesquisarBtn = ctk.CTkButton(appLivroConsult,
                          text="Pesquisar",
                          font=("Arial Bold", 30),
                          text_color="#FFFFFF",
                          width=290,
                          height=60,
                          bg_color="#ECC8F9",
                          fg_color="#D080EB",
                          border_color="#8000AD",
                          border_width=1,
                          corner_radius=30,
                          hover_color="#CC79EA",
                          command=on_pesquisar_btn_click,
                          )

pesquisarBtn.place(x=60,y=285)

# Labels

labelID = ctk.CTkLabel(appLivroConsult,
                       text="ID",
                       text_color="#ECC8F9",
                       bg_color="#D28CEA",
                       font=("Arial Bold", 20),
                       )

labelID.place(x=411,y=123)

labelAutor = ctk.CTkLabel(appLivroConsult,
                       text="Autor",
                       text_color="#ECC8F9",
                       bg_color="#D28CEA",
                       font=("Arial Bold", 20),
                       )

labelAutor.place(x=411,y=157)

labelTituloPlaceholder = ctk.CTkLabel(appLivroConsult,
                       text="Titulo",
                       text_color="#ECC8F9",
                       bg_color="#D28CEA",
                       font=("Arial Bold", 20),
                       )

labelTituloPlaceholder.place(x=411,y=189)

labelAnoPlaceholder = ctk.CTkLabel(appLivroConsult,
                       text="Ano",
                       text_color="#ECC8F9",
                       bg_color="#D28CEA",
                       font=("Arial Bold", 20),
                       )
labelAnoPlaceholder.place(x=411,y=221)

labelEditoraPlaceholder = ctk.CTkLabel(appLivroConsult,
                       text="Editora",
                       text_color="#ECC8F9",
                       bg_color="#D28CEA",
                       font=("Arial Bold", 20),
                       )
labelEditoraPlaceholder.place(x=411,y=252)

# Entry para atualizar dados

entryAutor = ctk.CTkEntry(appLivroConsult,
                       width=75,
                       height=25,
                       border_width=0,
                       bg_color="#D28CEA",
                       fg_color="#ECC8F9",
                       corner_radius=0,
                       )

entryAutor.place(x=632,y=162)

btnAutorUpdate = ctk.CTkButton(appLivroConsult,
                       width=45,
                       height=25,
                       border_width=0,
                       bg_color="#D28CEA",
                       fg_color="#CC66EE",
                       corner_radius=0,
                       text="Atualizar",
                       hover="#BF00FF",
                       command=on_btn_autor_update_click
                       )

btnAutorUpdate.place(x=707,y=162)

entryTitulo = ctk.CTkEntry(appLivroConsult,
                       width=75,
                       height=25,
                       border_width=0,
                       bg_color="#D28CEA",
                       fg_color="#ECC8F9",
                       corner_radius=0,
                       )

entryTitulo.place(x=632,y=192)

btnTituloUpdate = ctk.CTkButton(appLivroConsult,
                       width=45,
                       height=25,
                       border_width=0,
                       bg_color="#D28CEA",
                       fg_color="#CC66EE",
                       corner_radius=0,
                       text="Atualizar",
                       hover="#BF00FF",
                       command=on_btn_titulo_update_click,
                       )

btnTituloUpdate.place(x=707,y=192)

entryAno = ctk.CTkEntry(appLivroConsult,
                       width=75,
                       height=25,
                       border_width=0,
                       bg_color="#D28CEA",
                       fg_color="#ECC8F9",
                       corner_radius=0,
                       )

entryAno.place(x=632,y=222)

btnAnoUpdate = ctk.CTkButton(appLivroConsult,
                       width=45,
                       height=25,
                       border_width=0,
                       bg_color="#D28CEA",
                       fg_color="#CC66EE",
                       corner_radius=0,
                       text="Atualizar",
                       hover="#BF00FF",
                       command=on_btn_ano_update_click,
                       )

btnAnoUpdate.place(x=707,y=222)

entryEditora = ctk.CTkEntry(appLivroConsult,
                       width=75,
                       height=25,
                       border_width=0,
                       bg_color="#D28CEA",
                       fg_color="#ECC8F9",
                       corner_radius=0,
                       )

entryEditora.place(x=632,y=252)

btnEditoraUpdate = ctk.CTkButton(appLivroConsult,
                       width=45,
                       height=25,
                       border_width=0,
                       bg_color="#D28CEA",
                       fg_color="#CC66EE",
                       corner_radius=0,
                       text="Atualizar",
                       hover="#BF00FF",
                       command=on_btn_editora_update_click
                       )

btnEditoraUpdate.place(x=707,y=252)

appLivroConsult.mainloop()