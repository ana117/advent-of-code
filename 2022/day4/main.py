def solve_1(sample=False):
    file_name = "2022/day4/day4"
    if sample:
        file_name += "-sample"

    total_contained = 0
    with open(f'{file_name}.txt') as f:
        for line in f:
            line = line.strip()

            elf_one, elf_two = line.split(',')

            elf_one_range = [int(x) for x in elf_one.split('-')]
            elf_two_range = [int(x) for x in elf_two.split('-')]

            if elf_one_range[0] > elf_two_range[0]:
                if elf_one_range[1] <= elf_two_range[1]:
                    total_contained += 1
            elif elf_two_range[0] > elf_one_range[0]:
                if elf_two_range[1] <= elf_one_range[1]:
                    total_contained += 1
            else:
                total_contained += 1

    return total_contained


def solve_2(sample=False):
    file_name = "2022/day4/day4"
    if sample:
        file_name += "-sample"

    total_overlap = 0
    with open(f'{file_name}.txt') as f:
        for line in f:
            line = line.strip()

            elf_one, elf_two = line.split(',')

            elf_one_range = [int(x) for x in elf_one.split('-')]
            elf_two_range = [int(x) for x in elf_two.split('-')]

            if elf_one_range[0] > elf_two_range[1] or \
                elf_two_range[0] > elf_one_range[1]:
                continue
            
            total_overlap += 1

    return total_overlap


def main():
    # print(solve_1())
    print(solve_2())


if __name__ == "__main__":
    main()