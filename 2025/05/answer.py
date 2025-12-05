
"""
Write the question summary here
"""

test_data_a = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()
test_data_b = test_data_a
test_answer_a = 3
test_answer_b = 14


def solve_a(data):
  answer = 0

  ranges, ingredients = data.split("\n\n")

  fresh_ids = {}
  for line in ranges.splitlines():
    start, end = map(int, line.split("-"))
    for s, e in fresh_ids.items():
      if not (end < s or start > e):
        start = min(start, s)
        end = max(end, e)
        del fresh_ids[s]
        break
    fresh_ids[start] = end

  for line in ingredients.splitlines():
    ingredient_id = int(line)
    for s, e in fresh_ids.items():
      if s <= ingredient_id <= e:
        answer += 1
        break

  return answer

def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"


def solve_b(data):
  answer = 0

  ranges, _ = data.split("\n\n")
  
  fresh_ids = []
  for line in ranges.splitlines():
    start, end = map(int, line.split("-"))
    fresh_ids.append((start, end))

  has_changes = True
  while has_changes:
    has_changes = False
    for i in range(len(fresh_ids)):
      s1, e1 = fresh_ids[i]
      for j in range(i + 1, len(fresh_ids)):
        s2, e2 = fresh_ids[j]
        if not (e1 < s2 or e2 < s1):
          new_start = min(s1, s2)
          new_end = max(e1, e2)
          fresh_ids[i] = (new_start, new_end)
          del fresh_ids[j]
          has_changes = True
          break
      if has_changes:
        break

  for s, e in fresh_ids:
    answer += e - s + 1

  return answer
 
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"


if __name__ == "__main__":
  test_a()
  test_b()
