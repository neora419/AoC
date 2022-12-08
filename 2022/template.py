import copy, json, math, regex

lines = [line.strip("\n") for line in open("input/day8.txt").readlines()]

map_val = [[]]
for x, _ in enumerate(lines[0]):
  map_val.append([])
  for y, char in enumerate(lines[x]):
    map_val[x].append(int(char))
    assert map_val[x][y] == int(char), "mapping failed!"


  # caps = regex.search(r"((?P<com>cd|dir|\d+|ls)\s?(?P<tar>[\w/\.]+)?)", line)

  # if "ls" in caps.captures("com"): continue