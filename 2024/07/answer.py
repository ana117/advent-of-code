
"""
Write the question summary here
"""
              
test_data_a = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
""".strip()
test_data_b = test_data_a
test_answer_a = 3749
test_answer_b = 11387
              
def _add(a, b):
  return a + b

def _multiply(a, b):
  return a * b

def _concat(a, b):
  return int(str(a) + str(b))

def solve_a(data):
  answer = 0

  operator = [_add, _multiply]
  for equation in data.split("\n"):
    target, values = equation.split(":")
    target = int(target)
    values = list(map(int, values.split()))

    for i in range(2 ** (len(values) - 1)):
      current = values[0]
      for j in range(len(values) - 1):
        if i & (1 << j):
          current = operator[1](current, values[j + 1])
        else:
          current = operator[0](current, values[j + 1])
      if current == target:
        answer += target
        break

  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  operator = [_add, _multiply, _concat]
  for equation in data.split("\n"):
    target, values = equation.split(":")
    target = int(target)
    values = list(map(int, values.split()))

    for i in range(3 ** (len(values) - 1)):
      current = values[0]
      for j in range(len(values) - 1):
        current = operator[i % 3](current, values[j + 1])
        i //= 3
      if current == target:
        answer += target
        break

  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
