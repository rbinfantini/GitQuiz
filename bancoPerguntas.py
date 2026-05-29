# bancoPerguntas.py
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

    # Verdadeiro ou Falso
    {
        "tipo": "verdadeiro_falso",
        "pergunta": "'git add .' adiciona todos os arquivos modificados e novos da pasta atual para a staging area.",
        "resposta": "V",
        "explicacao": "Correto. O ponto representa o diretório atual recursivamente."
    },
    {
        "tipo": "verdadeiro_falso",
        "pergunta": "É possível ter mais de uma branch apontando para o mesmo commit.",
        "resposta": "V",
        "explicacao": "Branches são apenas ponteiros; vários podem apontar para o mesmo commit."
    },
    {
        "tipo": "verdadeiro_falso",
        "pergunta": "'git pull' é exatamente a mesma coisa que 'git fetch'.",
        "resposta": "F",
        "explicacao": "git pull = git fetch + git merge. O fetch só baixa, não integra."
    },
    {
        "tipo": "verdadeiro_falso",
        "pergunta": "O arquivo .gitignore deve ser commitado no repositório para funcionar corretamente.",
        "resposta": "V",
        "explicacao": "Sem commitar, o .gitignore só funciona localmente e não é compartilhado."
    },
    {
        "tipo": "verdadeiro_falso",
        "pergunta": "Deletar uma branch local também deleta a branch no repositório remoto.",
        "resposta": "F",
        "explicacao": "São independentes. Para deletar no remoto: git push origin --delete <branch>."
    },

    # ── Completar o Comando ──────────────────────────────────────────────────
    {
        "tipo": "completar_comando",
        "pergunta": "Complete o comando para criar e já entrar em uma nova branch:\ngit ________ feature/nova-funcao",
        "alternativas": ["A) branch", "B) checkout -b", "C) switch --new", "D) create"],
        "resposta": "B",
        "explicacao": "'git checkout -b' cria e já faz o checkout da nova branch."
    },
    {
        "tipo": "completar_comando",
        "pergunta": "Complete o comando para ver o histórico de commits de forma resumida:\ngit log ________",
        "alternativas": ["A) --short", "B) --summary", "C) --oneline", "D) --brief"],
        "resposta": "C",
        "explicacao": "'git log --oneline' exibe cada commit em uma única linha."
    },
    {
        "tipo": "completar_comando",
        "pergunta": "Complete o comando para desfazer as alterações de um arquivo antes do stage:\ngit ________ arquivo.txt",
        "alternativas": ["A) undo", "B) restore", "C) reset", "D) revert"],
        "resposta": "B",
        "explicacao": "'git restore arquivo.txt' descarta as mudanças na working tree."
    },
    {
        "tipo": "completar_comando",
        "pergunta": "Complete o comando para conectar seu repositório local a um remoto:\ngit remote ________ origin https://github.com/user/repo.git",
        "alternativas": ["A) link", "B) set", "C) add", "D) connect"],
        "resposta": "C",
        "explicacao": "'git remote add' registra um novo repositório remoto com um apelido."
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