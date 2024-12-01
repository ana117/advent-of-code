"""
Pair up the smallest number in the left list with the smallest number in the right list, 
then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; 
you'll need to add up all of those distances.
"""

test_data = """
3   4
4   3
2   5
1   3
3   9
3   3
""".strip()
test_answer_a = 11
test_answer_b = 31


def solve_a(data):
  nums = [int(x) for x in data.split()]
  left = sorted(nums[::2])
  right = sorted(nums[1::2])

  return sum(abs(l - r) for l, r in zip(left, right))

def test_a():
  assert solve_a(test_data) == test_answer_a, f"expected {test_answer_a} but got {solve_a(test_data)}"


def solve_b(data):
  nums = [int(x) for x in data.split()]
  left = sorted(nums[::2])
  right = sorted(nums[1::2])

  memory = {"left": {}, "right": {}}
  for r in right:
    memory["right"][r] = memory["right"].get(r, 0) + 1
  
  answer = 0
  for l in left:
    if l not in memory["left"]:
      memory["left"][l] = l * memory["right"].get(l, 0)
    answer += memory["left"][l]

  return answer

def test_b():
  assert solve_b(test_data) == test_answer_b, f"expected {test_answer_b} but got {solve_b(test_data)}"
