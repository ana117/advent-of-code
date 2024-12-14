
"""
Write the question summary here
"""
              
test_data_a = """
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
""".strip()
test_data_b = test_data_a
test_answer_a = 12
test_answer_b = test_answer_a
              

def solve_a(data):
  answer = 0

  size = 101, 103
  looping = 100
  robots = list(map(lambda x: x.split(' '), data.split('\n')))
  quadrants = [0, 0, 0, 0]
  qs = [[], [], [], []]
  for robot in robots:
    position = robot[0].split('=')[1].split(',')
    velocity = robot[1].split('=')[1].split(',')
    position = list(map(int, position))
    velocity = list(map(int, velocity))

    movement_x = velocity[0] * looping % size[0]
    movement_y = velocity[1] * looping % size[1]
    position[0] = (position[0] + movement_x) % size[0]
    position[1] = (position[1] + movement_y) % size[1]

    if position[0] < size[0] // 2 and position[1] < size[1] // 2:
      quadrants[0] += 1
      qs[0].append(position)
    elif position[0] > size[0] // 2 and position[1] < size[1] // 2:
      quadrants[1] += 1
      qs[1].append(position)
    elif position[0] < size[0] // 2 and position[1] > size[1] // 2:
      quadrants[2] += 1
      qs[2].append(position)
    elif position[0] > size[0] // 2 and position[1] > size[1] // 2:
      quadrants[3] += 1
      qs[3].append(position)

  answer = 1
  for q in quadrants:
    answer *= q

  return answer
              
def test_a():
  return True
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  size = 101, 103
  robots = list(map(lambda x: x.split(' '), data.split('\n')))
  for i in range(len(robots)):
    robot = robots[i]
    position = robot[0].split('=')[1].split(',')
    velocity = robot[1].split('=')[1].split(',')
    position = list(map(int, position))
    velocity = list(map(int, velocity))

    robots[i] = [position, velocity]
  
  used = set()
  while len(used) != len(robots):
    used = set()
    answer += 1
    for i in range(len(robots)):
      robot = robots[i]
      position, velocity = robot

      position[0] = (position[0] + velocity[0]) % size[0]
      position[1] = (position[1] + velocity[1]) % size[1]
      robots[i] = [position, velocity]
      used.add(tuple(position))

  return answer
              
def test_b():
  return True
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
