# Passo 1: Entrar no sistema da empresa 
# Link para acesso ao sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui  # Biblioteca para automação de ações no teclado e mouse
import time       # Biblioteca para gerenciar pausas no código

# Configuração global: define uma pausa de 0.3 segundos entre as ações do pyautogui
pyautogui.PAUSE = 0.3

# Abrir o navegador (chrome)
pyautogui.press("win")  # Pressiona a tecla Windows
pyautogui.write("chrome")  # Digita "chrome" para buscar o navegador
pyautogui.press("enter")  # Pressiona Enter para abrir o navegador

# Acessar o link do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")  # Digita o link
pyautogui.press("enter")  # Pressiona Enter para carregar a página
time.sleep(3)  # Aguarda 3 segundos para a página carregar

# Passo 2: Fazer login
pyautogui.click(x=685, y=451)  # Clica no campo de email
pyautogui.write("pythonimpressionador@gmail.com")  # Digita o email
pyautogui.press("tab")  # Navega para o próximo campo (senha)
pyautogui.write("sua senha")  # Digita a senha
pyautogui.click(x=955, y=638)  # Clica no botão de login
time.sleep(3)  # Aguarda 3 segundos para o login ser processado

# Passo 3: Importar a base de produtos
import pandas as pd  # Biblioteca para manipulação de dados
tabela = pd.read_csv("produtos.csv")  # Lê os dados do arquivo CSV
print(tabela)  # Exibe os dados carregados

# Passo 4: Cadastrar um produto
for linha in tabela.index:  # Itera por cada linha da tabela
    pyautogui.click(x=653, y=294)  # Clica no campo de código do produto
    codigo = tabela.loc[linha, "codigo"]  # Obtém o código do produto
    pyautogui.write(str(codigo))  # Digita o código
    pyautogui.press("tab")  # Avança para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))  # Digita a marca
    pyautogui.press("tab")  
    pyautogui.write(str(tabela.loc[linha, "tipo"]))  # Digita o tipo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))  # Digita a categoria
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))  # Digita o preço
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))  # Digita o custo
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]  # Verifica o campo de observações
    if not pd.isna(obs):  # Se não for vazio ou NaN, digita as observações
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")  # Confirma o cadastro do produto
    pyautogui.scroll(5000)  # Rola a tela para o início para evitar sobreposição