"""Configurações globais e constantes do RPG de Arena em Turnos.

Este módulo armazena os valores padrão para vida, dano, itens, aparência gráfica
e parâmetros de combate do jogo.
"""

import os

# Caminhos de Mídia (Assets)
BASE_DIR: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR: str = os.path.join(BASE_DIR, "assets")
HERO_SPRITE_PATH: str = os.path.join(ASSETS_DIR, "hero.ppm")
ENEMY_SPRITE_PATH: str = os.path.join(ASSETS_DIR, "enemy.ppm")

# Configurações do Jogador
PLAYER_MAX_HEALTH: int = 100
PLAYER_BASE_DAMAGE: int = 15
PLAYER_INITIAL_POTIONS: int = 3

# Configurações de Combate Avançado (Tasks 02, 03, 04)
CRITICAL_HIT_CHANCE: float = 0.20
CRITICAL_HIT_MULTIPLIER: float = 1.75
SPECIAL_ATTACK_DAMAGE: int = 35
SPECIAL_ATTACK_COOLDOWN: int = 3
DEFENSE_DAMAGE_REDUCTION: float = 0.50

# Configurações do Inimigo
ENEMY_MAX_HEALTH: int = 80
ENEMY_BASE_DAMAGE: int = 12

# Configurações de Itens
POTION_HEAL_AMOUNT: int = 30
WEAPON_BONUS_DAMAGE: int = 8

# Configurações da Interface Gráfica (GUI)
WINDOW_TITLE: str = "RPG de Arena em Turnos - Minicurso Git"
FULLSCREEN_BY_DEFAULT: bool = True

# Paleta de Cores da UI (Tema Escuro Cyber/Dark Fantasy)
BG_COLOR: str = "#181825"
PANEL_BG: str = "#1e1e2e"
ARENA_BG: str = "#11111b"
TEXT_COLOR: str = "#cdd6f4"
ACCENT_COLOR: str = "#89b4fa"
HEALTH_BAR_COLOR: str = "#a6e3a1"
ENEMY_HEALTH_BAR_COLOR: str = "#f38ba8"
BUTTON_BG: str = "#313244"
BUTTON_FG: str = "#cdd6f4"
BUTTON_HOVER_BG: str = "#45475a"
