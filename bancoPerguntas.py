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

    # Completar o Comando
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

perguntas_presidencia = [

    # Múltipla escolha avançada / pegadinhas
    {
        "tipo": "multipla_escolha",
        "pergunta": "Você fez 'git rebase origin/main' na sua branch. O que acontece com os SHAs dos seus commits?",
        "alternativas": [
            "A) Permanecem os mesmos",
            "B) São recalculados — novos commits são criados",
            "C) Somem do histórico",
            "D) São marcados como deprecated"
        ],
        "resposta": "B",
        "explicacao": "Rebase reescreve o histórico: cada commit é reaplicado e ganha um novo SHA."
    },
    {
        "tipo": "multipla_escolha",
        "pergunta": "Qual a diferença entre 'git reset --soft HEAD~1' e 'git reset --hard HEAD~1'?",
        "alternativas": [
            "A) Não há diferença prática",
            "B) --soft mantém as mudanças no stage; --hard descarta tudo",
            "C) --soft apaga o commit do remoto; --hard só apaga o local",
            "D) --hard mantém o stage; --soft descarta"
        ],
        "resposta": "B",
        "explicacao": "--soft volta o HEAD mas mantém os arquivos staged. --hard apaga tudo."
    },
    {
        "tipo": "multipla_escolha",
        "pergunta": "O que o comando 'git cherry-pick <SHA>' faz?",
        "alternativas": [
            "A) Cria uma tag no commit especificado",
            "B) Aplica as mudanças de um commit específico na branch atual",
            "C) Move a branch atual para o commit especificado",
            "D) Reverte o commit especificado"
        ],
        "resposta": "B",
        "explicacao": "cherry-pick copia um commit de qualquer lugar e aplica na branch atual."
    },
    {
        "tipo": "multipla_escolha",
        "pergunta": "Você deu 'git push --force' na main compartilhada. O que pode acontecer?",
        "alternativas": [
            "A) Nada, é equivalente ao push normal",
            "B) Sobrescreve o histórico remoto, causando problemas para todos do time",
            "C) O GitHub bloqueia automaticamente",
            "D) Apenas seus commits locais são enviados"
        ],
        "resposta": "B",
        "explicacao": "--force reescreve o histórico remoto. Em branch compartilhada, é destrutivo."
    },

    # Verdadeiro ou Falso — pegadinhas
    {
        "tipo": "verdadeiro_falso",
        "pergunta": "'git revert' é seguro para usar em branches públicas, diferente de 'git reset'.",
        "resposta": "V",
        "explicacao": "revert cria um novo commit que desfaz; não reescreve histórico. Reset sim."
    },
    {
        "tipo": "verdadeiro_falso",
        "pergunta": "Um 'git fetch' pode sobrescrever arquivos na sua working tree.",
        "resposta": "F",
        "explicacao": "fetch só atualiza as refs remotas locais. Nunca toca na working tree."
    },
    {
        "tipo": "verdadeiro_falso",
        "pergunta": "É possível fazer um commit vazio (sem nenhuma mudança de arquivo) com Git.",
        "resposta": "V",
        "explicacao": "git commit --allow-empty cria um commit sem mudanças. Útil para triggers de CI."
    },
    {
        "tipo": "verdadeiro_falso",
        "pergunta": "O comando 'git stash' salva também os arquivos untracked por padrão.",
        "resposta": "F",
        "explicacao": "Por padrão, stash ignora arquivos untracked. Use 'git stash -u' para incluí-los."
    },

    # Completar o Comando — avançado
    {
        "tipo": "completar_comando",
        "pergunta": "Complete o comando para fazer push de uma branch local para o remoto E já configurar o tracking:\ngit push ________ origin feature/minha-branch",
        "alternativas": ["A) --track", "B) --set-upstream", "C) --link", "D) --remote"],
        "resposta": "B",
        "explicacao": "'git push --set-upstream' (ou -u) configura o tracking automático da branch."
    },
    {
        "tipo": "completar_comando",
        "pergunta": "Você quer um rebase interativo dos últimos 3 commits para limpar o histórico. Complete:\ngit rebase ________ HEAD~3",
        "alternativas": ["A) --edit", "B) --squash", "C) -i", "D) --clean"],
        "resposta": "C",
        "explicacao": "'git rebase -i' abre o editor interativo para reorganizar, squash, reword etc."
    },
]

# Banco central e funções de acesso

BANCO_DE_PERGUNTAS = {
    "padrao": perguntas_padrao,
    "presidencia": perguntas_presidencia,
}

MODOS_DISPONIVEIS = list(BANCO_DE_PERGUNTAS.keys())