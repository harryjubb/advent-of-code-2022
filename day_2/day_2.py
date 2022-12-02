# Part 1:

# What would your total score be if everything goes exactly according to
# your strategy guide?

# Opponent:
# A = rock, B = paper, C = scissors
# You:
# X = rock, Y = paper, Z = scissors

ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
LOSS = 0
DRAW = 3

SHAPE_POINTS_MAP = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

PLAY_POINTS_MAP = {
    "AX": DRAW,
    "AY": WIN,
    "AZ": LOSS,
    "BX": LOSS,
    "BY": DRAW,
    "BZ": WIN,
    "CX": WIN,
    "CY": LOSS,
    "CZ": DRAW,
}

def points_for_play(play: str):
    """Calculate the points that would be earned for a given play"""

    return SHAPE_POINTS_MAP[play[1]] + PLAY_POINTS_MAP[play]

with open("./input.txt", "r") as fo:
    strategy = [line.strip().replace(" ", "") for line in fo.readlines()]

total_points = sum([points_for_play(play) for play in strategy])

assert total_points == 10404

print("Part 1:", total_points)

# Part 2

# X means you need to lose, Y means you need to end the round in a draw,
# and Z means you need to win
STRATEGY_TO_PLAY = {
    "AX": "AZ",
    "AY": "AX",
    "AZ": "AY",
    "BX": "BX",
    "BY": "BY",
    "BZ": "BZ",
    "CX": "CY",
    "CY": "CZ",
    "CZ": "CX",
}

revised_total_points = sum([
    points_for_play(STRATEGY_TO_PLAY[play])
    for play in strategy
])

print("Part 2:", revised_total_points)

assert revised_total_points == 10334