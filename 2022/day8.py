import copy, json, math, regex

lines = [line.strip("\n") for line in open("input/day8.txt").readlines()]

vis_map = {}
start = len(lines)*2+len(lines[0])*2-4
count = 0

#from top
for x, _ in enumerate(lines[0]):
  if x == 0 or x == len(lines[0]) - 1: continue
  highest_y = int(lines[0][x])
  for y, _ in enumerate(lines):
    if y == 0 or y == len(lines) - 1: continue
    if int(lines[y][x]) > highest_y:
      count += 1
      vis_map[f"{x} {y}"] = int(lines[y][x])
      highest_y = int(lines[y][x])
reverse = list(range(len(lines)))
reverse.sort(reverse=True)

# from bottom
for x, _ in enumerate(lines[0]):
  if x == 0 or x == len(lines[0]) - 1: continue
  highest_y = int(lines[-1][x])
  for y in reverse:
    if y == 0 or y == len(lines) - 1: continue
    if int(lines[y][x]) > highest_y:
      count += 1
      vis_map[f"{x} {y}"] = int(lines[y][x])
      highest_y = int(lines[y][x])

#from left
for y, _ in enumerate(lines):
  if y == 0 or y == len(lines) - 1: continue
  highest_x = int(lines[y][0])
  for x, _ in enumerate(lines[0]):
    if x == 0 or x == len(lines[0]) - 1: continue
    if int(lines[y][x]) > highest_x:
      count += 1
      vis_map[f"{x} {y}"] = int(lines[y][x])
      highest_x = int(lines[y][x])

reverse = list(range(len(lines[0])))
reverse.sort(reverse=True)

#from right
for y, _ in enumerate(lines):
  if y == 0 or y == len(lines) - 1: continue
  highest_x = int(lines[y][-1])
  for x in reverse:
    if x == 0 or x == len(lines[0]) - 1: continue
    if int(lines[y][x]) > highest_x:
      count += 1
      vis_map[f"{x} {y}"] = int(lines[y][x])
      highest_x = int(lines[y][x])

print(len(list(filter(lambda x: x > -1, vis_map.values()))) + start)


for key in vis_map.keys():
  # print(key)
  x, y = key.split()
  reverse = list(range(int(y)))
  # print(reverse)
  reverse.sort(reverse=True)
  i = 0
  for top in reverse:
    # print(int(x), top)
    # print(vis_map[key], lines[top][int(x)])
    if int(lines[top][int(x)]) >= int(lines[int(y)][int(x)]):
      i += 1
      break
    i += 1
  vis_map[key] = i
  # print(i)
  i = 0
  for bottom in range(int(y) + 1, len(lines)):
    # print(int(x), bottom)
    # print(vis_map[key], lines[bottom][int(x)])
    if int(lines[bottom][int(x)]) >= int(lines[int(y)][int(x)]):
      i += 1
      break
    i += 1
  vis_map[key] *= i
  # print(i)

  reverse = list(range(int(x)))
  reverse.sort(reverse=True)
  i = 0
  for left in reverse:
    # print(left)
    if int(lines[int(y)][left]) >= int(lines[int(y)][int(x)]):
      i += 1
      break
    i += 1
  vis_map[key] *= i
  # print(i)
  i = 0
  for right in range(int(x) + 1, len(lines[0])):
    # print(right)
    if int(lines[int(y)][right]) >= int(lines[int(y)][int(x)]):
      i += 1
      break
    i += 1
  vis_map[key] *= i
  # print(i)
  # print(vis_map)
print(max(vis_map.values()))
  



  # caps = regex.search(r"((?P<com>cd|dir|\d+|ls)\s?(?P<tar>[\w/\.]+)?)", line)

  # if "ls" in caps.captures("com"): continue
