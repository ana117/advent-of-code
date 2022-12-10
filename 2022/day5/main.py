def solve_1(sample=False):
    file_name = "2022/day5/day5"
    if sample:
        file_name += "-sample"

    stacks = {}

    movements = []
    is_initial = True
    max_stacks = 0

    with open(file_name + '.txt') as f:
        for line in f:
            if len(line.strip()) == 0:
                is_initial = False
                continue
            
            if is_initial:
                counter = 1
                for i in range(1, len(line), 4):
                    if (line[i] >= "A") and (line[i] <= "Z"):
                        max_stacks = max(max_stacks, counter)
                        if str(counter) not in stacks.keys():
                            stacks[str(counter)] = [line[i]]
                        else:
                            stacks[str(counter)].append(line[i])
                    counter += 1
                    
            else:
                line = line.strip()
                splitted = line.split()
                amount, src, dst = splitted[1], splitted[3], splitted[5]
                movements.append((amount, src, dst))
    
    for key in stacks:
        stacks[key] = stacks[key][::-1]
    
    for amount, src, dst in movements:
        for _ in range(int(amount)):
            stacks[dst].append(stacks[src].pop())
    
    ans = ""
    for i in range(max_stacks):
        ans += stacks[str(i+1)].pop()
    
    return ans


def solve_2(sample=False):
    file_name = "2022/day5/day5"
    if sample:
        file_name += "-sample"

    stacks = {}

    movements = []
    is_initial = True
    max_stacks = 0

    with open(file_name + '.txt') as f:
        for line in f:
            if len(line.strip()) == 0:
                is_initial = False
                continue
            
            if is_initial:
                counter = 1
                for i in range(1, len(line), 4):
                    if (line[i] >= "A") and (line[i] <= "Z"):
                        max_stacks = max(max_stacks, counter)
                        if str(counter) not in stacks.keys():
                            stacks[str(counter)] = [line[i]]
                        else:
                            stacks[str(counter)].append(line[i])
                    counter += 1
                    
            else:
                line = line.strip()
                splitted = line.split()
                amount, src, dst = splitted[1], splitted[3], splitted[5]
                movements.append((amount, src, dst))
    
    for key in stacks:
        stacks[key] = stacks[key][::-1]
    
    for amount, src, dst in movements:
        tmp = []
        for _ in range(int(amount)):
            tmp.append(stacks[src].pop()) 
        stacks[dst].extend(tmp[::-1])
    
    ans = ""
    for i in range(max_stacks):
        ans += stacks[str(i+1)].pop()
    
    return ans


def main():
    # print(solve_1())
    print(solve_2())


if __name__ == "__main__":
    main()