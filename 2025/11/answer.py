
"""
Write the question summary here
"""

test_data_a = """
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
""".strip()
test_data_b = """
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
""".strip()
test_answer_a = 5
test_answer_b = 2


def _lead_to_target(graph, start, end):
  memory = {}
  for k, v in graph.items():
    memory[k] = None
    for val in v:
      memory[val] = None
  memory[end] = 1

  while memory[start] is None:
    for node in memory:
      if memory[node] is None and all(memory[child] is not None for child in graph.get(node, ())):
        memory[node] = sum(memory[child] for child in graph.get(node, ()))
  
  return memory[start]

def solve_a(data):
  answer = 0

  graph = {}
  for line in data.splitlines():
    source, outputs = line.split(": ")
    graph[source] = outputs.split(" ")

  answer = _lead_to_target(graph, "you", "out")

  return answer

def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"


def solve_b(data):
  answer = 0

  graph = {}
  for line in data.splitlines():
    source, outputs = line.split(": ")
    graph[source] = outputs.split(" ")

  svr_dac = _lead_to_target(graph, "svr", "dac")
  dac_fft = _lead_to_target(graph, "dac", "fft")
  fft_out = _lead_to_target(graph, "fft", "out")
  answer = svr_dac * dac_fft * fft_out

  if answer == 0:
    svr_fft = _lead_to_target(graph, "svr", "fft")
    fft_dac = _lead_to_target(graph, "fft", "dac")
    dac_out = _lead_to_target(graph, "dac", "out")
    answer = svr_fft * fft_dac * dac_out

  return answer
 
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"


if __name__ == "__main__":
  test_a()
  test_b()
