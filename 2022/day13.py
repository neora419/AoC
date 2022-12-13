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

def find_end(string):
  list1 = 0
  for i, char in enumerate(string):
    if char == "[":
      list1 += 1
    elif char == "]":
      list1 -= 1
    if list1 == 0:
      return i

def compare(string1, string2):
  res = 0
  while res == 0:
    if string1.startswith(","): string1 = string1[1:]
    if string2.startswith(","): string2 = string2[1:]
    # print(string1, string2)
    if not string1 and not string2:
      return 0
    if not string1:
      return 1
    if not string2:
      return 2
    if string1[0] == "[" and string2[0] == "[":
      ending1 = find_end(string1)
      ending2 = find_end(string2)
      res = compare(string1[1:ending1], string2[1:ending2])
      if res == 1: return 1
      if res == 2: return 2
      string1 = string1[ending1+1:]
      string2 = string2[ending2+1:]
      continue
    elif string1[0] == "[" and string2[0] != "[":
      ending1 = find_end(string1)
      komma2 = string2.find(",")
      if komma2 == -1:
        res = compare(string1[1:ending1], string2)
      else:
        res = compare(string1[1:ending1], string2[:komma2])
      if res == 1: return 1
      if res == 2: return 2
      string1 = string1[ending1+1:]
      string2 = string2[komma2:]
      continue
    elif string1[0] != "[" and string2[0] == "[":
      komma1 = string1.find(",")
      ending2 = find_end(string2)
      if komma1 == -1:
        res = compare(string1, string2[1:ending2])
      else:
        res = compare(string1[:komma1], string2[1:ending2])
      if res == 1: return 1
      if res == 2: return 2
      string1 = string1[komma1:]
      string2 = string2[ending2+1:]
      continue
    # komma1 = string1.find(",")
    # komma2 = string2.find(",")
    num1 = string1.split(",")[0]
    num2 = string2.split(",")[0]
    if int(num1) < int(num2): return 1
    if int(num1) > int(num2): return 2
    if string1.find(",") == -1 and string2.find(",") == -1:
      return 0
    if string1.find(",") == -1:
      return 1
    if string2.find(",") == -1:
      return 2
    res = compare(string1[string1.find(",")+1:], string2[string2.find(",")+1:])
    string1 = string1[string1.find(",")+1:]
    string2 = string2[string2.find(",")+1:]
  return res
    
def get_comp(string1, string2):
  res = compare(string1, string2)
  if res == 1: return -1
  if res == 2: return 1
  assert 1 == 0
  return 0


pairs = [pair.split() for pair in open("input/day13.txt").read().split("\n\n")]

sum = 0
for i, pair in enumerate(pairs, start=1):
  res = compare(pair[0], pair[1])
  if res == 1:
    # print(i, True)
    sum += i
  # if res == 2:
  #   print(i, False)
print(sum)

pairs = [pair for pair in open("input/day13.txt").read().split()]
pairs.append("[[2]]")
pairs.append("[[6]]")
order = []
import functools as tools
order = sorted(pairs, key=tools.cmp_to_key(get_comp))

# WHY NOT +1 ON THE TWO??!!!?!?!
two = order.index("[[2]]")
six = order.index("[[6]]")+1
print(two * six)
