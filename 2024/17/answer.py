
"""
Write the question summary here
"""
              
from math import inf


test_data_a = """
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
""".strip()
test_data_b = """
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0
""".strip()
test_answer_a = "4,6,3,5,6,3,5,2,1,0"
test_answer_b = 117440
              

A = B = C = 0

def _get_combo_operand(operand):
  global A, B, C

  operand = int(operand)
  if 0 <= operand <= 3:
    return operand
  
  if operand == 4: return A
  if operand == 5: return B
  if operand == 6: return C

def _adv(operand):
  global A
  denominator = 2 ** _get_combo_operand(operand)
  A = A // denominator

def _bxl(operand):
  global B
  B = B ^ int(operand)

def _bst(operand):
  global B
  B = _get_combo_operand(operand) % 8

def _jnz(operand):
  if A == 0: return None
  return int(operand)

def _bxc(operand):
  global B
  B = B ^ C

def _out(operand):
  return _get_combo_operand(operand) % 8

def _bdv(operand):
  global A, B
  denominator = 2 ** _get_combo_operand(operand)
  B = A // denominator

def _cdv(operand):
  global A, C
  denominator = 2 ** _get_combo_operand(operand)
  C = A // denominator


def _run(program):
  i = 0
  output = []
  while i < len(program):
    jump = None
    opcode = str(program[i])
    operand = program[i+1]
    
    if opcode == "0": _adv(operand)
    if opcode == "1": _bxl(operand)
    if opcode == "2": _bst(operand)
    if opcode == "3": jump = _jnz(operand)
    if opcode == "4": _bxc(operand)
    if opcode == "5": output.append(_out(operand))
    if opcode == "6": _bdv(operand)
    if opcode == "7": _cdv(operand)

    if jump is not None:
      i = jump - 2

    i += 2

  return output

def solve_a(data):
  answer = 0

  global A, B, C
  registers, program = data.split("\n\n")
  for line in registers.split("\n"):
    register, value = line.split(":")
    if register == "Register A": A = int(value)
    if register == "Register B": B = int(value)
    if register == "Register C": C = int(value)

  program = program[9:].split(",")

  answer = ",".join(map(str, _run(program)))
  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  global A, B, C
  registers, program = data.split("\n\n")
  for line in registers.split("\n"):
    register, value = line.split(":")
    if register == "Register A": A = int(value)
    if register == "Register B": B = int(value)
    if register == "Register C": C = int(value)

  program = program[9:].split(",")
  program = list(map(int, program))

  answer = inf
  q = [(1, 0)]
  for i, a in q:
    for a in range(a, a+8):
      A = a
      B = C = 0
      if _run(program) == program[-i:]:
        q += [(i+1, a*8)]
        if i == len(program):
          answer = min(answer, a)
  
  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
