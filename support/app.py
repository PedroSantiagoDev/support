import pyperclip
import pyautogui
from random_location import set_locations
from random_service import set_service
from random_description import set_description
from time import sleep


amount = int(input('Define the number of tickets to be opened: '))

# Definir a localizacao de cada campo
position_service = 1045,384
position_applicant = 668,559
position_email = 1322,592
position_not_email = 1318,611
position_location = 1039,895
position_description = 859,635
position_continue = 951,910

for _ in range(amount):
    # Categoria
    service = set_service()
    pyperclip.copy(service)
    pyautogui.click(position_service, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.press('enter')

    sleep(3)
    # Requerente
    applicant = 'glpi'
    pyperclip.copy(applicant)
    pyautogui.click(position_applicant, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    # Acompanhar por e-mail
    pyautogui.click(position_email, duration=1)
    # Marca como não
    pyautogui.click(position_not_email, duration=1)

    pyautogui.click(940,703, duration=1)

    # # Localizacao
    location = set_locations()
    pyperclip.copy(location)
    pyautogui.click(position_location, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.press('enter')

    sleep(1)
    
    pyautogui.click(940,703, duration=1)
    pyautogui.hotkey('space')

    # Descricao
    description = set_description(service)
    pyperclip.copy(description)
    pyautogui.click(position_description, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    # # finalizar o chamado e começa o proximo
    pyautogui.click(position_continue, duration=1)
    sleep(5)