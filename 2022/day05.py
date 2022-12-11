import copy,regex

lines = [line.strip("\n") for line in open("input/day05.txt").readlines()]

stacks = []
header_count = 0
for line in lines:
  if not line: break

  search = regex.search(r"((?P<o>\s{3}|\[\w\])(?P<o> \s{3}| \[\w\])+)|( (\d)(   \d)+)", line)
  groups = search.groups()
  captures = search.captures("o")
  if header_count == 0:
    for cap in captures:
      stacks.append([])
  for i, cap in enumerate(captures):
    if cap:
      if cap.strip():
        stacks[i].append(cap.strip().strip("[]"))
  header_count += 1
  
stacks2 = copy.deepcopy(stacks)

for line in lines:
  if header_count >= 0: header_count -= 1; continue
  count,source,dest = regex.search(r"move (\d+) from (\d+) to (\d+)", line).groups()
  j = 0
  for i in range(int(count)):
    stacks[int(dest)-1].insert(0, stacks[int(source)-1][j])
    stacks2[int(dest)-1].insert(j, stacks2[int(source)-1][j])
    j += 1
  for i in range(j):
    stacks[int(source)-1].pop(0)
    stacks2[int(source)-1].pop(0)
print("part 1: "," ".join((stack[0] for stack in stacks)))
print("part 2: "," ".join((stack[0] for stack in stacks2)))
