
"""
Write the question summary here
"""
              
test_data_a = """
2333133121414131402
""".strip()
test_data_b = test_data_a
test_answer_a = 1928
test_answer_b = 2858
              

def solve_a(data):
  answer = 0

  blocks = []
  idx = 0
  status = 1  # 1: block, -1: space
  for c in data:
    for _ in range(int(c)):
      if status == 1:
        blocks.append(str(idx))
      else:
        blocks.append(".")

    if status == 1:
      idx += 1
    status *= -1
  
  i = 0
  j = len(blocks) - 1
  while i < j:
    if blocks[j] == ".":
      j -= 1
      continue

    if blocks[i] != ".":
      i += 1
      continue

    blocks[i], blocks[j] = blocks[j], blocks[i]
    i += 1
    j -= 1
  
  for i in range(len(blocks)):
    if blocks[i] == ".":
      break
    answer += (i * int(blocks[i]))

  return answer
              
def test_a():
  answer = solve_a(test_data_a)
  assert answer == test_answer_a, f"test_a failed: expected {test_answer_a} but got {answer}"

               
def solve_b(data):
  answer = 0

  blocks = []
  spaces = []

  idx = 0
  for i in range(len(data)):
    length = int(data[i])
    if length == 0:
      continue
    if i % 2 == 0:
      blocks.append((i // 2, idx, length))
    else:
      spaces.append((idx, length))
    idx += length

  
  for i in range(len(blocks)-1, -1, -1):
    value, idx, length = blocks[i]
    for j in range(len(spaces)):
      space_idx, space_length = spaces[j]
      if space_length >= length and space_idx < idx:
        blocks[i] = (value, space_idx, length)

        if space_length == length:
          spaces.pop(j)
        else:
          spaces[j] = (space_idx + length, space_length - length)
        
        spaces.append((idx, length))
        break

  for i in range(len(blocks)):
    value, idx, length = blocks[i]
    for j in range(length):
      answer += (j + idx) * value

  return answer
              
def test_b():
  answer = solve_b(test_data_b)
  assert answer == test_answer_b, f"test_b failed: expected {test_answer_b} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
