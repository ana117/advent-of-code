
"""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    
    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""
              

test_data_a = """
029A
980A
179A
456A
379A
""".strip()
test_data_b = test_data_a
test_answer_a = 126384
test_answer_b = test_answer_a


NUMPAD = [
  ["7", "8", "9"],
  ["4", "5", "6"],
  ["1", "2", "3"],
  [" ", "0", "A"]
]

DIRPAD = [
  [" ", "^", "A"],
  ["<", "v", ">"]
]

DIRECTIONS = {
  (0, 1): "v",
  (0, -1): "^",
  (1, 0): ">",
  (-1, 0): "<",
}


def _get_index(grid, value):
  for y, row in enumerate(grid):
    for x, cell in enumerate(row):
      if cell == value:
        return x, y
  return None

PATH_MEMORY = {}
def _get_path(grid_name, start, end):
  if (grid_name, start, end) in PATH_MEMORY:
    return PATH_MEMORY[(grid_name, start, end)]
  
  grid = NUMPAD if grid_name == "numpad" else DIRPAD
  
  start = _get_index(grid, start)
  end = _get_index(grid, end)
  empty = _get_index(grid, " ")

  visited = {start, empty}
  q = [(start, [])]
  paths = []

  distance = 0
  min_distance = float("inf")
  while q and distance <= min_distance:
    (x, y), path = q.pop(0)
    distance = len(path)
    if (x, y) == end:
      paths.append("".join(path) + "A")
      min_distance = distance
    else:
      visited.add((x, y))
      for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid) and (nx, ny) not in visited:
          q.append(((nx, ny), path + [DIRECTIONS[(dx, dy)]]))

  PATH_MEMORY[(grid_name, start, end)] = paths
  return paths

DPAD_MEMORY = {}
def _min_dpad_path(sequence, depth):
  if (sequence, depth) in DPAD_MEMORY:
    return DPAD_MEMORY[(sequence, depth)]
  
  if depth == 0:
    return len(sequence)
  
  d = 0
  curr = "A"
  for target in sequence:
    paths = _get_path("dirpad", curr, target)
    lengths = [_min_dpad_path(path, depth - 1) for path in paths]
    d += min(lengths)
    curr = target

  DPAD_MEMORY[(sequence, depth)] = d
  return d


def solve_a(data):
  global PATH_MEMORY, DPAD_MEMORY
  PATH_MEMORY = {}
  DPAD_MEMORY = {}

  answer = 0

  for line in data.split("\n"):
    codes = line.strip()
    curr = "A"
    for target in codes:
      paths = _get_path("numpad", curr, target)
      curr = target

      min_dpad = min([_min_dpad_path(path, 2) for path in paths])
      answer += min_dpad * int(codes[:-1])

  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  global PATH_MEMORY, DPAD_MEMORY
  PATH_MEMORY = {}
  DPAD_MEMORY = {}

  answer = 0

  for line in data.split("\n"):
    codes = line.strip()
    curr = "A"
    for target in codes:
      paths = _get_path("numpad", curr, target)
      curr = target

      min_dpad = min([_min_dpad_path(path, 25) for path in paths])
      answer += min_dpad * int(codes[:-1])

  return answer
              
def test_b():
  return True
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"


if __name__ == "__main__":
  test_a()
  test_b()
