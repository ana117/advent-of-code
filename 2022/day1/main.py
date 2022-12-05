def solve_1(sample=False):
    max_elf = 0
    curr_elf = 0

    file_name = "2022/day1/day1"
    if sample:
        file_name += "-sample"
    with open(f"{file_name}.txt") as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                max_elf = max(max_elf, curr_elf)
                curr_elf = 0
            else:
                curr_elf += int(line)
    return max(max_elf, curr_elf)


def solve_2(sample=False):
    file_name = "2022/day1/day1"
    if sample:
        file_name += "-sample"
    
    top_three = [0, 0, 0]
    least_calories = 0
    curr_calories = 0

    with open(f"{file_name}.txt") as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                if curr_calories > least_calories:
                    top_three.append(curr_calories)
                    top_three.sort()
                    top_three.pop(0)
                    least_calories = top_three[0]
                curr_calories = 0
            else:
                curr_calories += int(line)

    if curr_calories > least_calories:
        top_three.append(curr_calories)
        top_three.sort()
        top_three.pop(0)

    return sum(top_three)


def main():
    # print(solve_1())
    print(solve_2())


if __name__ == "__main__":
    main()