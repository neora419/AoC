import codecs
import re
import math
import string
lines = [line.strip() for line in codecs.open("input/day03.txt",)]

score = 0
j = 0
linegroup = []

for i in range(len(lines)):
    print(j)
    commonlist = []
    line1 = lines[j]
    line2 = lines[j+1]
    line3 = lines[j+2]
    
    print(line1)
    for char in line1:
        if line2.find(char) != -1:
            for char2 in line3:
                if char2 == char:
                    commonlist += char
    print(commonlist)
            
    i = 1
    for char in string.ascii_lowercase:
        if char == commonlist[0]:
            score += i
            break
        i += 1
    i = 27
    for char in string.ascii_uppercase:
        if char == commonlist[0]:
            score += i
            break
        i += 1
    print(score)
    j += 3
    if j>= len(lines):
        break
# for line in lines:
#     j += 1
#     if j % 3 == 0:
#         print(j)
#         linegroup = []
#     part1 = line[:math.floor(len(line)/2)]
#     part2 = line[math.floor(len(line)/2):]
#     commonlist = []
#     for char in part1:
#         if part2.find(char) != -1:
#             commonlist += part2[part2.find(char)]
#     linegroup += line
#     print(linegroup)
#     i = 1
#     for char in string.ascii_lowercase:
#         if char == commonlist[0]:
#             score += i
#             break
#         i += 1
#     i = 27
#     for char in string.ascii_uppercase:
#         if char == commonlist[0]:
#             score += i
#             break
#         i += 1
#     print(score)
    
# print(score)
# print(string.ascii_lowercase)
    # col1,col2 = re.search(r"(\w)\W(\w)", line).groups()