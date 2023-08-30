
test = int(input())

for item in range(test):
  courses, units, chapters = map(int, input().split())
  total_chapters = courses * units * chapters
  print(total_chapters)