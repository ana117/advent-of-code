"""
Codes:
- Rock = A, X
- Paper = B, Y
- Scissors = C, Z

Scores:
- Rock = 1
- Paper = 2
- Scissors = 3

- Lose = 0
- Draw = 3
- Win = 6
"""

points = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
    "win": 6,
    "draw": 3,
    "lose": 0,
}

my_results = {
        "X": {
            "A": "draw",
            "B": "lose",
            "C": "win",
        },
        "Y": {
            "A": "win",
            "B": "draw",
            "C": "lose",
        },
        "Z": {
            "A": "lose",
            "B": "win",
            "C": "draw",
        },
    }


def solve_1(sample=False):
    file_name = "2022/day2/day2"
    if sample:
        file_name += "-sample"

    total_score = 0
    with open(f"{file_name}.txt") as f:
        for line in f:
            line = line.strip()
            enemy, me = line.split(" ")

            total_score += points[my_results[me][enemy]]
            total_score += points[me]

    return total_score


def solve_2(sample=False):
    file_name = "2022/day2/day2"
    if sample:
        file_name += "-sample"

    my_output = {
        "X": {
            "A": "Z",
            "B": "X",
            "C": "Y",
        },
        "Y": {
            "A": "X",
            "B": "Y",
            "C": "Z",
        },
        "Z": {
            "A": "Y",
            "B": "Z",
            "C": "X",
        },
    }

    total_score = 0
    with open(f"{file_name}.txt") as f:
        for line in f:
            line = line.strip()
            enemy, me = line.split(" ")
            me = my_output[me][enemy]

            total_score += points[my_results[me][enemy]]
            total_score += points[me]

    return total_score

def main():
    # print(solve_1())
    print(solve_2())


if __name__ == "__main__":
    main()