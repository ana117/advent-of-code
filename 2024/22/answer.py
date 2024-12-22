
"""
Write the question summary here
"""
              
from functools import lru_cache


test_data_a = """
1
10
100
2024
""".strip()
test_data_b = """
1
2
3
2024
""".strip()
test_answer_a = 37327623
test_answer_b = 23
              

@lru_cache(maxsize=None)
def _mix(a, b):
  return a ^ b

@lru_cache(maxsize=None)
def _prune(a):
  return a % 16777216

@lru_cache(maxsize=None)
def _step_one(a):
  return _prune(_mix(a, a * 64))

@lru_cache(maxsize=None)
def _step_two(a):
  return _prune(_mix(a, a // 32))

@lru_cache(maxsize=None)
def _step_three(a):
  return _prune(_mix(a, a * 2048))

@lru_cache(maxsize=None)
def _generate_next_secret(a):
  return _step_three(_step_two(_step_one(a)))


def solve_a(data):
  answer = 0

  for line in data.split("\n"):
    if not line:
      continue
    a = int(line)
    for _ in range(2000):
      a = _generate_next_secret(a)
    answer += a

  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  sequences = set()
  result_sequences = []
  for line in data.split("\n"):
    if not line:
      continue

    curr_results = []
    a = int(line)
    for _ in range(2000):
      initial = a % 10
      a = _generate_next_secret(a)
      curr_results.append((a, (a % 10) - initial))

    curr_sequences = {}
    for i in range(len(curr_results) - 3):
      sequence = tuple([curr_results[i + j][1] for j in range(4)])
      if sequence not in curr_sequences:
        curr_sequences[sequence] = curr_results[i + 3][0] % 10
    
    sequences.update(curr_sequences.keys())
    result_sequences.append(curr_sequences)
  
  for sequence in sequences:
    curr = 0
    for result_sequence in result_sequences:
      if sequence in result_sequence:
        curr += result_sequence[sequence]
    answer = max(answer, curr)

  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"
              
if __name__ == "__main__":
  test_a()
  test_b()
