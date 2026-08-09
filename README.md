# ⚔️ RPG de Arena em Turnos - Repositório Base (Minicurso Git & Engenharia de Software)

Projeto base desenvolvido em **Python 3** e **HTML5/JS (Vercel)** para simular um ambiente de desenvolvimento real com boas práticas de Engenharia de Software (separação de responsabilidades, Padrões de Projeto e Integração Contínua) durante um **Minicurso de Git & GitHub**.

---

## 🌐 Deploy Online no Vercel (Visualização para Alunos)

O repositório conta com deploy automatizado via **GitHub Actions** para o **Vercel**, permitindo que alunos e professores acessem a aplicação diretamente pelo navegador.

---

## 🔑 Guia Passo a Passo: Configuração do Vercel e GitHub Actions (CI/CD)

Para que o deploy automático funcione a cada `push` ou `pull_request` no GitHub, siga estes passos para obter e configurar as 3 variáveis secretas (`VERCEL_TOKEN`, `VERCEL_ORG_ID`, `VERCEL_PROJECT_ID`).

### 1. Obter o `VERCEL_TOKEN`
1. Acesse o painel do Vercel: [https://vercel.com/account/tokens](https://vercel.com/account/tokens).
2. Clique em **Create Token** (ou "Criar Token").
3. Dê um nome ao token (ex: `GitHub Actions Minicurso`) e selecione o escopo de acesso.
4. Copie o token gerado.

### 2. Criar o Projeto no Vercel e obter `VERCEL_ORG_ID` e `VERCEL_PROJECT_ID`
Existem duas formas simples de vincular o projeto:

#### Opção A (Via Vercel Web Dashboard):
1. No dashboard do Vercel ([https://vercel.com/new](https://vercel.com/new)), importe o seu repositório do GitHub.
2. Após criar o projeto, vá em **Project Settings** (Configurações do Projeto).
3. Na aba **General**, copie o **Project ID** (`VERCEL_PROJECT_ID`).
4. Na aba **Team / Account Settings**, copie o **Org ID** ou **User ID** (`VERCEL_ORG_ID`).

#### Opção B (Via Terminal com Vercel CLI):
1. No terminal do seu computador, dentro da pasta do projeto, execute:
   ```bash
   npx vercel
   ```
2. Siga as instruções na tela (faça login e confirme a criação do projeto).
3. Abra o arquivo oculto gerado em `.vercel/project.json`. Ele conterá:
   ```json
   {
     "orgId": "SUA_ORG_ID_AQUI",
     "projectId": "SEU_PROJECT_ID_AQUI"
   }
   ```

### 3. Adicionar as Secrets no Repositório do GitHub
1. Abra o seu repositório no GitHub.
2. Acesse **Settings** > **Secrets and variables** > **Actions**.
3. Clique em **New repository secret** e adicione as 3 variáveis:
   - `VERCEL_TOKEN`: (O token copiado no Passo 1)
   - `VERCEL_ORG_ID`: (O `orgId` copiado no Passo 2)
   - `VERCEL_PROJECT_ID`: (O `projectId` copiado no Passo 2)

---

## 🏗️ Arquitetura do Projeto

```
Minicurso/
├── vercel.json                   # Configuração de rotas e build do Vercel
├── index.html                    # Interface Web responsiva para o Vercel
├── config/
│   └── settings.py          # Constantes globais do jogo (Ponto de conflito no Git)
├── core/
│   ├── entities.py          # Classes Character, Player e Enemy (sem UI/prints)
│   ├── items.py             # Composição de objetos (Weapon, Potion)
│   └── engine.py            # GameEngine e padrão Observer (EventNotifier)
├── ui/
│   ├── cli_view.py          # Interface de linha de comando (stdout/print)
│   └── gui_view.py          # Interface gráfica Tkinter
├── tests/
│   └── test_combat.py       # Testes unitários com unittest
├── .github/
│   └── workflows/
│       ├── ci.yml           # CI de Lint (Flake8) e Testes Unitários
│       └── deploy-vercel.yml # CD de Deploy Automático no Vercel
├── TASKS.md                  # Backlog de 20 Tasks para atividades dos alunos
└── README.md
```

---

## 🚀 Como Executar Localmente

### 1. Interface Gráfica Desktop (Tkinter)
```bash
python main.py
```

### 2. Interface de Terminal (CLI)
```bash
python main.py --cli
```

### 3. Servidor Web Local
```bash
python3 -m http.server 8000
```
Acesse `http://localhost:8000` no navegador.

---

## 🧪 Como Executar os Testes Unitários

```bash
python -m unittest discover tests
```