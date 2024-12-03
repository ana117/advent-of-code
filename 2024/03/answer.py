"""
It seems like the goal of the program is just to multiply some numbers. 
It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers.

However, because the program's memory has been corrupted, there are also many invalid 
characters that should be ignored, even if they look like part of a mul instruction. 
Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.
--
There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.
"""

test_data = """
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
""".strip()
test_answer_a = 161

test_data_2 = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
""".strip()
test_answer_b = 48


def solve_a(data):
  answer = 0
  
  for i in range(len(data)):
    if data[i:i+4] == "mul(":
      is_valid = True
      nums_1 = ""
      nums_2 = ""
      i += 4

      while data[i] != ",":
        curr = data[i]
        i += 1
        if not curr.isnumeric():
          is_valid = False
          break
        nums_1 += curr
      
      if not is_valid:
        continue
      
      i += 1
      while data[i] != ")":
        curr = data[i]
        i += 1
        if not curr.isnumeric():
          is_valid = False
          break
        nums_2 += curr

      if is_valid:
        answer += int(nums_1) * int(nums_2)
  return answer

def test_a():
  answer = solve_a(test_data)
  assert answer == test_answer_a, f"expected {test_answer_a} but got {answer}"


def solve_b(data):
  answer = 0
  
  is_enabled  = True
  i = 0
  while i < len(data):
    if data[i:i+4] == "do()":
      is_enabled = True
      i += 4
    elif data[i:i+7] == "don't()":
      is_enabled = False
      i += 6
    elif data[i:i+4] == "mul(":
      is_valid = True
      nums_1 = ""
      nums_2 = ""
      i += 4

      while data[i] != ",":
        curr = data[i]
        i += 1
        if not curr.isnumeric():
          is_valid = False
          break
        nums_1 += curr
      
      if not is_valid:
        continue
      
      i += 1
      while data[i] != ")":
        curr = data[i]
        i += 1
        if not curr.isnumeric():
          is_valid = False
          break
        nums_2 += curr

      if is_valid and is_enabled:
        answer += int(nums_1) * int(nums_2)
    else:
      i += 1
      
  return answer

def test_b():
  answer = solve_b(test_data_2)
  assert answer == test_answer_b, f"expected {test_answer_b} but got {answer}"
