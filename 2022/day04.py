import codecs
import re
import math
import string
lines = [line.strip() for line in codecs.open("input/day04.txt",)]

score = 0

for line in lines:
    
    groups = re.search(r"(\d+)-(\d+),(\d+)-(\d+)",line).groups()
    print(groups)
    elf1 = tuple(range(int(groups[0]),int(groups[1])+1))
    elf2 = tuple(range(int(groups[2]),int(groups[3])+1))
    print(elf1,elf2)
    len1 = len(elf1)
    len2 = len(elf2)
    res = elf1 + elf2
    con = tuple(set(res))
    if len(con) != len1 + len2:
        score += 1
    print(score)