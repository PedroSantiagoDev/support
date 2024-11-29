import pyperclip
import pyautogui
import webbrowser
from random_location import set_locations
from random_service import set_service
from random_description import set_description
from time import sleep


amount = int(input('Define the number of tickets to be opened: '))

chrome_path = '/usr/bin/google-chrome %s'  # No Linux, altere o caminho se necessário

url = 'https://atendimentoti.codevasf.gov.br/front/ticket.form.php'

webbrowser.get(chrome_path).open(url)

# Categoriaglpi
sleep(2)

pyautogui.click(1383,296, duration=1)

for _ in range(amount):

    #tipo
    pyautogui.click(1600,322, duration=1)
    pyautogui.click(1607,386, duration=1)
    sleep(2)

    #categoria
    service = set_service(12)
    pyperclip.copy(service)
    pyautogui.click(1599,365, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    sleep(2)
    pyautogui.press('enter')

    sleep(3)

    #status
    pyautogui.click(1601,450, duration=1)
    pyautogui.click(1576,607, duration=1)

    #Localização
    location = set_locations(9)
    pyperclip.copy(location)
    pyautogui.click(1576,695, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.press('enter')

    pyautogui.click(1390,672, duration=1)
    sleep(1)
    pyautogui.hotkey('space')

    # Requerente
    applicant = '60934194360'
    pyperclip.copy(applicant)
    pyautogui.click(1463,278, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.press('enter')
    sleep(2)

    #date
    pyautogui.click(1568,319, duration=1)
    pyautogui.click(1583,693, duration=1)
    pyautogui.click(1395,472, duration=1)

    #date solução
    pyautogui.click(1586,362, duration=1)
    pyautogui.click(1569,739, duration=1)
    pyautogui.click(1395,472, duration=1)

    sleep(1)

    # Descricao
    description = set_description(service)
    pyperclip.copy(description)
    pyautogui.click(514,516, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)

    # finalizar o chamado e começa o proximo
    pyautogui.click(1809,998, duration=1)
    sleep(5)