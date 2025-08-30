import pyodbc as pydb
import pandas as pd


def conectar():
    return pydb.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost;'
        'DATABASE=AdventureWorksLT2022;'
        "Trusted_Connection=yes;"
    )

def bpc(informacao, conexao):
    p_query = informacao.get()
    s_query = f"SELECT * FROM SalesLT.Customer WHERE FirstName = '{p_query}'"
    df = pd.read_sql_query(s_query, conexao)
    return df


def bpID(informacao, conexao):
    p_query = int(informacao.get())
    s_query = f"SELECT * FROM SalesLT.Customer WHERE CustomerID = {p_query}"
    df = pd.read_sql_query(s_query, conexao)
    return df

def pesquisa(x1, pesq, conexao):
    if pesq == "ID":
        return bpID(x1, conexao)
    elif pesq == 'NOME':
        return bpc(x1, conexao)
    else:
        print('Erro de piroca')