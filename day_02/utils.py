from dataclasses import dataclass


@dataclass
class Game:
    id: int
    cubes: dict

    @property
    def power(self):
        return self.cubes.get('red').get('max') * self.cubes.get('green').get('max') * self.cubes.get('blue').get('max')

    @staticmethod
    def from_line(line: str):
        splitted = line.split(':')
        _id_str, _sets_str = splitted[0], splitted[-1]
        id = int(_id_str.split(' ')[-1])

        cubes = {
            'red': {
                'max': 0,
            },
            'green': {
                'max': 0,
            },
            'blue': {
                'max': 0,
            }
        }
        sets = _sets_str.split(';')

        for _set in sets:
            cube_data = _set.strip().split(', ')

            for cube in cube_data:
                split_cube = cube.split(' ')

                color = split_cube[-1]
                value = int(split_cube[0])

                if value > cubes[color]['max']:
                    cubes[color]['max'] = value

        return Game(
            id=id,
            cubes=cubes,
        )
