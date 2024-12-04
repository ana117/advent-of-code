import datetime
import os


AOC_NOW = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=5)
YEAR = str(AOC_NOW.year)
DAY = str(AOC_NOW.day)


if __name__ == "__main__":
  if not os.path.exists(YEAR):
    os.mkdir(YEAR)
  
  day = DAY.zfill(2)
  folder_path = os.path.join(YEAR, day)
  if not os.path.exists(folder_path):
    os.mkdir(folder_path)

  answer_path = os.path.join(folder_path, 'answer.py')
  if not os.path.exists(answer_path):
    with open(answer_path, 'w') as f:
      f.write("""
\"\"\"
Write the question summary here
\"\"\"
              
test_data = \"\"\"

\"\"\".strip()
test_answer = 0
              

def solve_a(data):
  answer = 0
  return answer
              
def test_a():
  answer = solve_a(test_data)
  assert answer == test_answer, f"expected {test_answer} but got {answer}"

               
def solve_b(data):
  answer = 0
  return answer
              
def test_b():
  answer = solve_b(test_data)
  assert answer == test_answer, f"expected {test_answer} but got {answer}"

              
if __name__ == "__main__":
  test_a()
  test_b()
""")
    print(f"Created answer.py for {YEAR} Day {day}")

  input_file = os.path.join(folder_path, 'input.txt')
  if not os.path.exists(input_file):
    with open(input_file, 'w') as f:
      f.write("")
    print(f"Created input.txt for {YEAR} Day {day}")

  print(f"Ready for {YEAR} Day {day}")
