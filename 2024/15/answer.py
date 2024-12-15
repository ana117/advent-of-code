
"""
Write the question summary here
"""
              
test_data_a = """
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
""".strip()
test_data_b = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
""".strip()
test_answer_a = 10092
test_answer_b = 9021
              

def solve_a(data):
  answer = 0

  grid, sequences = data.split("\n\n")
  grid = [list(row[1:-1]) for row in grid.split("\n")[1:-1]]
  sequences = "".join(sequences.split())

  n = len(grid)
  m = len(grid[0])

  start = (0, 0)
  for i in range(n):
    for j in range(m):
      if grid[i][j] == "@":
        start = (i, j)
        grid[i][j] = "."
        break
  
  directions = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
  }
  for sequence in sequences:
    dx, dy = directions[sequence]
    x, y = start
    
    if x + dx < 0 or x + dx >= n or y + dy < 0 or y + dy >= m or grid[x + dx][y + dy] == "#":
      continue

    if grid[x + dx][y + dy] == "O":
      pushed_boxes = []
      box_x, box_y = x + dx, y + dy

      temp = []
      while True:
        next_box_x, next_box_y = box_x + dx, box_y + dy
        if next_box_x < 0 or next_box_x >= n or next_box_y < 0 or next_box_y >= m or grid[next_box_x][next_box_y] == "#":
          break
        elif grid[next_box_x][next_box_y] == "O":
          temp.append((box_x, box_y))
        elif grid[next_box_x][next_box_y] == ".":
          temp.append((box_x, box_y))
          pushed_boxes.extend(temp)
          break

        box_x += dx
        box_y += dy

      if pushed_boxes:
        start = (x + dx, y + dy)
        for box_x, box_y in pushed_boxes:
          grid[box_x][box_y] = "."
        
        for box_x, box_y in pushed_boxes:
          grid[box_x + dx][box_y + dy] = "O"

    else:
      start = (x + dx, y + dy)

  for i in range(n):
    for j in range(m):
      if grid[i][j] == "O":
        answer += 100 * (i+1) + j + 1

  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
    answer = 0
    return answer

def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
