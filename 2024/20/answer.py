
"""
Write the question summary here
"""


test_data_a = """
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
""".strip()
test_data_b = test_data_a
test_answer_a = 44
test_answer_b = 285


def solver(grid, start, cheats, limit):
  cheat_count = 0

  distances = {start: 0}
  q = [start]
  while q:
    x, y = q.pop(0)
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
      nx, ny = x + dx, y + dy
      if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) or grid[nx][ny] == "#":
        continue

      if (nx, ny) not in distances:
        distances[(nx, ny)] = distances[(x, y)] + 1
        q.append((nx, ny))
  
  d_items = list(distances.items())
  for i in range(len(d_items)):
    for j in range(i + 1, len(d_items)):
      s, iv = d_items[i]
      e, jv = d_items[j]

      d = abs(s[0] - e[0]) + abs(s[1] - e[1])
      if d <= cheats and jv - iv - d >= limit:
        cheat_count += 1
  
  return cheat_count


def solve_a(data, test=False):
  answer = 0

  grid = [list(row) for row in data.split("\n")]
  start = end = None
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == "S":
        start = (i, j)
      if grid[i][j] == "E":
        end = (i, j)
    
    if start and end:
      break

  limit = 2 if test else 100  
  answer = solver(grid, start, 2, limit)

  return answer
              
def test_a():
  answer = solve_a(test_data_a, test=True)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data, test=False):
  answer = 0

  grid = [list(row) for row in data.split("\n")]
  start = end = None
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == "S":
        start = (i, j)
      if grid[i][j] == "E":
        end = (i, j)
    
    if start and end:
      break
      
  limit = 50 if test else 100
  answer = solver(grid, start, 20, limit)

  return answer
              
def test_b():
  answer = solve_b(test_data_b, test=True)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

                
if __name__ == "__main__":
  test_a()
  test_b()
