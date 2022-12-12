def solve_1(sample=False):
    file_name = "2022/day9/day9"
    if sample:
        file_name += "-sample"
    file_name += ".txt"
    ans = 0

    movements = []
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip()
            movements.append(line.split())

    head = [0,0]
    tail = [0,0]
    visited = {(0,0)}
    for dir, amt in movements:
        for _ in range(int(amt)):
            prev = head[:]
            if dir == 'L':
                head[0] -= 1
            elif dir == 'R':
                head[0] += 1
            elif dir == 'U':
                head[1] += 1
            elif dir == 'D':
                head[1] -= 1
            
            if abs(head[0]-tail[0]) > 1 or abs(head[1]-tail[1]) > 1:
                visited.add((prev[0], prev[1]))
                tail = prev[:]
    
    ans = len(visited)
    return ans
    


def solve_2(sample=False):
    file_name = "2022/day9/day9"
    if sample:
        file_name += "-sample"
    file_name += ".txt"
    
    ans = 0
    movements = []
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip()
            movements.append(line.split())

    head = [0,0]
    tails = [[0,0] for _ in range(9)]
    visited = {(0,0)}
    for dir, amt in movements:
        for _ in range(int(amt)):
            if dir == 'L':
                head[0] -= 1
            elif dir == 'R':
                head[0] += 1
            elif dir == 'U':
                head[1] += 1
            elif dir == 'D':
                head[1] -= 1
            curr = head[:]

            for i in range(len(tails)):
                if abs(curr[0]-tails[i][0]) <= 1 and abs(curr[1]-tails[i][1]) <= 1:
                    break

                # horizontal
                if abs(curr[0]-tails[i][0]) > 1 and curr[1] == tails[i][1]:
                    tails[i][0] += 1 if curr[0] > tails[i][0] else -1
                # vertical
                elif abs(curr[1]-tails[i][1]) > 1 and curr[0] == tails[i][0]:
                    tails[i][1] += 1 if curr[1] > tails[i][1] else -1
                # diagonal
                else:
                    tails[i][0] += 1 if curr[0] > tails[i][0] else -1
                    tails[i][1] += 1 if curr[1] > tails[i][1] else -1

                if i == len(tails)-1:
                    visited.add((tails[i][0], tails[i][1]))
                curr = tails[i][:]

    ans = len(visited)
    return ans


def main():
    print(f'Puzzle 1\nSample: {solve_1(True)}\nReal  : {solve_1()}\n')
    print(f'Puzzle 2\nSample: {solve_2(True)}\nReal  : {solve_2()}\n')


if __name__ == "__main__":
    main()