from unittest import TestCase
from day_02.part_01 import solve as solve_part_1, Game
from day_02.part_02 import solve as solve_part_2


class TestDay02(TestCase):
    def setUp(self) -> None:
        self.input_values_01 = [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
        ]
        self.input_values_02 = []

    def test_part_01(self):
        assert solve_part_1(self.input_values_01) == 8

    def test_game_from_line(self):
        game = Game.from_line('Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green')
        assert game.power == 48

    def test_part_02(self):
        assert solve_part_2(self.input_values_01) == 2286
