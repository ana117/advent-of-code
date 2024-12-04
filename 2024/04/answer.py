
"""
She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, 
or even overlapping other words - you need to find all of them.
"""
              
test_data = """
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
""".strip()
test_answer_a = 18
test_answer_b = 9


TARGET_WORD = "XMAS"

def _check_horizontal(grid, i, j, target):
  if j + len(target) > len(grid[0]):
    return False
  
  word = "".join(grid[i][j:j+len(target)])
  return word == target or word == target[::-1]

def _check_vertical(grid, i, j, target):
  if i + len(target) > len(grid):
    return False
  
  word = "".join([grid[i+k][j] for k in range(len(target))])
  return word == target or word == target[::-1]

def _check_diagonal_up_right(grid, i, j, target):
  if i - len(target) + 1 < 0 or j + len(target) > len(grid[0]):
    return False
  word = "".join([grid[i-k][j+k] for k in range(len(target))])
  return word == target or word == target[::-1]
  
def _check_diagonal_down_right(grid, i, j, target):
  if i + len(target) > len(grid) or j + len(target) > len(grid[0]):
    return False
  word = "".join([grid[i+k][j+k] for k in range(len(target))])
  return word == target or word == target[::-1]

CHECKERS = [_check_horizontal, _check_vertical, _check_diagonal_up_right, _check_diagonal_down_right]

def _check_cross(grid, i, j, target):
  if i + 2 >= len(grid):
    return False

  down_right_match = _check_diagonal_down_right(grid, i, j, target)
  up_right_match = _check_diagonal_up_right(grid, i+2, j, target)
  return down_right_match and up_right_match

                                        
def solve_a(data):
  answer = 0

  grid = [list(row) for row in data.strip().split("\n")]
  n = len(grid)
  for i in range(n):
    for j in range(n):
      for checker in CHECKERS:
        if checker(grid, i, j, TARGET_WORD):
          answer += 1

  return answer
              
def test_a():
  answer = solve_a(test_data)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}\n"
              
def solve_b(data):
  answer = 0

  grid = [list(row) for row in data.strip().split("\n")]
  n = len(grid)
  for i in range(n):
    for j in range(n):
      if _check_cross(grid, i, j, TARGET_WORD[1:]):
        answer += 1
          
  return answer
              
def test_b():
  answer = solve_b(test_data)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}\n"

if __name__ == "__main__":
  test_a()
  test_b()
