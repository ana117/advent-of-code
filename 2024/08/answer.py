
"""
Write the question summary here
"""
              
from calendar import c


test_data_a = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".strip()
test_data_b = test_data_a
test_answer_a = 14
test_answer_b = 34
              

def solve_a(data):
  answer = 0

  antennas = {}
  grid_size = (len(data.split("\n")[0]), len(data.split("\n")))
  for y, line in enumerate(data.split("\n")):
    for x, cell in enumerate(line):
      if cell != ".":
        if cell not in antennas:
          antennas[cell] = []
        antennas[cell].append((x, y))

  antinodes = set()
  for symbol, coords in antennas.items():
    for i in range(len(coords)):
      for j in range(i + 1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        x_gap = abs(x1 - x2)
        y_gap = abs(y1 - y2)
        if x1 > x2:
          x1_antinode = x1 + x_gap
          x2_antinode = x2 - x_gap
        else:
          x1_antinode = x1 - x_gap
          x2_antinode = x2 + x_gap
        if y1 > y2:
          y1_antinode = y1 + y_gap
          y2_antinode = y2 - y_gap
        else:
          y1_antinode = y1 - y_gap
          y2_antinode = y2 + y_gap
        
        if x1_antinode >= 0 and x1_antinode < grid_size[0] and y1_antinode >= 0 and y1_antinode < grid_size[1]:
          antinodes.add((x1_antinode, y1_antinode))
        if x2_antinode >= 0 and x2_antinode < grid_size[0] and y2_antinode >= 0 and y2_antinode < grid_size[1]:
          antinodes.add((x2_antinode, y2_antinode))

  answer = len(antinodes)
  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  antennas = {}
  grid_size = (len(data.split("\n")[0]), len(data.split("\n")))
  for y, line in enumerate(data.split("\n")):
    for x, cell in enumerate(line):
      if cell != ".":
        if cell not in antennas:
          antennas[cell] = []
        antennas[cell].append((x, y))

  antinodes = set()
  for _, coords in antennas.items():
    antinodes.update(coords)

    for i in range(len(coords)):
      for j in range(i + 1, len(coords)):
        x1, y1 = coords[i]
        x2, y2 = coords[j]
        x_gap = abs(x1 - x2)
        y_gap = abs(y1 - y2)

        if x1 > x2:
          x1_antinode = x1 + x_gap
          x2_antinode = x2 - x_gap
        else:
          x1_antinode = x1 - x_gap
          x2_antinode = x2 + x_gap
          
        if y1 > y2:
          y1_antinode = y1 + y_gap
          y2_antinode = y2 - y_gap
        else:
          y1_antinode = y1 - y_gap
          y2_antinode = y2 + y_gap
        
        while x1_antinode >= 0 and x1_antinode < grid_size[0] and y1_antinode >= 0 and y1_antinode < grid_size[1]:
          antinodes.add((x1_antinode, y1_antinode))
          if x1 > x2:
            x1_antinode += x_gap
          else:
            x1_antinode -= x_gap
          if y1 > y2:
            y1_antinode += y_gap
          else:
            y1_antinode -= y_gap

        while x2_antinode >= 0 and x2_antinode < grid_size[0] and y2_antinode >= 0 and y2_antinode < grid_size[1]:
          antinodes.add((x2_antinode, y2_antinode))
          if x1 > x2:
            x2_antinode -= x_gap
          else:
            x2_antinode += x_gap
          if y1 > y2:
            y2_antinode -= y_gap
          else:
            y2_antinode += y_gap

  answer = len(antinodes)
  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
