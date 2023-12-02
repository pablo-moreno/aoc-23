from unittest import TestCase
from .part_01 import solve as solve_part_1
from .part_02 import solve as solve_part_2

class TestDay01(TestCase):
    def setUp(self) -> None:
        self.input_values_01 = [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet",
        ]
        self.input_values_02 = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen",
        ]

    def test_part_01(self):
        assert solve_part_1(self.input_values_01) == 142

    def test_part_02(self):
        assert solve_part_2(self.input_values_02) == 281
