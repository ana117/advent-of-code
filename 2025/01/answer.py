
"""
Write the question summary here
"""
              
test_data_a = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
""".strip()
test_data_b = test_data_a
test_answer_a = 3
test_answer_b = 6


def _move(current, direction, amount):
  if direction == 'L':
    amount *= -1
  return (current + amount) % 100

def solve_a(data):
  answer = 0

  current = 50
  for line in data.splitlines():
    direction = line[0]
    amount = int(line[1:])
    current = _move(current, direction, amount)
    if current == 0:
      answer += 1
  
  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  current = 50
  for line in data.splitlines():
    direction = line[0]
    amount = int(line[1:])
    
    adder = 1 if direction == 'R' else -1
    for _ in range(amount):
      current = (current + adder) % 100
      if current == 0:
        answer += 1
  
  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
