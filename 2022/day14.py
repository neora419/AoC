import copy, json, math, regex

# lines = [line.strip("\n") for line in open("input/day8.txt").readlines()]

def map_data(lines):
  map_val = [[]]
  for x, _ in enumerate(lines[0]):
    map_val.append([])
    for y, char in enumerate(lines[x]):
      map_val[x].append(int(char))
      assert map_val[x][y] == int(char), "mapping failed!"
  return map_val

paths = [line.split(" -> ") for line in open("input/day14.txt").read().split("\n") if line != ""]

y_list = []
for path in paths:
  for coord in path:
    y_list.append(int(coord.split(",")[1]))
y_list.append(0)
min_y = min(y_list)
max_y = max(y_list)

paths.append([f"0, {max_y + 2}", f"10000, {max_y + 2}"])

y_list = []
for path in paths:
  for coord in path:
    y_list.append(int(coord.split(",")[1]))
y_list.append(0)
min_y = min(y_list)
max_y = max(y_list)

x_list = []
for path in paths:
  for coord in path:
    x_list.append(int(coord.split(",")[0]))
min_x = min(x_list)
max_x = max(x_list)

map = []
for x in range(max_x - min_x + 1):
  map.append([])
  for y in range(max_y - min_y + 1):
    map[x].append(".")


for path in paths:
  print(path)
  temp_x = -1
  temp_y = -1
  for point in path:
    x_path = int(point.split(",")[0]) - min_x
    y_path = int(point.split(",")[1]) - min_y

    if temp_x != x_path and temp_x != -1:
      if x_path >= temp_x:
        for x in range(temp_x, x_path + 1):
          map[x][y_path] = "#"
      if x_path < temp_x:
        for x in range(x_path, temp_x + 1):
          map[x][y_path] = "#"
    if temp_y != y_path and temp_y != -1:
      if y_path >= temp_y:
        for y in range(temp_y, y_path + 1):
          map[x_path][y] = "#"
      if y_path < temp_y:
        for y in range(y_path, temp_y + 1):
          map[x_path][y] = "#"

    temp_x = x_path
    temp_y = y_path

assert map[500 - min_x][0 - min_y] != "#"
map[500 - min_x][0 - min_y] = "+"
source = (500 - min_x, 0 - min_y)

unit = -1
overflow = False
while not overflow:
  unit += 1
  if map[source[0]][source[1]] == "o":
    print(unit)
    break
  curr_sand = source
  print(unit)
  is_falling = True
  while is_falling:
    x = curr_sand[0]
    y = curr_sand[1]
    map[x][y] = "o"
    try:
      if map[x][y + 1] == ".":
        curr_sand = (x, y + 1)
        map[x][y] = "."
        continue
      elif map[x - 1][y + 1] == ".":
        if x == 0:
          overflow = True
          break
        curr_sand = (x - 1, y + 1)
        map[x][y] = "."
        continue
      elif map[x + 1][y + 1] == ".":
        curr_sand = (x + 1, y + 1)
        map[x][y] = "."
        continue
      is_falling = False
    except:
      overflow = True
      break
      
      


print(overflow, unit)
# print(map)

  # caps = regex.search(r"((?P<com>cd|dir|\d+|ls)\s?(?P<tar>[\w/\.]+)?)", line)

  # if "ls" in caps.captures("com"): continue