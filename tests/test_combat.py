"""Testes unitários para a lógica de combate e habilidades do RPG de Arena.

Executados no CI a cada Pull Request para garantir que alterações no código
não quebrem as regras do jogo.
"""

import unittest
from core.entities import Player, Enemy
from core.engine import GameEngine, GameObserver


class MockObserver(GameObserver):
    """Observador fictício para testar o envio de eventos do motor."""

    def __init__(self) -> None:
        self.events: list = []

    def on_event(self, event_type: str, data: dict) -> None:
        self.events.append((event_type, data))


class TestCombatLogic(unittest.TestCase):
    """Suíte de testes das regras de combate."""

    def setUp(self) -> None:
        """Inicializa entidades limpas."""
        self.player = Player(name="HeroiTeste", max_health=100, base_damage=15, potions=2)
        self.enemy = Enemy(name="MonstroTeste", max_health=50, base_damage=10)

    def test_character_take_damage(self) -> None:
        """Testa se o dano reduz a vida corretamente sem ficar menor que zero."""
        damage_dealt = self.player.take_damage(30)
        self.assertEqual(damage_dealt, 30)
        self.assertEqual(self.player.health, 70)

        damage_dealt_overkill = self.player.take_damage(200)
        self.assertEqual(damage_dealt_overkill, 70)
        self.assertEqual(self.player.health, 0)
        self.assertFalse(self.player.is_alive())

    def test_character_defense_stance(self) -> None:
        """Testa se a postura de defesa reduz o dano recebido em 50%."""
        self.player.set_defense_stance()
        self.assertTrue(self.player.is_defending)

        damage_taken = self.player.take_damage(40)
        self.assertEqual(damage_taken, 20)
        self.assertEqual(self.player.health, 80)
        self.assertFalse(self.player.is_defending)

    def test_character_heal_cap(self) -> None:
        """Testa se a cura restaura a vida sem ultrapassar a vida máxima."""
        self.player.take_damage(40)
        self.assertEqual(self.player.health, 60)

        healed = self.player.heal(25)
        self.assertEqual(healed, 25)
        self.assertEqual(self.player.health, 85)

        healed_overflow = self.player.heal(50)
        self.assertEqual(healed_overflow, 15)
        self.assertEqual(self.player.health, 100)

    def test_special_attack_cooldown(self) -> None:
        """Testa a habilidade Golpe Devastador e seu tempo de recarga."""
        self.assertTrue(self.player.can_use_special())

        damage = self.player.use_special_attack()
        self.assertEqual(damage, 35)
        self.assertFalse(self.player.can_use_special())

        damage_cooldown = self.player.use_special_attack()
        self.assertEqual(damage_cooldown, 0)

        for _ in range(4):
            self.player.update_cooldowns()

        self.assertTrue(self.player.can_use_special())

    def test_engine_full_combat_flow(self) -> None:
        """Testa a fluxo do motor e notificação dos observadores."""
        engine = GameEngine()
        mock_obs = MockObserver()
        engine.subscribe(mock_obs)

        engine.start_game()
        self.assertTrue(any(e[0] == "GAME_STARTED" for e in mock_obs.events))

        engine.player_attack()
        self.assertTrue(any(e[0] == "PLAYER_ATTACKED" for e in mock_obs.events))

        engine.player_defend()
        self.assertTrue(any(e[0] == "PLAYER_DEFENDED" for e in mock_obs.events))


if __name__ == "__main__":
    unittest.main()
