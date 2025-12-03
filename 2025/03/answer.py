
"""
Write the question summary here
"""

test_data_a = """
987654321111111
811111111111119
234234234234278
818181911112111
""".strip()
test_data_b = test_data_a
test_answer_a = 357
test_answer_b = 3121910778619


def solve_a(data):
  answer = 0

  for line in data.splitlines():
    digits = [int(c) for c in line.strip()]
    first = 0
    first_index = -1
    for i, digit in enumerate(digits[:-1]):
      if digit > first:
        first = digit
        first_index = i
    
    second = 0
    for digit in digits[first_index+1:]:
      if digit > second:
        second = digit
    
    answer += 10 * first + second

  return answer

def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"


def get_max(digits):
  max_digit = 0
  max_index = -1
  for i, digit in enumerate(digits):
    if digit > max_digit:
      max_digit = digit
      max_index = i
  return max_digit, max_index

def solve_b(data):
  answer = 0

  battery_count = 12
  for line in data.splitlines():
    last_index = 0
    digits = [int(c) for c in line.strip()]
    batteries = []
    for i in range(battery_count):
      ending = -1 * (battery_count - i - 1) if (battery_count - i -1) != 0 else None
      partial_digits = digits[last_index:ending] if ending is not None else digits[last_index:]
      max_digit, max_index = get_max(partial_digits)
      last_index += max_index + 1
      batteries.append(max_digit)

    total = 0
    for j, battery in enumerate(batteries):
      total += battery * (10 ** (battery_count - j - 1))
    answer += total

  return answer
 
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"


if __name__ == "__main__":
  test_a()
  test_b()
