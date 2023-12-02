"""
--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

What is the sum of all of the calibration values?

"""
import re
from typing import List

named_digits_regex = r'(?=(one|two|three|four|five|six|seven|eight|nine|\d))'


number_mapping = {
    'one': 1, 'two': 2, 'three': 3,
    'four': 4, 'five': 5, 'six': 6,
    'seven': 7, 'eight': 8, 'nine': 9,
}


def solve(values: List[str]) -> int:
    total = 0

    for line in values:
        total += _get_calibration_value_from_line(line)

    return total


def _parse_number(number: str) -> str:
    try:
        return str(int(number))
    except ValueError:
        return str(number_mapping.get(number))


def _get_calibration_value_from_line(line: str) -> int:
    digits = re.findall(named_digits_regex, line)
    value_str = ''.join([
        _parse_number(digits[0]),
        _parse_number(digits[-1]),
    ])

    return int(value_str)


if __name__ == '__main__':
    filename = 'input.txt'
    with open(filename) as f:
        values = f.readlines()
        result = solve(values)
        print(result)
