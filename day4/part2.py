from functools import cache


with open("./input.txt") as f:
    content = f.read().splitlines()

# content = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """.splitlines()


@cache
def get_card_winning_count(line: str):
    card, data = line.split(":")
    card_num = int(card.split(" ")[-1])
    winning, possession = data.split("|")
    winning_cards = set((int(i) for i in winning.strip().split() if i.strip()))
    possession_cards = set((int(i) for i in possession.strip().split() if i.strip()))

    count = len(possession_cards.intersection(winning_cards))

    return card_num, count


scratchcards = content.copy()
max_count = len(scratchcards)
pos = 0
while pos < max_count:
    card_num, count = get_card_winning_count(scratchcards[pos])
    for j in range(card_num + 1, card_num + 1 + count):
        scratchcards.append(content[j - 1])
    pos += 1
    max_count += count
    # scratchcards.sort()

print(max_count)
