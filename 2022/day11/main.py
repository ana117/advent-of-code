class Monkey:
    monkeys = {}
    mod_num = 1
    def __init__(self, monkey_num, items, op, test, target, worry_divider):
        self.monkey_num = monkey_num
        self.items = items
        self.op = op
        self.test = test
        self.target = target
        self.amount = 0
        self.worry_divider = worry_divider

        Monkey.monkeys[monkey_num] = self
        Monkey.mod_num *= self.test
    
    def inspect(self):
        for item in self.items:
            self.amount += 1
            worry_level = self.operation(item) // self.worry_divider
            if self.worry_divider == 1:
                worry_level = worry_level % Monkey.mod_num
            self.throw_item(worry_level)
        self.items = []

    
    def operation(self, worry_level):
        try:
            num = int(self.op[1])
        except ValueError:
            num = worry_level

        if self.op[0] == "+":
            worry_level += num
        elif self.op[0] == "*":
            worry_level *= num
        elif self.op[0] == "-":
            worry_level -= num
        elif self.op[0] == "/":
            worry_level //= num
        return worry_level
    
    def throw_item(self, worry_level):
        if worry_level % self.test == 0:
            target_monkey = self.target[0]
        else:
            target_monkey = self.target[1]
        Monkey.monkeys[target_monkey].items.append(worry_level)

    def __str__(self):
        return f"{self.monkey_num} {self.items}"


def create_monkey(datas, worry_divider):
    name = datas[0].split(" ")[1][0].strip()
    items = [int(x) for x in datas[1].split(":")[1].split(",")]
    op = (datas[2].split(" ")[-2], datas[2].split(" ")[-1])
    test = int(datas[3].split("by")[1])
    targets = (datas[4].split("monkey")[1].strip(), datas[5].split("monkey")[1].strip())

    monkey = Monkey(name, items, op, test, targets, worry_divider)
    return monkey
        


def solve_1(sample=False):
    file_name = "2022/day11/day11"
    if sample:
        file_name += "-sample"
    file_name += ".txt"

    monkeys = []
    datas = []
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                monkeys.append(create_monkey(datas, 3))
                datas = []
            else:
                datas.append(line)
        monkeys.append(create_monkey(datas, 3))
  

    for _ in range(20):
        for monkey in monkeys:
            monkey.inspect()
    
    ans = sorted(monkeys, key=lambda x: x.amount, reverse=True)[:2]

    return ans[0].amount * ans[1].amount
    


def solve_2(sample=False):
    file_name = "2022/day11/day11"
    if sample:
        file_name += "-sample"
    file_name += ".txt"

    monkeys = []
    datas = []
    with open(file_name) as f:
        for line in f.readlines():
            line = line.strip()
            if len(line) == 0:
                monkeys.append(create_monkey(datas, 1))
                datas = []
            else:
                datas.append(line)
        monkeys.append(create_monkey(datas, 1))
  
    for _ in range(10000):
        for monkey in monkeys:
            monkey.inspect()
    
    ans = sorted(monkeys, key=lambda x: x.amount, reverse=True)[:2]

    return ans[0].amount * ans[1].amount


def main():
    print(f'Puzzle 1\nSample: {solve_1(True)}\nReal  : {solve_1()}\n')
    print(f'Puzzle 2\nSample: {solve_2(True)}\nReal  : {solve_2()}\n')


if __name__ == "__main__":
    main()