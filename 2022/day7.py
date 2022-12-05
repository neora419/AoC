import regex
import math

lines = [line.strip("\n") for line in open("input/day7.txt").readlines()]

for line in lines:
  groups = regex.search(r"(.*)", line).groups()
  caps_o = regex.search(r"(?P<o>.*)", line).captures("o")

  print(groups)