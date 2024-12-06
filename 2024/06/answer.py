
"""
The map shows the current position of the guard with ^ (to indicate the guard is currently facing up from the perspective of the map). 
Any obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:
- If there is something directly in front of you, turn right 90 degrees.
- Otherwise, take a step forward.
"""
              
test_data_a = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip()
test_data_b = test_data_a
test_answer_a = 41
test_answer_b = 6
              

def solve_a(data):
  answer = 0

  guard = (0, 0)
  direction = (0, 1)

  obstacles = set()
  rows = data.split("\n")

  size = (len(rows[0]), len(rows))

  for y, row in enumerate(rows):
    for x, cell in enumerate(row):
      if cell == "#":
        obstacles.add((x, y))
      elif cell == "^":
        guard = (x, y)
        direction = (0, -1)
      elif cell == ">":
        guard = (x, y)
        direction = (1, 0)
      elif cell == "v":
        guard = (x, y)
        direction = (0, 1)
      elif cell == "<":
        guard = (x, y)
        direction = (-1, 0)

  stepped = set([guard])
  while True:
    if guard[0] < 0 or guard[0] >= size[0] or guard[1] < 0 or guard[1] >= size[1]:
      break

    if (guard[0] + direction[0], guard[1] + direction[1]) in obstacles:
      direction = (-direction[1], direction[0])
    else:
      guard = (guard[0] + direction[0], guard[1] + direction[1])
      if guard not in stepped:
        answer += 1
        stepped.add(guard)

  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  grid = [list(row) for row in data.split("\n")]
  size = (len(grid[0]), len(grid))
  for x in range(size[0]):
    for y in range(size[1]):
      if grid[y][x] == "^":
        guard = (x, y)
        break
    else:
      continue
    break

  directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

  # Brute force, put obstacles in every spot
  for x in range(size[0]):
    for y in range(size[1]):
      if grid[y][x] == "#":
        continue

      stepped = set()
      stepped_dir = set()
      loop_guard = (guard[0], guard[1]) 
      direction = 0

      while True:
        if (*loop_guard, direction) in stepped_dir:
          answer += 1
          break

        stepped.add(loop_guard)
        stepped_dir.add((*loop_guard, direction))
        next_loop_guard = (loop_guard[0] + directions[direction][0], loop_guard[1] + directions[direction][1])

        if next_loop_guard[0] < 0 or next_loop_guard[0] >= size[0] or next_loop_guard[1] < 0 or next_loop_guard[1] >= size[1]:
          break
        
        if grid[next_loop_guard[1]][next_loop_guard[0]] == "#" or (next_loop_guard[0] == x and next_loop_guard[1] == y):
          direction = (direction + 1) % 4
        else:
          loop_guard = (loop_guard[0] + directions[direction][0], loop_guard[1] + directions[direction][1])

  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
