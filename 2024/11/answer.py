
"""
Write the question summary here
"""
              
test_data_a = """
125 17
""".strip()
test_data_b = test_data_a
test_answer_a = 55312
test_answer_b = 65601038650482


BLINK_TIMES = 25
BLINK_TIMES_B = 75
MULTIPLIER = 2024

def solve_a(data):
  answer = 0

  stones = list(map(int, data.split()))
  for _ in range(BLINK_TIMES):
    next_arrangement = []
    for stone in stones:
      if stone == 0:
        next_arrangement.append(1)
      
      elif len(str(stone)) % 2 == 0:
        string_stone = str(stone)
        mid = len(string_stone) // 2
        left = int(string_stone[:mid])
        right = int(string_stone[mid:])
        next_arrangement.extend([left, right])
      
      else:
        next_arrangement.append(stone * MULTIPLIER)

    stones = next_arrangement

  answer = len(stones)
  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  stones = {}
  for stone in map(int, data.split()):
    if stone not in stones:
      stones[stone] = 0
    stones[stone] += 1

  for _ in range(BLINK_TIMES_B):
    next_stones = {}
    transformation = []
    for stone in stones:
      if stone == 0:
        transformation.append((stone, 1))
      
      elif len(str(stone)) % 2 == 0:
        string_stone = str(stone)
        mid = len(string_stone) // 2
        left = int(string_stone[:mid])
        right = int(string_stone[mid:])
        transformation.append((stone, left))
        transformation.append((stone, right))

      else:
        transformation.append((stone, stone * MULTIPLIER))
      
    for old, new in transformation:
      if new not in next_stones:
        next_stones[new] = 0
      next_stones[new] += stones[old]

    stones = next_stones

  answer = sum(stones.values())
  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
