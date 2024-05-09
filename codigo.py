#Passo a passo do projeto

# 1. Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# para instalar: pip install pyautogui
import pyautogui
import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

# pyautogui.click(x=774, y=611)
# Entrar no site do sistema

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# aqui pode ser que ele demore alguns segundos para carregar o site
time.sleep(3)

# 2. Fazer login
pyautogui.click(x=725, y=384)
pyautogui.write("d.santos.barbosa@hotmail.com")

pyautogui.press("tab")
pyautogui.write("Psychofaint1")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# 3. Abrir/Importar a base de dados de produtos para cadastrar
# pip install pandas numpy openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# 4. Cadastrar um produto

for linha in tabela.index:

    codigo = str(tabela.loc[linha, "codigo"])

    pyautogui.click(x=694, y=274)
    pyautogui.write(codigo)
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = (str(tabela.loc[linha, "obs"]))
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    
    pyautogui.press("enter")

    pyautogui.scroll(5000)


