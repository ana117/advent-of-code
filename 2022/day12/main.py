# ord(a) = 97 | ord(z) = 122
# ord(S) = 83 | ord(E) = 69


import sys


def solve_1(sample=False):
    file_name = "2022/day12/day12"
    if sample:
        file_name += "-sample"
    file_name += ".txt"

    ans = 0
    grid = []
    start = []
    end = []
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip()
            tmp = []
            for c in line:
                if c == "S":
                    start = [len(grid), len(tmp)]
                elif c == "E":
                    end = [len(grid), len(tmp)]
                tmp.append(ord(c))
            grid.append(tmp)

    
    d = [[sys.maxsize for _ in range(len(grid[0]))] for _ in range(len(grid))]
    d[end[0]][end[1]] = 0

    return ans
    


def solve_2(sample=False):
    file_name = "2022/day12/day12"
    if sample:
        file_name += "-sample"
    file_name += ".txt"
    
    ans = 0
    return ans


def main():
    print(f'Puzzle 1\nSample: {solve_1(True)}\nReal  : \n')
    print(f'Puzzle 2\nSample: {solve_2(True)}\nReal  : {solve_2()}\n')


if __name__ == "__main__":
    main()