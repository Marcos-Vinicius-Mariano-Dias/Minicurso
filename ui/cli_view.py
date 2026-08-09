"""Interface de Linha de Comando (CLI) para o RPG de Arena.

Implementa a interface GameObserver para narrar o combate via terminal (print)
e captura comandos de entrada do usuário.
"""

from typing import Dict, Any
from core.engine import GameEngine


class CLIView:
    """Observador de terminal que exibe a narrativa do combate no stdout."""

    def __init__(self, engine: GameEngine) -> None:
        """Inicializa a visualização CLI e se conecta ao motor do jogo.

        Args:
            engine: Instância do GameEngine a ser observada.
        """
        self.engine: GameEngine = engine
        self.engine.subscribe(self)

    def on_event(self, event_type: str, data: Dict[str, Any]) -> None:
        """Trata eventos enviados pelo GameEngine e imprime no terminal."""
        if event_type == "GAME_STARTED":
            print("\n==========================================")
            print("      ⚔️  BEM-VINDO À ARENA DE RPG! ⚔️")
            print("==========================================")
            p_hp = f"{data['player_health']}/{data['player_max_health']}"
            e_hp = f"{data['enemy_health']}/{data['enemy_max_health']}"
            print(f"Herói: {data['player_name']} (HP: {p_hp})")
            print(f"Inimigo: {data['enemy_name']} (HP: {e_hp})\n")

        elif event_type == "PLAYER_ATTACKED":
            print(f"🗡️  {data['attacker']} atacou {data['target']} causando {data['damage']} dano!")
            t_hp = f"{data['target_health']}/{data['target_max_health']}"
            print(f"   --> {data['target']} agora tem {t_hp} HP.")

        elif event_type == "ENEMY_ATTACKED":
            print(f"🔥 {data['attacker']} contra-atacou causando {data['damage']} de dano!")
            t_hp = f"{data['target_health']}/{data['target_max_health']}"
            print(f"   --> {data['target']} agora tem {t_hp} HP.")

        elif event_type == "PLAYER_HEALED":
            print(f"🧪 {data['player_name']} usou poção e recuperou {data['healed_amount']} HP!")
            curr_hp = f"{data['current_health']}/{data['max_health']}"
            print(f"   --> HP: {curr_hp} | Poções: {data['potions_remaining']}")

        elif event_type == "ACTION_FAILED":
            print(f"⚠️  {data['reason']}")

        elif event_type == "GAME_OVER":
            print("\n==========================================")
            if data["is_player_winner"]:
                print(f"🏆 VITÓRIA! {data['winner']} derrotou o oponente e venceu a partida!")
            else:
                print(f"💀 DERROTA! {data['winner']} venceu o combate...")
            print("==========================================\n")

    def run_loop(self) -> None:
        """Executa o loop de leitura de comandos no terminal."""
        self.engine.start_game()

        while not self.engine.is_game_over:
            if self.engine.current_turn == "player":
                print("\n--- Seus Comandos ---")
                print("1. Atacar [A]")
                print("2. Usar Poção [P]")
                print("3. Sair [Q]")
                choice = input("Escolha sua ação: ").strip().lower()

                if choice in ("1", "a", "atacar"):
                    self.engine.player_attack()
                elif choice in ("2", "p", "pocao", "poção"):
                    self.engine.player_heal()
                elif choice in ("3", "q", "sair"):
                    print("Saindo da arena...")
                    break
                else:
                    print("Opção inválida! Digite 1 (Atacar) ou 2 (Poção).")
