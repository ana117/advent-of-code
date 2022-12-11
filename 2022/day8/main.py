from tools1 import is_visible
from tools2 import count_visible


def solve_1(sample=False):
    file_name = "2022/day8/day8"
    if sample:
        file_name += "-sample"
    
    ans = 0
    grid = []
    with open(f'{file_name}.txt') as f:
        for line in f.readlines():
            line = line.strip()
            grid.append([int(x) for x in line])


    dp = [[[-1,-1,-1,-1] for _ in range(len(grid[0]))] for _ in range(len(grid))]

    ans = 2 * len(grid) + 2 * len(grid[0]) - 4
    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            if is_visible(grid, i, j, dp):
                ans += 1

    return ans
    


def solve_2(sample=False):
    file_name = "2022/day8/day8"
    if sample:
        file_name += "-sample"
    
    ans = 0
    grid = []
    with open(f'{file_name}.txt') as f:
        for line in f.readlines():
            line = line.strip()
            grid.append([int(x) for x in line])


    for i in range(1, len(grid)-1):
        for j in range(1, len(grid[i])-1):
            ans = max(ans, count_visible(grid, i, j))

    return ans


def main():
    print(f'Puzzle 1\nSample: {solve_1(True)}\nReal  : {solve_1()}\n')
    print(f'Puzzle 2\nSample: {solve_2(True)}\nReal  : {solve_2()}\n')


if __name__ == "__main__":
    main()