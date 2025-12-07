
"""
Write the question summary here
"""

test_data_a = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip()
test_data_b = test_data_a
test_answer_a = 21
test_answer_b = 40


def solve_a(data):
  answer = 0

  grid = [list(line) for line in data.splitlines()]
  rows = len(grid)
  cols = len(grid[0])

  beams = set()
  for c in range(cols):
    if grid[0][c] == 'S':
      beams.add((1, c))
      break

  current_row = 2
  while current_row < rows:
    new_beams = set()
    
    for r, c in beams:
      if grid[current_row][c] == '^':
        answer += 1
        if c + 1 < cols:
          new_beams.add((current_row + 1, c + 1))
        if c - 1 >= 0:
          new_beams.add((current_row + 1, c - 1))
      else:
        new_beams.add((current_row + 1, c))
    beams = new_beams
    current_row += 1

  return answer

def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"


def solve_b(data):
  answer = 0

  grid = [list(line) for line in data.splitlines()]
  rows = len(grid)
  cols = len(grid[0])

  results = {r: 0 for r in range(rows+1)}
  beams = list()
  for c in range(cols):
    if grid[0][c] == 'S':
      beams.append(c)
      results[c] += 1
      break

  current_row = 2
  while current_row < rows:
    curr_results = {r: 0 for r in range(rows+1)}
    for c in beams:
      if grid[current_row][c] == '^':
        if c + 1 < cols:
          curr_results[c + 1] += results[c]
        if c - 1 >= 0:
          curr_results[c - 1] += results[c]
      else:
        curr_results[c] += results[c]
      results[c] = 0

    results = curr_results
    beams = [c for c in range(cols) if results[c] > 0]
    current_row += 2

  answer = sum(results.values())

  return answer
 
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"


if __name__ == "__main__":
  test_a()
  test_b()
