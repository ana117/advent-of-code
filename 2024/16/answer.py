
"""
Write the question summary here
"""
              
import heapq
from multiprocessing import heap


test_data_a = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
""".strip()
test_data_b = test_data_a
test_answer_a = 7036
test_answer_b = 44
              

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def djikstra(grid, start):
  q = [(0, start[0], start[1], 0, {(start[0], start[1])})]
  visited = set()
  while q:
    dist, x, y, direction, path = heapq.heappop(q)
    
    if (x, y) in visited:
      continue

    if grid[x][y] == "E":
      return dist, path
    
    visited.add((x, y))

    direction_right = (direction + 1) % 4
    direction_left = (direction - 1) % 4

    for dir in [direction, direction_right, direction_left]:
      dx, dy = DIRECTIONS[dir]
      nx, ny = x + dx, y + dy
      if grid[nx][ny] == "#" or (nx, ny) in visited:
        continue

      cost = 1
      if dir != direction:
        cost += 1000
      
      npath = path.copy()
      npath.add((nx, ny))
      heapq.heappush(q, (dist + cost, nx, ny, dir, npath))

  return -1, None


def solve_a(data):
  answer = 0

  grid = [list(row) for row in data.split("\n")]
  reindeer = None
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == "S":
        reindeer = (i, j, 0)
        break
    if reindeer:
      break
  
  answer, _ = djikstra(grid, reindeer)

  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  grid = [list(row) for row in data.split("\n")]
  reindeer = None
  for i in range(len(grid)):
    for j in range(len(grid[i])):
      if grid[i][j] == "S":
        reindeer = (i, j, 0)
        break
    if reindeer:
      break
  
  minimum, path = djikstra(grid, reindeer)

  seats = path.copy()
  for x, y in path:
    if grid[x][y] in "SE":
      continue

    grid[x][y] = "#"
    cost, seat_path = djikstra(grid, reindeer)
    if cost == minimum:
      seats.update(seat_path)
    grid[x][y] = "."

  answer = len(seats)
  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
