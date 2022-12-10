import copy, json, math, regex

lines = [line.strip("\n") for line in open("input/day10.txt").readlines()]

def map_data(lines):
  map_val = [[]]
  for x, _ in enumerate(lines[0]):
    map_val.append([])
    for y, char in enumerate(lines[x]):
      map_val[x].append(int(char))
      assert map_val[x][y] == int(char), "mapping failed!"
  return map_val

grid = []
for y in range(6):
  grid.append("")
  for x in range(40):
    grid[y] += " "

def draw(grid, i, x):
  y = math.floor(i / 40)
  row = (i % 40) - 1
  diff = abs(x - row)
  if diff <= 1: 
    list1 = list(grid[y])
    list1[row] = "#"
    grid[y] = "".join(list1)
    print("\n"+"\n".join(grid))
  return grid

x = 1
score = []
counter = 20
i = 0
for line in lines:
  i += 1
  draw(grid, i, x)
  if i % 40 == 20:
    score.append(i * x)
    print("cycle: ", i)
    print(score)
  com, val = regex.search(r"(?P<com>noop|addx)\s?(?P<val>[-\d]+)?", line).groups()
  # com = caps.captures("com")[0]
  # val = caps.captures("val")[0]
  if com in "addx":
    i += 1
    draw(grid, i, x)
    if i % 40 == 20:
      score.append(i * x)
      print("cycle: ", i)
      print(score)
    
    x += int(val)
  elif com == "noop":
    pass
  else:
    print(line)
    input()
print(sum(score))
print("\n".join(grid))
  


  # if "ls" in caps.captures("com"): continue