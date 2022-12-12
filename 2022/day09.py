import copy, json, math, regex

lines = [line.strip("\n") for line in open("input/day09.txt").readlines()]

def map_data(lines):
  map_val = [[]]
  for x, _ in enumerate(lines[0]):
    map_val.append([])
    for y, char in enumerate(lines[x]):
      map_val[x].append(int(char))
      assert map_val[x][y] == int(char), "mapping failed!"
  return map_val

head = [0, 0]
tail = [0, 0]
knots = [[0, 0],]
for _ in range(9):
  knots.append([0, 0])
print(len(knots))
history = {}
history["0 0"] = 1
history_1 = {}
history_1["0 0"] = 1
for line in lines:
  com, val = line.split()
  for step in range(int(val)):
    if com == "U":
      knots[0][1] += 1
    if com == "D":
      knots[0][1] -= 1
    if com == "R":
      knots[0][0] += 1
    if com == "L":
      knots[0][0] -= 1
    for i, knot in enumerate(knots):
      if i == 0: continue
      diff_x = abs(knots[i - 1][0] - knots[i][0])
      diff_y = abs(knots[i - 1][1] - knots[i][1])
      # print("head: ", head)

      # print(diff_x,diff_y)
      if (diff_x > 0 and diff_y > 0) and (diff_x > 1 or diff_y > 1):
        if knots[i - 1][0] > knots[i][0] and knots[i - 1][1] > knots[i][1]:
          knots[i][0] += 1
          knots[i][1] += 1 
        elif knots[i - 1][0] < knots[i][0] and knots[i - 1][1] < knots[i][1]:
          knots[i][0] -= 1
          knots[i][1] -= 1
        elif knots[i - 1][1] > knots[i][1] and knots[i - 1][0] < knots[i][0]:
          knots[i][0] -= 1
          knots[i][1] += 1
        elif knots[i - 1][1] < knots[i][1] and knots[i - 1][0] > knots[i][0]:
          knots[i][0] += 1
          knots[i][1] -= 1
        # print("tail: ",tail)
        diff_x = abs(knots[i - 1][0] - knots[i][0])
        diff_y = abs(knots[i - 1][1] - knots[i][1])


      if diff_x > 1 or diff_y > 1:
        if diff_x == 0: pass
        elif knots[i - 1][0] > knots[i][0]:
          knots[i][0] += 1
        elif knots[i - 1][0] < knots[i][0]:
          knots[i][0] -= 1
        if diff_y == 0: pass
        elif knots[i - 1][1] > knots[i][1]:
          knots[i][1] += 1
        elif knots[i - 1][1] < knots[i][1]:
          knots[i][1] -= 1
      if i == 1:
        history_1[f"{knots[i][0]} {knots[i][1]}"] = 1
      elif i == len(knots) - 1:
        history[f"{knots[i][0]} {knots[i][1]}"] = 1
      # print("tail: ",tail)
# print(history.keys())
print("part 1: ", len(history_1.keys()))
print("part 2: ", len(history.keys()))




  # caps = regex.search(r"((?P<com>cd|dir|\d+|ls)\s?(?P<tar>[\w/\.]+)?)", line)

  # if "ls" in caps.captures("com"): continue