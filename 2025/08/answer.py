
"""
Write the question summary here
"""

test_data_a = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".strip()
test_data_b = test_data_a
test_answer_a = 40
test_answer_b = 25272


def _get_distance(a, b):
  xa, ya, za = a
  xb, yb, zb = b
  return ((xa - xb) ** 2 + (ya - yb) ** 2 + (za - zb) ** 2) ** 0.5

def solve_a(data, max_iterations=1000):
  answer = 0

  boxes = data.splitlines()
  dimensions = [list(map(int, box.split(","))) for box in boxes]
  box_circuit = [{i} for i in range(len(dimensions))]

  distances = []
  for i in range(len(dimensions)):
    for j in range(i + 1, len(dimensions)):
      dist = _get_distance(dimensions[i], dimensions[j])
      distances.append((dist, i, j))
  distances = sorted(distances, key=lambda x: x[0])

  for _, i, j in distances[:max_iterations]:
    box_circuit[i].update(box_circuit[j])
    for k in box_circuit[j]:
      box_circuit[k] = box_circuit[i]
  
  unique_circuits = []
  seen = set()
  for circuit in box_circuit:
    circuit_id = frozenset(circuit)
    if circuit_id not in seen:
      seen.add(circuit_id)
      unique_circuits.append(circuit)

  largest_circuits = sorted(unique_circuits, key=lambda x: -len(x))[:3]
  answer = 1
  for circuit in largest_circuits:
    answer *= len(circuit)

  return answer

def test_a():
  answer = solve_a(test_data_a, max_iterations=10)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"


def solve_b(data):
  answer = 0

  boxes = data.splitlines()
  dimensions = [list(map(int, box.split(","))) for box in boxes]
  box_circuit = [{i} for i in range(len(dimensions))]

  distances = []
  for i in range(len(dimensions)):
    for j in range(i + 1, len(dimensions)):
      dist = _get_distance(dimensions[i], dimensions[j])
      distances.append((dist, i, j))
  distances = sorted(distances, key=lambda x: x[0])

  last_pair = None
  for _, i, j in distances:
    box_circuit[i].update(box_circuit[j])
    for k in box_circuit[j]:
      box_circuit[k] = box_circuit[i]
    
    if len(box_circuit[i]) == len(boxes):
      last_pair = (i, j)
      break

  a, b = last_pair
  answer = dimensions[a][0] * dimensions[b][0]

  return answer
 
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"


if __name__ == "__main__":
  test_a()
  test_b()
