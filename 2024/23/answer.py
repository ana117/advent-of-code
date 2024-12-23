"""
Write the question summary here
"""
              
from collections import defaultdict


test_data_a = """
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
""".strip()
test_data_b = test_data_a
test_answer_a = 7
test_answer_b = "co,de,ka,ta"
              

def solve_a(data):
  answer = 0

  parties = defaultdict(set)
  for line in data.split("\n"):
    a, b = line.split("-")
    parties[a].add(b)
    parties[b].add(a)
  
  t_lan = set()
  for pt in parties:
    if pt.startswith("t"):
      for pa in parties[pt]:
        for pb in parties[pt]:
          if pb in parties[pa]:
            t_lan.add("".join(sorted([pt, pa, pb])))

  answer = len(t_lan)
  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  parties = defaultdict(set)
  for line in data.split("\n"):
    a, b = line.split("-")
    parties[a].add(b)
    parties[b].add(a)
  

  largest_size = -1
  largest = None
  for a in parties:
      for b in parties[a]:
        
        curr_party = None
        for c in parties[a]:
          if c == b: continue

          if curr_party is None:
            curr_party = {c} | parties[c]
          else:
            curr_party = curr_party.intersection({c} | parties[c])

        if curr_party is not None and len(curr_party) > largest_size:
          largest = sorted(curr_party)
          largest_size = len(curr_party)

  answer = ",".join(largest)
  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
