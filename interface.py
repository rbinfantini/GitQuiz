import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def mostrar_boas_vindas():
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.YELLOW + Style.BRIGHT + "       BEM-VINDO AO GITQUIZ       ")
    print(Fore.CYAN + Style.BRIGHT + "=" * 50 + "\n")

def mostrar_acerto():
    print(Fore.GREEN + Style.BRIGHT + "✔ Resposta Correta!\n")

def mostrar_erro():
    print(Fore.RED + Style.BRIGHT + "✖ Resposta Incorreta.\n")