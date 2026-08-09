#  Plano de Tasks - Minicurso de Git & GitHub (RPG Arena)

Este documento contém um **backlog de 20 tarefas (tasks)** estruturadas para o minicurso de Git. Cada task simula uma demanda real de desenvolvimento de software (criação de branch, modificação de regras de negócio ou UI, tratamento de conflitos e abertura de Pull Request).

---

##  Lista de Tasks do Projeto

###  Tasks Prioritárias (Já Implementadas no Repositório Base)

#### [TASK-01] Espelhamento de Sprites e Gerenciador de Telas
- **Objetivo**: Inverter o sprite do inimigo para encarar o herói e criar um fluxo de telas (`Start Screen`, `Arena`, `End Screen`).
- **Arquivos Afetados**: `ui/gui_view.py`, `assets/enemy.ppm`.

#### [TASK-02] Sistema de Dano Crítico
- **Objetivo**: Adicionar 20% de chance para ataques desferirem acertos críticos (1.75x de dano).
- **Arquivos Afetados**: `config/settings.py`, `core/engine.py`.

#### [TASK-03] Habilidade Especial (Golpe Devastador)
- **Objetivo**: Adicionar o comando de ataque especial com *cooldown* de 3 turnos.
- **Arquivos Afetados**: `core/entities.py`, `core/engine.py`, `ui/gui_view.py`.

#### [TASK-04] Postura de Defesa (Shield Stance)
- **Objetivo**: Adicionar a ação "Defender", reduzindo o dano recebido no próximo turno em 50%.
- **Arquivos Afetados**: `core/entities.py`, `core/engine.py`, `ui/gui_view.py`.

#### [TASK-05] Números Flutuantes de Dano no Canvas
- **Objetivo**: Animar o valor do dano e cura subindo dinamicamente sobre os personagens no palco.
- **Arquivos Afetados**: `ui/gui_view.py`.

---

###  Tasks de Exercício para os Alunos (Backlog para Pull Requests)

#### [TASK-06] Modo História / Campanha com Diálogos
- **Descrição**: Criar um modo história com capítulos sequenciais (Capítulo 1: A Invasão do Vilarejo, Capítulo 2: As Ruínas do Dragão) contendo caixas de diálogo pré-batalha entre o Herói e o Vilão.
- **Conceito Git**: Exercício de branching longo e criação de novos módulos (`core/story.py`).
- **Complexidade**: ⭐⭐⭐ (Alta)

#### [TASK-07] Seleção de Classes de Personagem
- **Descrição**: Permitir ao jogador escolher entre 3 classes na tela de início: **Guerreiro** (alta vida), **Mago** (dano mágico elevado) e **Ladino** (alta taxa crítica).
- **Conceito Git**: Herança de classes em Python e conflito no `entities.py`.
- **Complexidade**: ⭐⭐⭐ (Alta)

#### [TASK-08] Sistema de Ondas de Inimigos (Wave System)
- **Descrição**: Ao derrotar um inimigo, o próximo da lista surge automaticamente sem reiniciar a vida do jogador.
- **Conceito Git**: Alteração da estrutura do loop no `core/engine.py`.
- **Complexidade**: ⭐⭐ (Média)

#### [TASK-09] Barra de Mana e Habilidades Mágicas
- **Descrição**: Adicionar a barra de Mana (MP) ao jogador e ao `settings.py`. Habilidades consomem MP que regenera 5 pontos por turno.
- **Conceito Git**: Alteração de configurações no `settings.py` (conflitos planejados).
- **Complexidade**: ⭐⭐ (Média)

#### [TASK-10] Efeitos de Status (Debuffs / Buffs)
- **Descrição**: Implementar status de **Veneno** (dano por 3 turnos) e **Atordoamento** (faz o inimigo perder o turno).
- **Conceito Git**: Adição de enums/dicionários no `core/entities.py`.
- **Complexidade**: ⭐⭐ (Média)

