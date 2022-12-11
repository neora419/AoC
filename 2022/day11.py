import copy, json, math, regex

lines = [line.strip("\n") for line in open("input/day11.txt").readlines()]

ops = {"+":sum, "*":math.prod}
monkeys = open("input/day11.txt").read().split("\n\n")
mons = []
for j, monkey in enumerate(monkeys):
  mons.append({})
  mlines = monkey.split("\n")
  mons[j]["i"] = int(regex.search(r"(?P<i>\d+)", mlines[0]).captures("i")[0])
  mons[j]["start"] = [int(num.strip().strip(",")) for num in regex.search(r"(?P<start>\d+,? ?)+", mlines[1]).captures("start")]
  mons[j]["op"] = regex.search(r"new = (?P<op>.+)", mlines[2]).captures("op")[0].split()
  mons[j]["div"] = int(regex.search(r"by (?P<div>\d+)", mlines[3]).captures("div")[0])
  mons[j]["true"] = int(regex.search(r"key (?P<true>\d+)", mlines[4]).captures("true")[0])
  mons[j]["false"] = int(regex.search(r"key (?P<false>\d+)", mlines[5]).captures("false")[0])
  mons[j]["ins_count"] = 0

list1 = [mon["div"] for mon in mons]
foo = math.prod(list1)
for u in range(10_000):
  for k, mon in enumerate(mons):
    mon["ins_count"] += len(mon["start"])
    for i, item_lvl in enumerate(mon["start"]):
      nums = []
      nums.append(int(item_lvl) if mon["op"][0] == "old" else int(mon["op"][0]))
      nums.append(int(item_lvl) if mon["op"][2] == "old" else int(mon["op"][2]))
      worry = math.floor(ops[mon["op"][1]](nums))
      if worry % mon["div"] == 0:
        mons[mon["true"]]["start"].append(worry % foo)
        assert mon["true"] != k
      else:
        mons[mon["false"]]["start"].append(worry % foo)
        assert mon["true"] != k
    mon["start"] = []
        
res = [mon["ins_count"] for mon in sorted(mons, key=lambda mon: mon["ins_count"], reverse=True)]
print(math.prod(res[:2]))