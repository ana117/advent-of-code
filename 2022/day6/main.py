def solve_1(sample=False):
    file_name = "2022/day6/day6"
    if sample:
        file_name += "-sample"
    
    ans = -1
    with open(f'{file_name}.txt') as f:
        line = f.read().strip()

        markers = ""
        for i in range(len(line)):
            if line[i] in markers:
                markers = markers[markers.index(line[i])+1:]

            markers += line[i]
            if len(markers) == 4:
                ans = i+1
                break
    
    return ans
    


def solve_2(sample=False):
    file_name = "2022/day6/day6"
    if sample:
        file_name += "-sample"
    
    ans = -1
    with open(f'{file_name}.txt') as f:
        line = f.read().strip()

        markers = ""
        for i in range(len(line)):
            if line[i] in markers:
                markers = markers[markers.index(line[i])+1:]

            markers += line[i]
            if len(markers) == 14:
                ans = i+1
                break
    
    return ans


def main():
    print(f'Puzzle 1\nSample: {solve_1(True)}\nReal  : {solve_1()}\n')
    print(f'Puzzle 2\nSample: {solve_2(True)}\nReal  : {solve_2()}\n')


if __name__ == "__main__":
    main()