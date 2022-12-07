import copy, math, regex

lines = [line.strip("\n") for line in open("input/day6.txt").readlines()]
line = lines[0]

recent_chars = []
recent_chars_p2 = []

for i, char in enumerate(line, start=1):
  recent_chars.append(char)
  
  if len(recent_chars) > 4:
    recent_chars.pop(0)
  temp = []
  for recent_char in recent_chars:
    if recent_char not in temp:
      temp.append(recent_char)
  recent_chars_p2.append(char)
  if len(recent_chars_p2) > 14:
    recent_chars_p2.pop(0)
  if len(temp) < 4: continue
  # print(i)
  
  
  
  temp = []
  for recent_char in recent_chars_p2:
    if recent_char not in temp:
      temp.append(recent_char)
  lenn = len(temp)
  if len(temp) < 14: continue
  print(i)
  break
  
  # groups = regex.search(r"(.*)", line).groups()
  # caps_o = regex.search(r"(?P<o>.*)", line).captures("o")

  # print(groups)