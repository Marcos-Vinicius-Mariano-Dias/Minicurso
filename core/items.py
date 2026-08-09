"""Módulo de itens do jogo.

Demonstra composição de objetos dentro do sistema de combate (ex: armas e poções).
"""


class Weapon:
    """Representa uma arma equipável por um personagem."""

    def __init__(self, name: str, bonus_damage: int) -> None:
        """Inicializa uma nova arma.

        Args:
            name: Nome da arma.
            bonus_damage: Dano adicional concedido ao personagem.
        """
        self.name: str = name
        self.bonus_damage: int = bonus_damage

    def __repr__(self) -> str:
        return f"Weapon(name='{self.name}', bonus_damage={self.bonus_damage})"


class Potion:
    """Representa uma poção de cura no inventário."""

    def __init__(self, name: str = "Poção de Cura", heal_amount: int = 30) -> None:
        """Inicializa uma poção de cura.

        Args:
            name: Nome da poção.
            heal_amount: Quantidade de pontos de vida restaurados.
        """
        self.name: str = name
        self.heal_amount: int = heal_amount

    def use(self) -> int:
        """Consome a poção e retorna a quantidade de cura.

        Returns:
            int: Quantidade de vida a ser curada.
        """
        return self.heal_amount
