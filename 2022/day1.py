lines = [line.strip() for line in open("input/day1.txt").readlines()]

count_per_elf = []

count_per_elf.append(0)
for line in lines:
  if not line:
    count_per_elf.append(0)
    continue
  count_per_elf[-1] += int(line)

count_per_elf.sort()

print(count_per_elf[-1])
print(sum(count_per_elf[-3:]))