import pyperclip
import pyautogui
import webbrowser
from random_location import set_locations
from random_service import set_service
from random_description import set_description
from time import sleep


amount = int(input('Define the number of tickets to be opened: '))

# Definir a localizacao de cada campo
position = 972,359
position_service = 1034,411
position_applicant = 715,564
position_email = 1323,595
position_not_email = 1315,618
position_location = 1046,887
position_description = 781,706
position_continue = 950,956

chrome_path = '/usr/bin/google-chrome %s'  # No Linux, altere o caminho se necessário

url = 'https://glpi.codevasf.gov.br/front/ticket.form.php'

webbrowser.get(chrome_path).open(url)

# Categoriaglpi
sleep(1)

pyautogui.click(position, duration=1)

for _ in range(amount):


    # Categoriaglpi
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