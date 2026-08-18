# RPG de Arena em Turnos - Repositório Base (Minicurso).
---

## Deploy Online no Vercel (Visualização para Alunos)

**Acesse o jogo online em**: [https://minicursoufv.vercel.app/](https://minicursoufv.vercel.app/)

---

## Arquitetura do Projeto

```
Minicurso/
├── vercel.json          
├── index.html                    # Interface Web responsiva para o Vercel
├── config/
│   └── settings.py          # Constantes globais do jogo
├── core/
│   ├── entities.py          # Classes Character, Player e Enemy 
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
└── README.md
```

---

## Como Executar Localmente

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

## Como Executar os Testes Unitários

```bash
python -m unittest discover tests
```