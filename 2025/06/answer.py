
"""
Write the question summary here
"""

test_data_a = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".strip()
test_data_b = test_data_a
test_answer_a = 4277556
test_answer_b = 3263827


def solve_a(data):
  answer = 0

  lines = data.split("\n")
  number_rows = lines[:-1]
  operations = lines[-1].split()

  results = []
  is_first_pass = True
  for number_row in number_rows:
    numbers = list(map(int, number_row.split()))
    for i in range(len(operations)):
      if is_first_pass:
        results.append(numbers[i])
        continue
      
      if operations[i] == "*":
        results[i] *= numbers[i]
      elif operations[i] == "+":
        results[i] += numbers[i]
    is_first_pass = False

  answer = sum(results)

  return answer

def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"


from itertools import zip_longest
def solve_b(data):
  answer = 0

  lines = data.split("\n")
  number_rows = lines[:-1]
  operations = lines[-1].split()

  parsed_numbers = list(zip_longest(*number_rows))

  results = []
  digit_index = 0
  for i, op in enumerate(operations):
    while digit_index < len(parsed_numbers):
      digits = [int(d) for d in parsed_numbers[digit_index] if d.isdigit()]
      if not digits:
        digit_index += 1
        break
      
      parsed_number = int("".join(map(str, digits)))
      if len(results) <= i:
        results.append(parsed_number)
      else:
        if op == "*":
          results[i] *= parsed_number
        elif op == "+":
          results[i] += parsed_number
      digit_index += 1

  answer = sum(results)

  return answer
 
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"


if __name__ == "__main__":
  test_a()
  test_b()
