def solve_1(sample=False):
    file_name = "2022/day10/day10"
    if sample:
        file_name += "-sample"
    file_name += ".txt"
    ans = 0

    cycle = 0
    x = 1
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            data = line.split()

            if data[0] == 'addx':
                for _ in range(2):
                    cycle += 1
                    if cycle == 20 or (cycle-20)%40 == 0:
                        ans += x * cycle
                x += int(data[1])
            else:
                cycle += 1
                if cycle == 20 or (cycle-20)%40 == 0:
                    ans += x * cycle

    return ans
    


def solve_2(sample=False):
    file_name = "2022/day10/day10"
    if sample:
        file_name += "-sample"
    file_name += ".txt"
    ans = [""]

    cycle = 0
    x = 1
    sprite_size = 3
    crt = ""
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            data = line.split()

            if data[0] == 'addx':
                for _ in range(2):
                    cycle += 1
                    if cycle >= x and cycle < (x + sprite_size):
                        crt += "#"
                    else:
                        crt += "."

                    if cycle % 40 == 0:
                        ans.append(crt)
                        crt = ""
                        cycle = 0
                x += int(data[1])

            else:
                cycle += 1
                if cycle >= x and cycle < (x + sprite_size):
                    crt += "#"
                else:
                    crt += "."

                if cycle % 40 == 0:
                    ans.append(crt)
                    crt = ""
                    cycle = 0

    return "\n".join(ans)


def main():
    print(f'Puzzle 1\nSample: {solve_1(True)}\nReal  : {solve_1()}\n')
    print(f'Puzzle 2\nSample: {solve_2(True)}\n\nReal  : {solve_2()}\n')


if __name__ == "__main__":
    main()