from functools import cache
import multiprocessing
from pathlib import Path
import re
from typing import Callable, Iterable


with open(Path(__file__).parent / "input.txt") as f:
    content = [line for line in f.read().splitlines() if line]
    content_str = " ".join(content)

seeds_line = content[0]
seeds = list((map(lambda x: int(x.strip()), seeds_line.split(":")[1].split())))


def process_number_line(number_line: str):
    ranges: list[tuple[int, int, int]] = []
    number_line = number_line.strip()
    numbers = tuple(map(lambda x: int(x.strip()), number_line.split()))
    for i in range(0, len(numbers), 3):
        dest_start, source_start, range_len = numbers[i : i + 3]
        ranges.append((dest_start, source_start, range_len))

    return ranges


def prepare_functions(ranges: list[tuple[int, int, int]]):
    source_to_dest: list[Callable[[int], int | None]] = []
    for r in ranges:
        dest_start, source_start, range_len = r
        source_to_dest.append(
            # default arguments required because of late binding in lambdas
            lambda x, dest_start=dest_start, source_start=source_start, range_len=range_len: dest_start
            + (x - source_start)
            if source_start <= x < (source_start + range_len)
            else None
        )

    source_to_dest.append(lambda x: x)
    return tuple(source_to_dest)


@cache
def find_value(source_to_dest: tuple[Callable[[int], int | None]], value: int) -> int:
    for func in source_to_dest:
        if ans := func(value):
            return ans

    raise ValueError(f"unable to find {value=} for {source_to_dest=}")


seed_to_soil = tuple()
soil_to_fertilizer = tuple()
fertilizer_to_water = tuple()
water_to_light = tuple()
light_to_temperature = tuple()
temperature_to_humidity = tuple()
humidity_to_location = tuple()

text_spans = [match.span() for match in re.finditer(r"\w+-to-\w+ map:", content_str)]
for i in range(len(text_spans)):
    if i == 0:
        # seed to soil
        numbers = content_str[text_spans[i][1] : text_spans[i + 1][0]]
        ranges = process_number_line(numbers)
        seed_to_soil = prepare_functions(ranges)
    elif i == 1:
        # soil to fertilizer
        numbers = content_str[text_spans[i][1] : text_spans[i + 1][0]]
        ranges = process_number_line(numbers)
        soil_to_fertilizer = prepare_functions(ranges)
    elif i == 2:
        # fertilizer to water
        numbers = content_str[text_spans[i][1] : text_spans[i + 1][0]]
        ranges = process_number_line(numbers)
        fertilizer_to_water = prepare_functions(ranges)
    elif i == 3:
        # water to light
        numbers = content_str[text_spans[i][1] : text_spans[i + 1][0]]
        ranges = process_number_line(numbers)
        water_to_light = prepare_functions(ranges)
    elif i == 4:
        # light to temp
        numbers = content_str[text_spans[i][1] : text_spans[i + 1][0]]
        ranges = process_number_line(numbers)
        light_to_temperature = prepare_functions(ranges)
    elif i == 5:
        # temp to humid
        numbers = content_str[text_spans[i][1] : text_spans[i + 1][0]]
        ranges = process_number_line(numbers)
        temperature_to_humidity = prepare_functions(ranges)
    elif i == 6:
        # humid to location
        numbers = content_str[text_spans[i][1] : len(content_str)]
        ranges = process_number_line(numbers)
        humidity_to_location = prepare_functions(ranges)


def find_min_location(seeds: Iterable[int]):
    # first set min location to max, then compare and reset it
    min_location = float("inf")

    for seed in seeds:
        soil = find_value(seed_to_soil, seed)
        fertilizer = find_value(soil_to_fertilizer, soil)
        water = find_value(fertilizer_to_water, fertilizer)
        light = find_value(water_to_light, water)
        temperature = find_value(light_to_temperature, light)
        humidity = find_value(temperature_to_humidity, temperature)
        location = find_value(humidity_to_location, humidity)
        min_location = min(min_location, location)

    return min_location


if __name__ == "__main__":
    print(find_min_location(seeds))
    seed_ranges = [range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]
    with multiprocessing.Pool() as pool:
        results = pool.map(find_min_location, seed_ranges)
    print(min(results))
