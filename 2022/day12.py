import copy, json, math, regex, string

lines = [line.strip("\n") for line in open("input/day12.txt").readlines()]

def map_data(lines):
  map_val = []
  map_val2 = []
  for x, _ in enumerate(lines):
    map_val.append([])
    map_val2.append([])
    for y, char in enumerate(lines[x]):
      map_val[x].append(char)
      map_val2[x].append(True)
      assert map_val[x][y] == char, "mapping failed!"
  return map_val, map_val2
start = []
a_z_values = {a:i for i, a in enumerate(string.ascii_lowercase)}
height_map, been_map = map_data(lines)
for x, _ in enumerate(height_map):
  for y, char in enumerate(height_map[x]):
    if "E" == char:
      start = (x, y)

res = []
def is_climbable(height_map, current, a, b):
  # if ("S" == height_map[current[0]][current[1]]) or ("S" == height_map[a][b]): return True
  # if ("E" == height_map[current[0]][current[1]]) or ("E" == height_map[a][b]): return True
  one = height_map[current[0]][current[1]]
  two = height_map[a][b]
  a_z_values = {a:i for i, a in enumerate(string.ascii_lowercase)}
  a_z_values["S"] = 0
  a_z_values["E"] = 25
  diff = a_z_values[one] - a_z_values[two]
  if diff <=1:
    if two == "a":
      print("part 2: ", i)
    if a_z_values[one] == 0: pass
    return True
  else:
    return False

end = ()
for x, _ in enumerate(height_map):
  for y, char in enumerate(height_map[x]):
    if "S" == char:
      end = (x, y)
# test = {}
# test.keys()
been_to_list = [start,]


print(start)
for i in range(1, 1000):
  # if i % 20 == 0:
  # print(i)
  temp_list = copy.deepcopy(been_to_list)
  for l, been_to in enumerate(temp_list):
    if been_to[0] != 0:
      if been_map[been_to[0] - 1][been_to[1]]:
        if is_climbable(height_map, been_to, been_to[0] - 1, been_to[1]): 
          been_to_list.append((been_to[0] - 1, been_to[1]))
          been_map[been_to[0] - 1][been_to[1]] = False
    if been_to[0] != len(height_map) - 1:
      if been_map[been_to[0] + 1][been_to[1]]:
        if is_climbable(height_map, been_to, been_to[0] + 1, been_to[1]): 
          been_to_list.append((been_to[0] + 1, been_to[1]))
          been_map[been_to[0] + 1][been_to[1]] = False

    if been_to[1] != 0:
      if been_map[been_to[0]][been_to[1] - 1]:
        if is_climbable(height_map, been_to, been_to[0], been_to[1] - 1):
          been_to_list.append((been_to[0], been_to[1] - 1))
          been_map[been_to[0]][been_to[1] - 1] = False
    if been_to[1] != len(height_map[0]) - 1:
      if been_map[been_to[0]][been_to[1] + 1]:
        if is_climbable(height_map, been_to, been_to[0], been_to[1] + 1):
          been_to_list.append((been_to[0], been_to[1] + 1))
          been_map[been_to[0]][been_to[1] + 1] = False
    
  # print(been_to_list)
    
  if end in been_to_list:
    print(i)
    # print(been_to_list)
    print(start)
    res.append(i)
    break
    

print(sorted(res))
    # caps = regex.search(r"((?P<com>cd|dir|\d+|ls)\s?(?P<tar>[\w/\.]+)?)", line)

    # if "ls" in caps.captures("com"): continue