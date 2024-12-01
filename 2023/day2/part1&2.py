from dataclasses import dataclass


MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


@dataclass(order=True)
class Cube:
    red: int
    green: int
    blue: int

    def __bool__(self):
        return self.red <= MAX_RED and self.green <= MAX_GREEN and self.blue <= MAX_BLUE

    def power(self):
        return self.red * self.blue * self.green


@dataclass(frozen=True)
class Game:
    _id: int
    cubes_shown: list[Cube]

    @classmethod
    def from_string(cls, s: str):
        # * regex can be used instead of this splitting nightmare
        gameID, cube_data = s.split(":")
        gameID = int(
            gameID.split(" ")[-1]
        )  # made a mistake of getting only last digit of the whole number
        cubes: list[Cube] = list()
        for cb in cube_data.split(";"):
            by_color = map(lambda s: s.strip(), cb.strip().split(","))
            cube = Cube(0, 0, 0)
            for count_and_color in by_color:
                count, color = count_and_color.split(" ")
                exec(f"cube.{color}={count}")

            cubes.append(cube)

        return cls(gameID, cubes)

    def is_possible(self):
        return all(self.cubes_shown)

    # for part 2
    def fewest_required(self):
        max_used_red = max([c.red for c in self.cubes_shown])
        max_used_green = max([c.green for c in self.cubes_shown])
        max_used_blue = max([c.blue for c in self.cubes_shown])
        return Cube(max_used_red, max_used_green, max_used_blue)


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1 and sys.argv[1]:
        with open(sys.argv[1]) as f:
            inputs = f.read().split("\n")
    else:
        N = 5
        inputs = []
        for _ in range(5):
            inputs.append(input())

    sum_ids = 0
    sum_powers = 0
    for inp in inputs:
        if not inp.strip():
            continue
        game = Game.from_string(inp)
        if game.is_possible():
            sum_ids += game._id
        # part 2
        sum_powers += game.fewest_required().power()

    print(sum_ids)
    print(sum_powers)
