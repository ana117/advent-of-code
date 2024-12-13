
"""
Write the question summary here
"""
              
test_data_a = """
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
""".strip()
test_data_b = test_data_a
test_answer_a = 480
test_answer_b = 875318608908
              

def _get_x_y(data, sep):
  x, y = data.split(",")
  x = int(x.split(sep)[1])
  y = int(y.split(sep)[1])
  return x, y

def _get_machine_data(machine):
  a, b, prize = machine.split("\n")

  a = a.split(": ")[1]
  a = _get_x_y(a, "+")

  b = b.split(": ")[1]
  b = _get_x_y(b, "+")

  prize = prize.split(": ")[1]
  prize = _get_x_y(prize, "=")

  return a, b, prize


def solve_a(data):
  answer = 0

  machines = data.split("\n\n")
  for machine in machines:
    a, b, prize = _get_machine_data(machine)
    ax, ay = a
    bx, by = b
    px, py = prize

    det = ax * by - ay * bx
    det_a = px * by - py * bx
    det_b = ax * py - ay * px

    A = det_a / det
    B = det_b / det

    if (A.is_integer() and B.is_integer()):
      answer += (3 * A) + B

  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  machines = data.split("\n\n")
  for machine in machines:
    a, b, prize = _get_machine_data(machine)
    ax, ay = a
    bx, by = b
    px, py = prize

    px += 10000000000000
    py += 10000000000000

    det = ax * by - ay * bx
    det_a = px * by - py * bx
    det_b = ax * py - ay * px

    A = det_a / det
    B = det_b / det

    if (A.is_integer() and B.is_integer()):
      answer += (3 * A) + B

  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
