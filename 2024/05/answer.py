
"""
The notation X|Y means that if both page number X and page number Y are to be produced 
as part of an update, page number X must be printed at some point before page number Y.

The first section specifies the page ordering rules, one per line. 
The first rule, 47|53, means that if an update includes both page number 47 and page number 53, 
then page number 47 must be printed at some point before page number 53.

The second section specifies the page numbers of each update. Because most safety manuals are different, 
the pages needed in the updates are different too. 
The first update, 75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29.

To get the printers going as soon as possible, start by identifying which updates are already in the right order.
For some reason, the Elves also need to know the middle page number of each update being printed (sum it up).
"""
              
test_data_a = """
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
""".strip()
test_data_b = test_data_a
test_answer_a = 143
test_answer_b = 123


def _parse_rules(rule_string):
  rules = {}
  for line in rule_string.split("\n"):
    a, b = line.split("|")
    if a not in rules:
      rules[a] = set()
    rules[a].add(b)

  return rules

def solve_a(data):
  answer = 0
  rule_string, update_string = data.split("\n\n")
  rules = _parse_rules(rule_string)

  for update in update_string.split("\n"):
    seen = set()
    pages = update.split(",")
    for i in range(len(pages)):
      page = pages[i]
      if page in rules and rules[page].intersection(seen):
        break
      seen.add(page)
    else:
      mid = len(pages) // 2
      answer += int(pages[mid])

  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  rule_string, update_string = data.split("\n\n")
  rules = _parse_rules(rule_string)
  
  invalids = []
  for update in update_string.split("\n"):
    seen = set()
    for page in update.split(","):
      if page in rules and rules[page].intersection(seen):
        invalids.append(update)
        break
      seen.add(page)

  for invalid in invalids:
    pages = invalid.split(",")
    is_invalid = True
    while is_invalid:
      is_invalid = False
      for i in range(len(pages) - 1):
        a, b = pages[i], pages[i + 1]
        if a in rules and b in rules[a]:
          pages[i], pages[i + 1] = b, a
          is_invalid = True
          break
    mid = len(pages) // 2
    answer += int(pages[mid])

  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
