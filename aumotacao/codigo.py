# Passo a passo do projeto

# Passo 1 - Entrar no sistema da empresa 
        # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Importando as bibliotecas 

import pyautogui as py
import time

# clicar -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey(clrl + v)
# texto com aspas precisa colocar uma \ antes das aspas

py.PAUSE = 5                # Comando para uma pausa entre todos os comandos

py.press('win')             # Comando para pressiona o botão windows

py.write('chrome')          # Comando para digitar a palavra chrome

py.press('enter')           # Comando para pressionar o botão enter

link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'

py.write(link)              # Comando para escrever o link salvo na variavel

py.press('enter')
# Uma pausa de 5 segundo para carregar a página
time.sleep(5)

# Passo 2 - Fazer o login
py.click(x=321, y=543)

py.write('pythonimpressionador@gmail.com')

py.press('tab')

py.write('minhasenha')

py.press('tab')

py.press('enter')

time.sleep(5)

# Passo 3 - Importar a base de dados
import pandas as pd
import numpy as np
import openpyxl as op

produtos = pd.read_csv('produtos.csv')

for linha in produtos.index:
      
    # Passo 4 - Cadastrar um produto

    py.click(x=657, y=578)

    codigo = produtos.loc[linha, 'codigo']
    marca = produtos.loc[linha, 'marca']
    tipo = produtos.loc[linha, 'tipo']
    categoria = produtos.loc[linha, 'categoria']
    preco = produtos.loc[linha, 'preco_unitario']
    custo = produtos.loc[linha, 'custo']
    
    py.write(codigo)          # Código do produto
    py.press('tab')

    py.write(marca)          # Marcar do produto 
    py.press('tab')

    py.write(tipo)            # Tipo do produto
    py.press('tab')

    py.write(str(categoria))           # Categoria do produto
    py.press('tab')

    py.write(str(preco))               # Preço do produto
    py.press('tab')

    py.write(str(custo))               # Custo do produto
    py.press('tab')

    obs = produtos.loc[linha, 'obs']
    if not pd.isna(obs):
        py.write(str(obs))                 # Observação do produto
    py.press('tab')

    py.press('enter')               # Cadastrar o produto

    py.scroll(5000)

# Passo 5 - Repetir o processo até acabar a base de dados

