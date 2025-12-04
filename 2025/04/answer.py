
"""
Write the question summary here
"""

test_data_a = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()
test_data_b = test_data_a
test_answer_a = 13
test_answer_b = 43


def solve_a(data):
  answer = 0

  grid = [list(line) for line in data.splitlines()]
  rows = len(grid)
  cols = len(grid[0])
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] != '@':
        continue
      
      adjacent_count = 0
      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
          adjacent_count += 1

      if adjacent_count < 4:
        answer += 1

  return answer

def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"


def solve_b(data):
  answer = 0

  grid = [list(line) for line in data.splitlines()]
  rows = len(grid)
  cols = len(grid[0])
  
  while True:
    found = False
    for r in range(rows):
      for c in range(cols):
        if grid[r][c] != '@':
          continue
        
        adjacent_count = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
          nr, nc = r + dr, c + dc
          if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
            adjacent_count += 1

        if adjacent_count < 4:
          answer += 1
          grid[r][c] = '.'
          found = True

    if not found:
      break

  return answer
 
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"


if __name__ == "__main__":
  test_a()
  test_b()
