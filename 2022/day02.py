import codecs
import re
lines = [line.strip() for line in codecs.open("input/day02.txt",)]

score = 0
for line in lines:
    
    col1,col2 = re.search(r"(\w)\W(\w)", line).groups()
    if col1 == "A":
        if col2 == "Y": 
            score += 3
            score += 1
        elif col2 == "X":
            score += 3
        else:
            score += 6
            score += 2
    elif col1 == "B":
        if col2 == "Z":
            score += 6
            score += 3
        elif col2 == "Y":
            score += 3
            score += 2
        else:
            score += 1
    elif col1 == "C":
        if col2 == "X":
            score += 2
        elif col2 == "Z":
            score += 6
            score += 1
        else:
            score += 3
            score += 3
    print(score)