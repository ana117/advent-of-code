
"""
Based on un-scorched scraps of the book, you determine that a good hiking trail is as long as possible 
and has an even, gradual, uphill slope. 
For all practical purposes, this means that a hiking trail is any path that starts at height 0, ends at height 9, 
and always increases by a height of exactly 1 at each step. 
Hiking trails never include diagonal steps - only up, down, left, or right (from the perspective of the map).
"""
              
test_data_a = """
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
""".strip()
test_data_b = test_data_a
test_answer_a = 36
test_answer_b = 81
              

def _hike(grid, i, j, visited):
  if (i, j) in visited:
    return 0
  
  visited.add((i, j))
  if grid[i][j] == "9":
    return 1
  
  next = str(int(grid[i][j]) + 1)
  score = 0

  if i > 0 and grid[i-1][j] == next:
    score += _hike(grid, i-1, j, visited)
  if i < len(grid) - 1 and grid[i+1][j] == next:
    score += _hike(grid, i+1, j, visited)
  if j > 0 and grid[i][j-1] == next:
    score += _hike(grid, i, j-1, visited)
  if j < len(grid[0]) - 1 and grid[i][j+1] == next:
    score += _hike(grid, i, j+1, visited)

  return score

def solve_a(data):
  answer = 0

  grid = [list(row) for row in data.split("\n")]
  n = len(grid)
  m = len(grid[0])
  trailheads = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == "0"]
  for i, j in trailheads:
    answer += _hike(grid, i, j, set())

  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"


def _hike_2(grid, i, j, visited, path, paths):
  next = str(int(grid[i][j]) + 1)
  score = 0

  visited.add((i, j))
  path += f"{i}{j}"
  if grid[i][j] == "9" and path not in paths:
    paths.add(path)
    return 1

  if i > 0 and grid[i-1][j] == next:
    score += _hike_2(grid, i-1, j, visited, path, paths)
  if i < len(grid) - 1 and grid[i+1][j] == next:
    score += _hike_2(grid, i+1, j, visited, path, paths)
  if j > 0 and grid[i][j-1] == next:
    score += _hike_2(grid, i, j-1, visited, path, paths)
  if j < len(grid[0]) - 1 and grid[i][j+1] == next:
    score += _hike_2(grid, i, j+1, visited, path, paths)

  return score

def solve_b(data):
  answer = 0

  grid = [list(row) for row in data.split("\n")]
  n = len(grid)
  m = len(grid[0])
  trailheads = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == "0"]
  for i, j in trailheads:
    answer += _hike_2(grid, i, j, set(), f"{i}{j}", set())
    
  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
