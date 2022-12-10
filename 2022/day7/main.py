def count_total_size(directories, directory_sizes, curr_dir):
    if directory_sizes[curr_dir] != -1:
        return directory_sizes[curr_dir]

    total_size = 0
    for item in directories[curr_dir]:
        if isinstance(item, int):
            total_size += item
        else:
            total_size += count_total_size(directories, directory_sizes, item)
    directory_sizes[curr_dir] = total_size
    return total_size

def solve_1(sample=False):
    file_name = "2022/day7/day7"
    if sample:
        file_name += "-sample"
    
    ans = 0

    directories = {}
    curr_path = []
    with open(f'{file_name}.txt') as f:
        for line in f.readlines():
            line = line.strip()
            data = line.split()

            if data[0] == '$':
                if data[1] == 'cd':
                    if data[2] == '..':
                        curr_path.pop()
                    else:
                        curr_path.append(data[2])
            
            # ls / files / directory
            else:
                curr_dir = '/'.join(curr_path)
                if data[0] == 'dir':
                    to_add = curr_dir + '/' + data[1]
                else:
                    to_add = int(data[0])

                if curr_dir not in directories:
                    directories[curr_dir] = []
                directories[curr_dir].append(to_add)
    
    
    directory_sizes = {}
    for directory in directories:
        directory_sizes[directory] = -1
    
    for directory in directories:
        count_total_size(directories, directory_sizes, directory)

    for directory in directory_sizes:
        if directory_sizes[directory] <= 100000:
            ans += directory_sizes[directory]

    return ans
    


def solve_2(sample=False):
    file_name = "2022/day7/day7"
    if sample:
        file_name += "-sample"
    

    directories = {}
    curr_path = []
    with open(f'{file_name}.txt') as f:
        for line in f.readlines():
            line = line.strip()
            data = line.split()

            if data[0] == '$':
                if data[1] == 'cd':
                    if data[2] == '..':
                        curr_path.pop()
                    else:
                        curr_path.append(data[2])
            
            # ls / files / directory
            else:
                curr_dir = '/'.join(curr_path)
                if data[0] == 'dir':
                    to_add = curr_dir + '/' + data[1]
                else:
                    to_add = int(data[0])

                if curr_dir not in directories:
                    directories[curr_dir] = []
                directories[curr_dir].append(to_add)
    
    
    directory_sizes = {}
    for directory in directories:
        directory_sizes[directory] = -1
    
    for directory in directories:
        count_total_size(directories, directory_sizes, directory)

    max_size = 70_000_000
    total_size = directory_sizes['/']
    curr_free = max_size - total_size
    size_to_delete = 30000000 - curr_free
    
    ans = 0
    for directory in directory_sizes:
        if directory_sizes[directory] >= size_to_delete:
            if ans == 0 or directory_sizes[directory] < ans:
                ans = directory_sizes[directory]

    return ans


def main():
    print(f'Puzzle 1\nSample: {solve_1(True)}\nReal  : {solve_1()}\n')
    print(f'Puzzle 2\nSample: {solve_2(True)}\nReal  : {solve_2()}\n')


if __name__ == "__main__":
    main()