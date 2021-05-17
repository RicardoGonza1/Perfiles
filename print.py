import pyautogui
import webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=573142425831&text=Estoy+interesado%28a%29+en+FutuTiendas&app_absent=0')

sleep(50)

with open('song.txt','r') as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")
        sleep(5)    