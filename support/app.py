import pyperclip
import pyautogui
from random_location import set_locations
from random_service import set_service
from random_description import set_description
from time import sleep


amount = int(input('Define the number of tickets to be opened: '))

# Definir a localizacao de cada campo
position_service = 2405,413
position_applicant = 2033,568
position_email = 2685,595
position_not_email = 2678,616
position_location = 2404,882
position_description = 2161,678
position_continue = 2319,927

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

    pyautogui.click(2279,710, duration=1)

    # # Localizacao
    location = set_locations()
    pyperclip.copy(location)
    pyautogui.click(position_location, duration=1)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.press('enter')

    sleep(1)
    
    pyautogui.click(2221,884, duration=1)
    pyautogui.hotkey('space')

    # Descricao
    description = set_description(service)
    pyperclip.copy(description)
    pyautogui.click(position_description, duration=1)
    pyautogui.hotkey('ctrl', 'v')

    # # finalizar o chamado e começa o proximo
    pyautogui.click(position_continue, duration=1)
    sleep(5)