import time  # Biblioteca para pausas no código
import pyautogui  # Biblioteca para automação de teclado e mouse

time.sleep(5)  # Aguarda 5 segundos antes de executar a próxima ação
print(pyautogui.position())  # Captura e exibe a posição atual do cursor do mouse na tela

pyautogui.scroll(200)  # Rola a tela 200 unidades para cima