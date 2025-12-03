
"""
Write the question summary here
"""
              
test_data_a = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
""".strip()
test_data_b = test_data_a
test_answer_a = 1227775554
test_answer_b = 4174379265
              

def _is_valid_a(num):
  num = str(num)
  if len(num) % 2 == 0:
    mid_point = len(num) // 2
    left, right = num[:mid_point], num[mid_point:]
    if left == right:
      return False
  return True

def solve_a(data):
  answer = 0

  for id_range in data.split(","):
    one, two = id_range.split("-")
    for num in range(int(one), int(two) + 1):
      if not _is_valid_a(num):
        answer += num

  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"


import re
def _is_valid_b(num):
  num = str(num)
  for length in range(1, len(num) // 2 + 1):
    if len(num) % length == 0:
      occurences = [m for m in re.finditer(num[:length], num)]
      if len(occurences) * length == len(num):
        return False
  return True

def solve_b(data):
  answer = 0

  for id_range in data.split(","):
    one, two = id_range.split("-")
    for num in range(int(one), int(two) + 1):
      if not _is_valid_b(num):
        answer += num

  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
