import datetime
import os
import subprocess


AOC_NOW = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=5)
YEAR = str(AOC_NOW.year)
DAY = str(AOC_NOW.day)

def commit_and_push(year, day, message=None, push=False):
    day = day.zfill(2)
    folder_path = os.path.join(year, day)

    if not os.path.exists(folder_path):
        print(f"No solution found for {year} Day {day}")
        return

    if message is None:
        message = f"{year}/{day}"

    try:
        subprocess.run(['git', 'add', folder_path], check=True)
        subprocess.run(['git', 'commit', '-m', message], check=True)
        if push:
          subprocess.run(['git', 'push'], check=True)
        
        r = f"Changes for {year} Day {day} have been committed"
        if push:
            r += " and pushed"
        print(r)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    commit_and_push(YEAR, DAY)