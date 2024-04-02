import random

def set_service(key = None):
    service = {
        1: "SU-61 - Atualização de dados do Usuário",
        2: "SU-63 - Autorização de Acesso",
        3: "SU-30 - Zimbra DeskTop",
        4: "SU-31 - Mozilla ThunderBird",
        5: "SU-32 - Outlook",
        6: "IMP-10 - Impressora - Hardware - Manutenção Corretiva",
        7: "PC-09 - Periféricos - HD Externo",
        8: "PC-17 - Backups",
        9: "SU-05 - Computador - Manutenção",
        10: "SU-06 - Computador - Substituição",
        11: "SU-07 - Computador - Formatação",
        12: "SU-08 - Computador - Remanejamento / Movimentação",
        13: "SU-09 - Periféricos - Mouse",
        14: "SU-10 - Periféricos - Teclado",
        15: "SU-16 - Periféricos - Nobreak",
        16: "SU-25 - Ponto de Rede - Crimpagem de ponto",
        17: "SU-26 - Ponto de Rede - Remanejamento de Ponto",
        18: "SU-27 - Ponto de Rede - Instalação de Cabeamento Cat 5",
        19: "SU-52 - Monitor - Hardware - Remanejamento / Movimentação",
        20: "IT-02 - Erro de acesso a página",
        21: "SU-03 - Microsoft Windows 10",
        22: "Su-11 - Windows Adicionar Computador no Domínio",
        23: "SU-12 - Windows Compartilhamento de Pasta",
        24: "SU-13 - Windows Formatação",
        25: "SU-14 - Windows Instalação",
        26: "SU-15 - Windows Manutenção",
        27: "SU-70 - Antivirus",
        28: "SU-72 - FreePDF",
        29: "SU-73 - Microsoft Office",
        30: "SU-75 - Google Chrome",
        31: "SU-76 - Mozilla FireFox",
        32: "SU-78 - 7-Zip",
        33: "SU-79 - Java",
        34: "SU-80 - Java Runtime Environment",
        35: "SU-81 - Adobe Acrobat",
        36: "SU-89 - Módulo de Segurança Bancário",
        37: "SU-92 - Siafi",
        38: "SU-66 - VOIP - Configuração"
    }

    if key is None:
        key = random.randint(1, 38)

    return service[key]