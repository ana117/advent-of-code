1560475800
"""
Write the question summary here
"""

test_data_a = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip()
test_data_b = test_data_a
test_answer_a = 50
test_answer_b = 24


def solve_a(data):
  answer = 0

  red_tiles = [
    (int(line.split(",")[0]), int(line.split(",")[1]))
    for line in data.split("\n")
  ]
  for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
      x1, y1 = red_tiles[i]
      x2, y2 = red_tiles[j]
      area = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
      if area > answer:
        answer = area

  return answer

def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"


def _get_line(a, b):
  line = set()
  x1, y1 = a
  x2, y2 = b

  a1, a2 = min(x1, x2), max(x1, x2)
  b1, b2 = min(y1, y2), max(y1, y2)
  for a in range(a1, a2 + 1):
    for b in range(b1, b2 + 1):
      line.add((a, b))
  return line

def solve_b(data):
  answer = 0

  red_tiles = [
    (int(line.split(",")[0]), int(line.split(",")[1]))
    for line in data.split("\n")
  ]
  perimeters = set()
  for i in range(1, len(red_tiles)):
    x1, y1 = red_tiles[i - 1]
    x2, y2 = red_tiles[i]
    line = _get_line((x1, y1), (x2, y2))
    perimeters |= line
  perimeters |= _get_line(red_tiles[-1], red_tiles[0])

  areas = []
  for i in range(len(red_tiles)):
    for j in range(i + 1, len(red_tiles)):
      x1, y1 = red_tiles[i]
      x2, y2 = red_tiles[j]
      area = abs(x1 - x2 + 1) * abs(y1 - y2 + 1)
      areas.append((area, (x1, y1), (x2, y2)))
  areas.sort(reverse=True, key=lambda x: x[0])

  for area, (x1, y1), (x2, y2) in areas:
    a1, a2 = min(x1, x2), max(x1, x2)
    b1, b2 = min(y1, y2), max(y1, y2)
    is_valid = True
    for ap, bp in perimeters:
      if (a1 < ap < a2) and (b1 < bp < b2):
        is_valid = False
        break
    if is_valid:
      answer = area
      break

  return answer
 
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"


if __name__ == "__main__":
  test_a()
  test_b()
