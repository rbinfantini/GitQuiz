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