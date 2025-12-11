
"""
Write the question summary here
"""

from collections import deque
import numpy as np


test_data_a = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".strip()
test_data_b = test_data_a
test_answer_a = 7
test_answer_b = 33


def solve_a(data):
  answer = 0

  machines = []
  for line in data.splitlines():
    initial_state, o = line.split("] ")
    initial_state = initial_state[1:]
    initial_state = ["1" if c == "#" else "0" for c in initial_state]

    buttons, _ = o.split(" {")
    buttons = [
      tuple(int(x) for x in b[1:-1].split(",") if x)
      for b in buttons.split()
    ]
    machines.append((initial_state, buttons))

  for machine in machines:
    initial_state = int("".join(machine[0][::-1]), 2)
    seen = set()
    q = deque([(initial_state, 0)])
    while q:
      state, steps = q.popleft()
      if state == 0:
        answer += steps
        break
      if state in seen:
        continue
      seen.add(state)

      for button in machine[1]:
        q.append((state ^ sum(1 << i for i in button), steps + 1))

  return answer

def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"


def solve_b(data):
  answer = 0
  return answer
 
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"


if __name__ == "__main__":
  test_a()
  test_b()
