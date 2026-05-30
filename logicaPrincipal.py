# Lógica Principal - GitQuiz [PUCTech]

from bancoPerguntas import get_perguntas
import interface

def normalizar_resposta(resposta):
    return resposta.strip().upper()

def verificar_resposta(pergunta, resposta_usuario):
    resposta_usuario = normalizar_resposta(resposta_usuario)
    resposta_correta = pergunta["resposta"].upper()
    return resposta_usuario == resposta_correta

def calcular_pontuacao(acertos, total):
    if total == 0:
        return 0
    return int((acertos / total) * 100)

def executar_quiz(modo):
    perguntas = get_perguntas(modo)
    acertos = 0
    erros = 0
    total = len(perguntas)

    # Limpa a tela e mostra a sua arte de boas-vindas
    interface.limpar_tela()
    interface.mostrar_boas_vindas()

    for pergunta in perguntas:
        print(f"\n{pergunta['pergunta']}")
        for alternativa in pergunta["alternativas"]:
            print(alternativa)

        resposta = input("\nSua resposta: ")

        if verificar_resposta(pergunta, resposta):
            interface.mostrar_acerto()
            acertos += 1
        else:
            interface.mostrar_erro()
            erros += 1

        print(f"Explicação: {pergunta['explicacao']}\n")
        print("-" * 40)

    pontuacao = calcular_pontuacao(acertos, total)

    return {
        "modo": modo,
        "acertos": acertos,
        "erros": erros,
        "total": total,
        "pontuacao": pontuacao
    }

if __name__ == "__main__":
    resultado_final = executar_quiz("padrao")
    interface.mostrar_game_over(resultado_final)