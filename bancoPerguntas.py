# Banco de perguntas do GitQuiz
# Modos disponíveis: padrao, presidencia

#  MODO PADRÃO — Git & GitHub para todos
# Formato: multipla_escolha | verdadeiro_falso | completar_comando

perguntas_padrao = []

#MODO PRESIDÊNCIA

perguntas_presidencia = []

#Banco central e funções de acesso

BANCO_DE_PERGUNTAS = {
    "padrao": perguntas_padrao,
    "presidencia": perguntas_presidencia,
}

MODOS_DISPONIVEIS = list(BANCO_DE_PERGUNTAS.keys())