import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def mostrar_boas_vindas():
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.YELLOW + Style.BRIGHT + "       BEM-VINDO AO GITQUIZ       ")
    print(Fore.CYAN + Style.BRIGHT + "=" * 50 + "\n")