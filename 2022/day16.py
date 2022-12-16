import copy, json, math, regex

lines = [line.strip("\n") for line in open("input/day16.txt").readlines()]

def map_data(lines):
  map_val = [[]]
  for x, _ in enumerate(lines[0]):
    map_val.append([])
    for y, char in enumerate(lines[x]):
      map_val[x].append(int(char))
      assert map_val[x][y] == int(char), "mapping failed!"
  return map_val

options = {}

for line in lines:
  caps = regex.search(r"Valve (?P<curr>\w+).+=(?P<rate>\d+); .+ valves? ((?P<valves>\w+),? ?)+", line)
  options[caps.captures("curr")[0]] = {}
  options[caps.captures("curr")[0]]["rate"] = caps.captures("rate")[0]
  options[caps.captures("curr")[0]]["valves"] = caps.captures("valves")

curr = "AA"
tar = "HH"
been_to = []
def find_path(options:dict, curr:str, tar:str, been_to:list, step:int, paths:list, i:int) -> list:
  print(paths)
  if curr == tar:
    i += 1
    paths.append([])
    return step, paths, i
  if curr in been_to:
    return -1, paths, i
  been_to.append(curr)
  poss = options[curr]["valves"]
  step += 1
  ret = []
  for tunnel in poss:
    path_copy = copy.deepcopy(paths[i])
    paths[i].append(tunnel)
    temp = find_path(options, tunnel, tar, been_to, step, paths, i)
    ret.append(temp[0])
    if temp[0] == -1: paths[i] = copy.deepcopy(path_copy); ret.pop(-1); continue
    if temp[0] > min(ret): paths[i] = copy.deepcopy(path_copy); ret.pop(-1); continue
    step = temp[0]
    paths = temp[1]
    i = temp[2]
    print(paths)
  return step, paths, i



print(find_path(options, curr, tar, been_to, 0, [[]], 0))


for minute in range(1, 31).__reversed__():
  print(minute)

  
