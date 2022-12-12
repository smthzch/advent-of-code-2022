"""
Elf plays
    A: rock
    B: paper
    C: scissors

You play
    X: rock
    Y: paper
    Z: scissors
"""

# map the play you make to the score for a match
play_scores = {
    'x': 1,
    'y': 2,
    'z': 3
}

# scores for lose, draw, win, for the combinations of plays
outcome_scores = {
    'ax': 3,
    'ay': 6,
    'az': 0,
    'bx': 0,
    'by': 3,
    'bz': 6,
    'cx': 6,
    'cy': 0,
    'cz': 3
}
   

def get_score1(pth):
    total_score = 0
    with open(pth, 'r') as rdr:
        for line in rdr:
            elf, you = [x.strip().lower() for x in line.split(' ')]
            total_score += outcome_scores[elf + you] + play_scores[you]
    return total_score

# for part two, translate the game outcome to which play to make
toplay = {
    'ax': 'z',
    'ay': 'x',
    'az': 'y',
    'bx': 'x',
    'by': 'y',
    'bz': 'z',
    'cx': 'y',
    'cy': 'z',
    'cz': 'x'
}

def get_score2(pth):
    total_score = 0
    with open(pth, 'r') as rdr:
        for line in rdr.readlines():
            elf, you = [x.strip().lower() for x in line.split(' ')]
            play = toplay[elf + you]
            total_score += outcome_scores[elf + play] + play_scores[play]
    return total_score
