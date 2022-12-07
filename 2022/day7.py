import copy, json, math, regex

def create_dir(current, sim, caps):
  if len(current) == 0:
    sim[caps.captures("tar")[0]] = {}
  else:
    sim[current[0]] = create_dir(current[1:], sim[current[0]], caps)
  return sim

def create_file(current, sim, caps):
  if len(current) == 0:
    sim[caps.captures("tar")[0]] = int(caps.captures("com")[0])
  else:
    sim[current[0]] = create_file(current[1:], sim[current[0]], caps)
  return sim

def find_sizes(sim, count, summation):
  summ = 0
  temp = 0
  if type(sim) is int: return sim, count
  for key in sim.keys():
    if type(sim[key]) is int:
      summ += sim[key]
    else:
      sim[key], count, temp = find_sizes(sim[key], count, summation)
      summ += temp[-1]
  summation.append(summ)
  
  print(sim)
  return sim, count, summation

lines = [line.strip("\n") for line in open("input/day7.txt").readlines()]

sim = {"/":{},}
current = ["/",]


for line in lines:
  caps = regex.search(r"((?P<com>cd|dir|\d+|ls)\s?(?P<tar>[\w/\.]+)?)", line)

  if "ls" in caps.captures("com"): continue

  if "cd" in caps.captures("com"):
    if caps.captures("tar")[0] == "/": current = ["/",]; continue
    folders = caps.captures("tar")[0].split("/")
    for folder in folders:
      if folder == "..": current.pop(-1)
      else:
        current.append(folder)
  if "dir" in caps.captures("com"):
    sim = create_dir(current, sim, caps)
  if caps.captures("com")[0].isdigit():
    sim = create_file(current, sim, caps)

count = 0
summation = []
sim, count, summation = find_sizes(sim["/"], count, summation)
print(sum(filter(lambda x: x <= 100_000, summation)))

free = 30_000_000 - (70_000_000 - summation[-1])
temp = list(filter(lambda x: x >= free, summation))
print(min(temp))



  # caps_o = regex.search(r"(?P<o>.*)", line).captures("o")

  # print(groups)