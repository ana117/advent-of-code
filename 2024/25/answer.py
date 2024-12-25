
"""
Write the question summary here
"""
              
test_data_a = """
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
""".strip()
test_data_b = test_data_a
test_answer_a = 3
test_answer_b = 0
              

def solve_a(data):
  answer = 0
  locks = []
  keys = []

  for group in data.split("\n\n"):
    heights = [-1] * 5
    is_lock = group[0] == "#"
    for line in group.split("\n"):
      for i, c in enumerate(line):
        if c == "#":
          heights[i] += 1

    if is_lock:
      locks.append(heights)
    else:
      keys.append(heights)
  
  
  for lock in locks:
    for key in keys:
      for i in range(5):
        if lock[i] + key[i] > 5:
          break
      else:
        answer += 1

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
