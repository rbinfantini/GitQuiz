import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def mostrar_boas_vindas():
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.YELLOW + Style.BRIGHT + "       BEM-VINDO AO GITQUIZ       ")
    print(Fore.CYAN + Style.BRIGHT + "=" * 50 + "\n")

def mostrar_acerto():
    print(Fore.GREEN + Style.BRIGHT + "Resposta Correta!\n")

def mostrar_erro():
    print(Fore.RED + Style.BRIGHT + "Resposta Incorreta.\n")

def mostrar_game_over(resultado):
    print("\n" + Fore.MAGENTA + Style.BRIGHT + "=" * 50)
    print(Fore.YELLOW + Style.BRIGHT + "                  FIM DE JOGO                   ")
    print(Fore.CYAN + f"   Você acertou {resultado['acertos']} de {resultado['total']} perguntas.")
    print(Fore.GREEN + f"   Pontuação Final: {resultado['pontuacao']}%")
    print(Fore.MAGENTA + Style.BRIGHT + "=" * 50 + "\n")