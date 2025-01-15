# pip install pyautogui
import pyautogui
import time

# pausa para cada comando
pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.hotkey("ctrl" , "c") -> combinações

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")


pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

pyautogui.press("f11")

time.sleep(3)

# login
pyautogui.press("tab")
# pyautogui.click(x=700, y=370) 

pyautogui.write("batatinha@gmail.com")

# próximo campo
pyautogui.press("tab")

pyautogui.write("sofia pq voce nunca avisa onde vai porra")

pyautogui.press("tab")

pyautogui.press("enter")
                
# pip install pandas openpyxl
import pandas

# pandas.read_csv("C:\Users\marcos\Downloads\produtos.csv")
tabela = pandas.read_csv("produtos.csv")

time.sleep(2)

# for coluna in tabela.columns

for linha in tabela.index:
    pyautogui.click(x=920, y=170)

    # código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    # str converte para string
    pyautogui.write(str(categoria)) 
    pyautogui.press("tab")

    # preco_unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])    
    if obs != "nan":
            pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    # pyautogui.press("pgup")
    pyautogui.scroll(5000)

