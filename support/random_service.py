import random

def set_service(key = None):
    service = {
        1: "SU-60 - Alteração de senha de Usuário",
        2: "SU-61 - Atualização de dados do Usuário",
        3: "SU-63 - Autorização de Acesso",
        4: "SU-30 - Zimbra DeskTop",
        5: "SU-31 - Mozilla ThunderBird",
        6: "SU-32 - Outlook",
        7: "IMP-10 - Impressora - Hardware - Manutenção Corretiva",
        8: "PC-09 - Periféricos - HD Externo",
        9: "PC-17 - Backups",
        10: "PC-18 - Periférico - Microfone",
        11: "SU-05 - Computador - Manutenção",
        12: "SU-06 - Computador - Substituição",
        13: "SU-07 - Computador - Formatação",
        14: "SU-08 - Computador - Remanejamento / Movimentação",
        15: "SU-09 - Periféricos - Mouse",
        16: "SU-10 - Periféricos - Teclado",
        17: "SU-16 - Periféricos - Nobreak",
        18: "SU-25 - Ponto de Rede - Crimpagem de ponto",
        19: "SU-26 - Ponto de Rede - Remanejamento de Ponto",
        20: "SU-27 - Ponto de Rede - Instalação de Cabeamento Cat 5",
        21: "SU-52 - Monitor - Hardware - Remanejamento / Movimentação",
        22: "IT-02 - Erro de acesso a página",
        23: "SU-03 - Microsoft Windows 10",
        24: "Su-11 - Windows Adicionar Computador no Domínio",
        25: "SU-12 - Windows Compartilhamento de Pasta",
        26: "SU-13 - Windows Formatação",
        27: "SU-14 - Windows Instalação",
        28: "SU-15 - Windows Manutenção",
        29: "SU-70 - Antivirus",
        30: "SU-72 - FreePDF",
        31: "SU-73 - Microsoft Office",
        32: "SU-75 - Google Chrome",
        33: "SU-76 - Mozilla FireFox",
        34: "SU-78 - 7-Zip",
        35: "SU-79 - Java",
        36: "SU-80 - Java Runtime Environment",
        37: "SU-81 - Adobe Acrobat",
        38: "SU-89 - Módulo de Segurança Bancário",
        39: "SU-92 - Siafi",
        40: "SU-66 - VOIP - Configuração"
    }

    if key is None:
        key = random.randint(1, 40)

    return service[key]