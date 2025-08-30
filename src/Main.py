import tkinter as tk
from tkinter import ttk
import pyodbc as pdb
import pandas as pd
import Functions as fc

conexao = fc.conectar()


# Função que busca em uma coluna específica(CustomerID) de uma tabela específica(SalesLT.Customer) as informações baseadas na que o usuário inseriu no campo de texto
def consulta(pesq):
    try:
        df = fc.pesquisa(informacao2, pesq, conexao)
    

        # Limpar o Treeview
        tree.delete(*tree.get_children())
        tree['columns'] = list(df.columns) # Define as colunas do DF
        tree['show'] = 'headings' # Mostra só os nomes das colunas

        # Definir colunas
        for col in df.columns:
            tree.heading(col, text=col) # Nome da coluna
            tree.column(col, width=120, anchor='w') # Largura e alinhamento
       


        # Inserir linhas
        for _, row in df.iterrows():
            tree.insert("", "end", values=list(row))
    except Exception as e:
        print(f"Erro: {e}")


# Janela principal
janela = tk.Tk()
janela.title("Minha interface gráfica")
janela.geometry("400x300")
janela.config(background="purple")

# Rótulo
label_instrução = tk.Label(janela, text="Olá Mundo!")
label_instrução.pack(pady=10)
label_instrução.configure(background="purple")



# Caixa de texto
informacao2 = tk.Entry(janela, width=30)
informacao2.pack(pady=10)


# Funções para mostrar o DataFrame
tree = ttk.Treeview(janela)
tree.pack(fill='both', expand='true')

# Scroll vertical
scrollbar = tk.Scrollbar(janela, orient='horizontal', command=tree.xview)
tree.configure(xscroll=scrollbar.set)
scrollbar.pack(side="bottom", fill="x")

frame_botoes = tk.Frame(janela, bg='Purple')
frame_botoes.pack(pady=10)


# Botão que busca pela coluna "FirstName"
botao1 = tk.Button(frame_botoes, text="NOME", command=lambda: (consulta("NOME")))
botao1.pack(side='left', padx=10)

# Botão que busca pela coluna "CustomerID"
botao2 = tk.Button(frame_botoes, text="ID", command=lambda:(consulta("ID")))
botao2.pack(side='left', padx=10)

# Executar janela
janela.mainloop()