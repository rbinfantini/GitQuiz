# Lógica Principal - GitQuiz [PUCTech]

# Busca as perguntas no banco de perguntas
from perguntas import get_perguntas

'''
Função para normalizar a resposta, removendo espaços extras e convertendo para maiúscula.
Parâmetros:
    resposta (str): A resposta do usuário a ser normalizada.
Retorna:
    str: A resposta normalizada, pronta para comparação.
'''
def normalizar_resposta(resposta):
    return resposta.strip().upper()


'''
Função para verificar se a resposta do usuário está correta.
Parâmetros:
    pergunta (dict): O dicionário contendo a pergunta e a resposta correta.
    resposta_usuario (str): A resposta fornecida pelo usuário.
Retorna:
    bool: True se a resposta estiver correta, False caso contrário.
'''
def verificar_resposta(pergunta, resposta_usuario):
    resposta_usuario = normalizar_resposta(resposta_usuario)
    resposta_correta = pergunta["resposta"].upper()

    return resposta_usuario == resposta_correta

'''
Função para calcular a pontuação do usuário com base no número de acertos e total de perguntas.
Parâmetros:
    acertos (int): O número de respostas corretas do usuário.
    total (int): O número total de perguntas respondidas.
Retorna:
    int: A pontuação do usuário, calculada como uma porcentagem de acertos.
'''
def calcular_pontuacao(acertos, total):
    if total == 0:
        return 0
    
    return int((acertos / total) * 100)

'''
Função para executar o quiz, apresentando as perguntas ao usuário e coletando suas respostas.
Parâmetros:
    modo (str): O modo do quiz, que determina o conjunto de perguntas a ser utilizado.
Retorna:
    dict: Um dicionário contendo os resultados do quiz, incluindo o modo, número de acertos, erros, total de perguntas e pontuação.
'''
def executar_quiz(modo):
    perguntas = get_perguntas(modo)
    acertos = 0
    erros = 0
    total = len(perguntas)

    # Exibe a pergunta
    for pergunta in perguntas:
        print(pergunta["pergunta"])

        # Exibe as alternativas
        for alternativa in pergunta["alternativas"]:
            print(alternativa)

        # Solicita a resposta do usuário
        resposta = input("Sua resposta: ")

        # Valida a resposta do usuário
        if verificar_resposta(pergunta, resposta):
            print("Resposta Correta!")
            acertos += 1
        else:
            print("Resposta Incorreta.")
            erros += 1

        # Mostra a exxplicação
        print(f"Explicação: {pergunta['explicacao']}\n")
        print()

    # Calcula a pontuação final do usuário
    pontuacao = calcular_pontuacao(acertos, total)

    return {
        "modo": modo,
        "acertos": acertos,
        "erros": erros,
        "total": total,
        "pontuacao": pontuacao
    }


'''
Função para mostrar os resultados finais do quiz.
Parâmetros:
    resultado (dict): O dicionário contendo os resultados do quiz, incluindo o modo, número de acertos, erros, total de perguntas e pontuação.
Retorna:
    None: Esta função apenas exibe os resultados e não retorna nenhum valor.
'''
def mostrar_resultados(resultado):
    print("=== Resultado Final ===")
    print(f"Modo: {resultado['modo']}")
    print(f"Acertos: {resultado['acertos']}")
    print(f"Erros: {resultado['erros']}")
    print(f"Total de perguntas: {resultado['total']}")
    print(f"Porcentagem: {resultado['porcentagem']:.2f}%")