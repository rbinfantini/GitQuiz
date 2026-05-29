# Banco de perguntas do GitQuiz
# Modos disponíveis: padrao, presidencia

# MODO PADRÃO
# Formato: multipla_escolha | verdadeiro_falso | completar_comando

perguntas_padrao = [

    # Múltipla escolha
    {
        "tipo": "multipla_escolha",
        "pergunta": "Qual comando cria uma cópia local de um repositório remoto?",
        "alternativas": ["A) git init", "B) git clone", "C) git pull", "D) git fetch"],
        "resposta": "B",
        "explicacao": "git clone copia o repositório inteiro, incluindo histórico."
    },
    {
        "tipo": "multipla_escolha",
        "pergunta": "Qual comando envia seus commits locais para o repositório remoto?",
        "alternativas": ["A) git send", "B) git upload", "C) git push", "D) git commit"],
        "resposta": "C",
        "explicacao": "git push envia os commits da branch local para o remoto."
    },
    {
        "tipo": "multipla_escolha",
        "pergunta": "O que faz o comando 'git status'?",
        "alternativas": [
            "A) Mostra o histórico de commits",
            "B) Mostra arquivos modificados, staged e não rastreados",
            "C) Compara duas branches",
            "D) Exibe informações do repositório remoto"
        ],
        "resposta": "B",
        "explicacao": "git status mostra o estado atual da working tree e da staging area."
    },
    {
        "tipo": "multipla_escolha",
        "pergunta": "Qual é a finalidade de um Pull Request no GitHub?",
        "alternativas": [
            "A) Baixar as alterações do remoto",
            "B) Propor a integração de uma branch em outra, com revisão de código",
            "C) Criar uma nova branch",
            "D) Desfazer o último commit"
        ],
        "resposta": "B",
        "explicacao": "Um PR é um pedido de revisão e merge de uma branch para outra."
    },
    {
        "tipo": "multipla_escolha",
        "pergunta": "O que acontece quando você faz 'git merge' de uma branch na main?",
        "alternativas": [
            "A) A branch é deletada automaticamente",
            "B) Os commits da branch são integrados à main",
            "C) A main passa a apontar para a branch",
            "D) Um novo repositório é criado"
        ],
        "resposta": "B",
        "explicacao": "git merge integra o histórico da branch na branch atual."
    },
    {
        "tipo": "multipla_escolha",
        "pergunta": "O que é um conflito de merge?",
        "alternativas": [
            "A) Quando o push é recusado pelo servidor",
            "B) Quando duas branches modificaram a mesma parte de um arquivo",
            "C) Quando o repositório remoto está fora do ar",
            "D) Quando um commit é feito sem mensagem"
        ],
        "resposta": "B",
        "explicacao": "Conflitos ocorrem quando o Git não consegue mesclar automaticamente."
    },
]

# MODO PRESIDÊNCIA

perguntas_presidencia = []

# Banco central e funções de acesso
BANCO_DE_PERGUNTAS = {
    "padrao": perguntas_padrao,
    "presidencia": perguntas_presidencia,
}

MODOS_DISPONIVEIS = list(BANCO_DE_PERGUNTAS.keys())