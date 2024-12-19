from functools import lru_cache


"""
Write the question summary here
"""
              
test_data_a = """
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
""".strip()
test_data_b = test_data_a
test_answer_a = 6
test_answer_b = 16
              

def _helper_a(design, towels):
  if design in towels:
    return True
  
  for i in range(1, len(design)):
    if design[:i] in towels and _helper_a(design[i:], towels):
      return True
  return False

def _helper_b(design, towels, cache):
  if design in cache:
    return cache[design]

  arrangements = 0
  if design in towels:
    arrangements += 1

  for i in range(1, len(design)):
    left = design[:i]
    right = design[i:]
    if left in towels:
      arrangements += _helper_b(right, towels, cache)

  cache[design] = arrangements
  return arrangements


def solve_a(data):
  answer = 0

  towels, designs = data.split("\n\n")
  towels = set(towels.split(", "))
  designs = designs.split("\n")

  for design in designs:
    if _helper_a(design, towels):
      answer += 1

  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  towels, designs = data.split("\n\n")
  towels = set(towels.split(", "))
  designs = designs.split("\n")

  towels = frozenset(towels)
  for design in designs:
    answer += _helper_b(design, towels, {})

  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
