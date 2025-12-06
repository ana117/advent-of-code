import datetime
import os
import importlib.util


AOC_NOW = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=5)
YEAR = str(AOC_NOW.year)
DAY = str(AOC_NOW.day)


def run(year, day):
  day = day.zfill(2)
  folder_path = os.path.join(year, day)
  answer_path = os.path.join(folder_path, 'answer.py')

  if not os.path.exists(answer_path):
    print(f"No solution found for {year} Day {day}")

  else:
    spec = importlib.util.spec_from_file_location("answer", answer_path)
    answer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(answer)
    
    input_file = os.path.join(folder_path, 'input.txt')
    with open(input_file, 'r') as f:
        input_data = f.read().strip()
    
    answer.test_a()
    print(f"Part 1 solution for {year} Day {day}: {answer.solve_a(input_data)}")

    if hasattr(answer, 'solve_b'):
      answer.test_b()
      print(f"Part 2 solution for {year} Day {day}: {answer.solve_b(input_data)}")


if __name__ == "__main__":
  run(YEAR, DAY)
