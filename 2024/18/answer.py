
"""
Write the question summary here
"""
              
import heapq


test_data_a = """
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
""".strip()
test_data_b = test_data_a
test_answer_a = 22
test_answer_b = "6,1"
              

def djikstra(grid, start, target):
  q = [(0, start[0], start[1], {(start[0], start[1])})]
  visited = set()
  while q:
    dist, x, y, path = heapq.heappop(q)
    
    if (x, y) in visited:
      continue

    if x == target[0] and y == target[1]:
      return dist, path
    
    visited.add((x, y))

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
      nx, ny = x + dx, y + dy
      if not (0 <= nx < len(grid) and 0 <= ny < len(grid[0])) or grid[nx][ny] == "#" or (nx, ny) in visited:
        continue

      npath = path.copy()
      npath.add((nx, ny))
      heapq.heappush(q, (dist + 1, nx, ny, npath))

  return -1, None

def solve_a(data, test=False):
  answer = 0

  n = 70 if not test else 6
  limit = 1024 if not test else 12

  grid = [["." for _ in range(n+1)] for _ in range(n+1)]
  lines = data.strip().split("\n")
  for i in range(limit):
    line = lines[i]
    x, y = map(int, line.split(","))
    grid[y][x] = "#"
  
  answer, path = djikstra(grid, (0, 0), (n, n))

  return answer
              
def test_a():
  answer = solve_a(test_data_a, test=True)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data, test=False):
  answer = 0

  n = 70 if not test else 6
  limit = 1024 if not test else 12

  grid = [["." for _ in range(n+1)] for _ in range(n+1)]
  lines = data.strip().split("\n")
  for i in range(limit):
    line = lines[i]
    x, y = map(int, line.split(","))
    grid[x][y] = "#"
  
  d, path = djikstra(grid, (0, 0), (n, n))

  possible = d != -1
  i = limit
  while possible:
    x, y = lines[i].split(",")
    x, y = int(x), int(y)
    grid[x][y] = "#"

    if (x, y) in path:
      d, path = djikstra(grid, (0, 0), (n, n))

    possible = d != -1
    i += 1

  answer = lines[i-1]
  return answer
              
def test_b():
  answer = solve_b(test_data_b, test=True)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
