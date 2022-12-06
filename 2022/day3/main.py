def solve_1(sample=False):
    file_name = "2022/day3/day3"
    if sample:
        file_name += "-sample"

    priority_sum = 0
    with open(f'{file_name}.txt') as f:
        for line in f:
            line = line.strip()

            mid = len(line) // 2
            left_items = set(line[:mid])

            for item in line[mid:]:
                if item in left_items:
                    ordinal = ord(item)
                    if ordinal >= 65 and ordinal <= 90:  # A-Z
                        priority_sum += ordinal - 64 + 26
                    elif ordinal >= 97 and ordinal <= 122:  # a-z
                        priority_sum += ordinal - 96
                    break
    
    return priority_sum


def solve_2(sample=False):
    file_name = "2022/day3/day3"
    if sample:
        file_name += "-sample"

    priority_sum = 0
    counter = 0
    with open(f'{file_name}.txt') as f:
        rucksacks = []
        for line in f:
            line = line.strip()
            rucksacks.append(set(line))
            counter += 1

            if counter == 3:
                badge = rucksacks[0].intersection(rucksacks[1], rucksacks[2]).pop()

                ordinal = ord(badge)
                if ordinal >= 65 and ordinal <= 90:  # A-Z
                    priority_sum += ordinal - 64 + 26
                elif ordinal >= 97 and ordinal <= 122:  # a-z
                    priority_sum += ordinal - 96
                
                counter = 0
                rucksacks = []
    
    return priority_sum

def main():
    # print(solve_1())
    print(solve_2())


if __name__ == "__main__":
    main()