#### [TASK-11] Inventário de Itens e Sistema de Loot
- **Descrição**: Inimigos derrotados têm 50% de chance de dropar poções de vida ou elixires de força que são armazenados em um inventário expansível.
- **Conceito Git**: Criação do módulo `core/inventory.py`.
- **Complexidade**: ⭐⭐⭐ (Alta)

#### [TASK-12] Sistema de Nível e Experiência (XP)
- **Descrição**: O jogador ganha pontos de experiência (XP) ao derrotar inimigos. Ao subir de nível, recupera vida e aumenta dano base.
- **Conceito Git**: Modificação no modelo `Player`.
- **Complexidade**: ⭐⭐ (Média)

#### [TASK-13] Ranking e Placar de Melhores Partidas (Leaderboard)
- **Descrição**: Salvar os registros de vitórias em um arquivo local `scores.json` e exibir um botão "Ranking" no menu inicial.
- **Conceito Git**: Manipulação de arquivos JSON e I/O em Python.
- **Complexidade**: ⭐⭐ (Média)

#### [TASK-14] Troca Dinâmica de Biomas e Arenas
- **Descrição**: Permitir escolher o cenário da arena (Caverna, Floresta Sombria, Castelo) alterando a cor de fundo do Canvas.
- **Conceito Git**: Alteração de constantes no `config/settings.py`.
- **Complexidade**: ⭐ (Baixa)

#### [TASK-15] Medidor de Combos e Multiplicador de Dano
- **Descrição**: Acertar 3 ataques seguidos sem usar poção ativa um multiplicador de dano de 1.5x.
- **Conceito Git**: Controle de estado no `core/engine.py`.
- **Complexidade**: ⭐⭐ (Média)

#### [TASK-16] Seletor de Dificuldade (Fácil, Médio, Hardcore)
- **Descrição**: Adicionar seletor de dificuldade na tela inicial que ajusta o HP e o dano do inimigo através do `settings.py`.
- **Conceito Git**: Alteração simultânea por múltiplos alunos (simulação de merge conflict).
- **Complexidade**: ⭐ (Baixa)

#### [TASK-17] Fases e Transformação de Chefão (Boss)
- **Descrição**: Quando o chefe chega a 30% de HP, ele entra em modo "Frenesi" (dobra de dano e muda de cor).
- **Conceito Git**: Condicionais de estado no `core/entities.py`.
- **Complexidade**: ⭐⭐ (Média)

#### [TASK-18] Customização de Atalhos de Teclado
- **Descrição**: Permitir remapear as teclas de atalho (Atacar, Defender, Poção) no `settings.py`.
- **Conceito Git**: Edição de constantes do sistema.
- **Complexidade**: ⭐ (Baixa)

#### [TASK-19] Exportação de Relatório da Batalha (Log Export)
- **Descrição**: Adicionar um botão no final da partida para salvar o histórico de combate em um arquivo `relatorio_batalha.txt`.
- **Conceito Git**: Manipulação de strings e I/O de arquivos.
- **Complexidade**: ⭐ (Baixa)

#### [TASK-20] Modo Sobrevivência (Infinito)
- **Descrição**: O jogador enfrenta inimigos gerados aleatoriamente com atributos progressivamente maiores até ser derrotado.
- **Conceito Git**: Integração de múltiplos módulos do `core`.
- **Complexidade**: ⭐⭐⭐ (Alta)

---

##  Como Utilizar este Backlog no Minicurso

1. O instrutor atribui uma **Task** (ex: `TASK-08` ou `TASK-16`) para cada aluno ou dupla.
2. Cada aluno cria uma branch com o nome da task: `git checkout -b feature/task-08-barra-de-mana`.
3. O aluno implementa a funcionalidade e roda a suíte de testes: `python3 -m unittest discover tests`.
4. O aluno faz o push e abre um Pull Request para a branch `main`.
5. Se dois alunos modificarem o arquivo `config/settings.py`, eles vivenciarão um **conflito de mesclagem (merge conflict)** e aprenderão a resolvê-lo na prática!
