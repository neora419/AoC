import copy, json, math, regex

lines = [line.strip("\n") for line in open("input/day15.txt").readlines()]

to_check = 10

pos = {}
pos["sensor_x"] = []
pos["sensor_y"] = []
pos["beacon_x"] = []
pos["beacon_y"] = []
pos["distance"] = []
for line in lines:
  caps = regex.search(r"S[\s\w]+x=(?P<Sx>-?\d+), y=(?P<Sy>-?\d+): clos[\s\w]+x=(?P<Bx>-?\d+), y=(?P<By>-?\d+)", line)
  dis_x = abs(int(caps.captures("Sx")[0]) - int(caps.captures("Bx")[0]))
  dis_y = abs(int(caps.captures("Sy")[0]) - int(caps.captures("By")[0]))
  dis = dis_x + dis_y
  if (int(caps.captures("Sy")[0]) + dis < to_check) or (int(caps.captures("Sy")[0]) - dis > to_check): continue
  pos["sensor_x"].append(int(caps.captures("Sx")[0]))
  pos["sensor_y"].append(int(caps.captures("Sy")[0]))
  pos["beacon_x"].append(int(caps.captures("Bx")[0]))
  pos["beacon_y"].append(int(caps.captures("By")[0]))
  pos["distance"].append(dis)

max_x = max(pos["beacon_x"]) if max(pos["beacon_x"]) > max(pos["sensor_x"]) else max(pos["sensor_x"])
min_x = min(pos["beacon_x"]) if min(pos["beacon_x"]) < min(pos["sensor_x"]) else min(pos["sensor_x"])
max_dis_x = max(pos["distance"])
line_to_check = []
for x in range(max_x - min_x + 1 + max_dis_x*2):
  line_to_check.append(".")

for i, _ in enumerate(pos["beacon_x"]):
  if pos["beacon_y"][i] == to_check: line_to_check[pos["beacon_x"][i] - min_x + max_dis_x] = "B"
  if pos["sensor_y"][i] == to_check: line_to_check[pos["sensor_x"][i] - min_x + max_dis_x] = "S"

  if pos["sensor_y"][i] > to_check:
    overshoot = abs(pos["sensor_y"][i] - pos["distance"][i] - to_check)
  else:
    overshoot = abs(pos["sensor_y"][i] + pos["distance"][i] - to_check)
  # print(overshoot)
  for j in range(-overshoot, overshoot + 1):
    if line_to_check[pos["sensor_x"][i] - min_x + max_dis_x +j] != ".": continue
    line_to_check[pos["sensor_x"][i] - min_x + max_dis_x +j] = "#"

# print("".join(line_to_check))
# print(max_dis_x, min_x)
print("part 1: ", len(list(filter(lambda x: x == "#", line_to_check))))

pos = {}
pos["sensor_x"] = []
pos["sensor_y"] = []
pos["beacon_x"] = []
pos["beacon_y"] = []
pos["distance"] = []

for line in lines:
  caps = regex.search(r"S[\s\w]+x=(?P<Sx>-?\d+), y=(?P<Sy>-?\d+): clos[\s\w]+x=(?P<Bx>-?\d+), y=(?P<By>-?\d+)", line)
  dis_x = abs(int(caps.captures("Sx")[0]) - int(caps.captures("Bx")[0]))
  dis_y = abs(int(caps.captures("Sy")[0]) - int(caps.captures("By")[0]))
  dis = dis_x + dis_y
  pos["sensor_x"].append(int(caps.captures("Sx")[0]))
  pos["sensor_y"].append(int(caps.captures("Sy")[0]))
  pos["beacon_x"].append(int(caps.captures("Bx")[0]))
  pos["beacon_y"].append(int(caps.captures("By")[0]))
  pos["distance"].append(dis)

possible = list(range(len(pos["beacon_x"])))
to_remove = []
count = 0
for i, _ in enumerate(pos["beacon_x"]):
  print(to_remove)
  dis = pos["distance"][i]
  for j, _ in enumerate(pos["beacon_x"]):
    dis_x = abs(pos["beacon_x"][i] - pos["sensor_x"][j])
    dis_y = abs(pos["beacon_y"][i] - pos["sensor_y"][j])
    dis_to_j = dis_x + dis_y
    if dis >= dis_to_j:
      to_remove.append(j)

for rem in to_remove:
  if rem in possible:
    possible.remove(rem)
  print(possible)

print(possible)

