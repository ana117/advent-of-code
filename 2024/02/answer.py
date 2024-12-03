"""
So, a report only counts as safe if both of the following are true:
  - The levels are either all increasing or all decreasing.
  - Any two adjacent levels differ by at least one and at most three.

Example:
  7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
  1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
  9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
  1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
  8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
  1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
"""

test_data = """
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
""".strip()
test_answer_a = 2
test_answer_b = 4


def _is_safe(level):
  is_increasing = level[0] < level[1]
  for i in range(len(level)-1):
    gap = abs(level[i] - level[i+1])

    if gap < 1 or gap > 3:
      return False
    if (is_increasing and level[i] >= level[i+1]) or (not is_increasing and level[i] <= level[i+1]):
      return False
  return True

def solve_a(data):
  answer = 0
  levels = [
    [int(level) for level in line.split()]
    for line in data.split("\n")
  ]
  
  for level in levels:
    if _is_safe(level):
      answer += 1
      
  return answer

def test_a():
  answer = solve_a(test_data)
  assert answer == test_answer_a, f"expected {test_answer_a} but got {answer}"


def solve_b(data):
  answer = 0
  levels = [
    [int(level) for level in line.split()]
    for line in data.split("\n")
  ]
  
  for level in levels:
    if _is_safe(level):
      answer += 1
    else:
      for i in range(len(level)):
        if _is_safe(level[:i] + level[i+1:]):
          answer += 1
          break

  return answer

def test_b():
  answer = solve_b(test_data)
  assert answer == test_answer_b, f"expected {test_answer_b} but got {answer}"
