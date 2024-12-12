
"""
Write the question summary here
"""
              

test_data_a = """
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
""".strip()
test_data_b = test_data_a
test_answer_a = 1930
test_answer_b = 1206
              

def _flood_fill(grid, i, j, visited, region, label):
  n = len(grid)
  m = len(grid[0])
  if i < 0 or i >= n or j < 0 or j >= m or (i, j) in visited or grid[i][j] != label:
    return region
  
  visited.add((i, j))
  region.append((i, j))
  
  region = _flood_fill(grid, i + 1, j, visited, region, label)
  region = _flood_fill(grid, i - 1, j, visited, region, label)
  region = _flood_fill(grid, i, j + 1, visited, region, label)
  region = _flood_fill(grid, i, j - 1, visited, region, label)

  return region  


def solve_a(data):
  answer = 0

  regions = []
  grid = list(map(list, data.split("\n")))
  n = len(grid)
  m = len(grid[0])

  visited = set()
  for i in range(n):
    for j in range(m):
      if (i, j) in visited:
        continue
      region = _flood_fill(grid, i, j, visited, [], grid[i][j])
      regions.append(region)

  for region in regions:
    area = len(region)
    perimeter = 0
    for i, j in region:
      if i == 0 or (i - 1, j) not in region:
        perimeter += 1
      if i == n - 1 or (i + 1, j) not in region:
        perimeter += 1
      if j == 0 or (i, j - 1) not in region:
        perimeter += 1
      if j == m - 1 or (i, j + 1) not in region:
        perimeter += 1
    answer += (area * perimeter)

  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  regions = []
  grid = list(map(list, data.split("\n")))
  n = len(grid)
  m = len(grid[0])

  visited = set()
  for i in range(n):
    for j in range(m):
      if (i, j) in visited:
        continue
      region = _flood_fill(grid, i, j, visited, [], grid[i][j])
      regions.append(region)

  for region in regions:
    area = len(region)
    sides = 0

    for i, j in region:
      this = grid[i][j]
      up = grid[i - 1][j] if i > 0 else None
      down = grid[i + 1][j] if i < n - 1 else None
      left = grid[i][j - 1] if j > 0 else None
      right = grid[i][j + 1] if j < m - 1 else None

      if this != up and this != right:
        sides += 1
      if this != down and this != right:
        sides += 1
      if this != down and this != left:
        sides += 1
      if this != up and this != left:
        sides += 1
      
      up_left = grid[i - 1][j - 1] if i > 0 and j > 0 else None
      up_right = grid[i - 1][j + 1] if i > 0 and j < m - 1 else None
      down_left = grid[i + 1][j - 1] if i < n - 1 and j > 0 else None
      down_right = grid[i + 1][j + 1] if i < n - 1 and j < m - 1 else None

      if this != up_left and this == up and this == left:
        sides += 1
      if this != up_right and this == up and this == right:
        sides += 1
      if this != down_left and this == down and this == left:
        sides += 1
      if this != down_right and this == down and this == right:
        sides += 1

    answer += (area * sides)

  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
