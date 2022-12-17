import copy, json, math, regex
def run():
  lines = [line.strip("\n") for line in open("input/day17.txt").readlines()]

  def map_data(lines):
    map_val = [[]]
    for x, _ in enumerate(lines[0]):
      map_val.append([])
      for y, char in enumerate(lines[x]):
        map_val[x].append(int(char))
        assert map_val[x][y] == int(char), "mapping failed!"
    return map_val

  input = lines[0]
  width = 7

  map = [[]]
  for y in range(width):
    map[0].append("-")

  rocks = [
    [["#","#","#","#"]],
    
    [[".","#","."],
    ["#","#","#"],
    [".","#","."]],
    
    [[".",".","#"],
    [".",".","#"],
    ["#","#","#"]],
    
    [["#"],
    ["#"],
    ["#"],
    ["#"]],
    
    [["#","#"],
    ["#","#"]]
  ]
    
  print(map)
  nr = 0

  def move_rock(dir, rock, width, map):
    is_falling = True
    temp_rock = copy.deepcopy(rock)
    if dir == ">":
      if max([x[1] for x in rock]) < width - 1:
        rock = [[x[0],x[1]+1] for x in rock]
        # print(rock)
        for point in rock:
          if map[point[0]][point[1]] != ".":
            is_falling = False
            # map = draw_rock(map, temp_rock)
            break
    elif dir == "<":
      if min([x[1] for x in rock]) > 0:
        rock = [[x[0],x[1]-1] for x in rock]
        # print(rock)
        for point in rock:
          if map[point[0]][point[1]] != ".":
            is_falling = False
            # map = draw_rock(map, temp_rock)
            break
    elif dir == "down":
      if min([x[0] for x in rock]) < len(map):
        rock = [[x[0]+1,x[1]] for x in rock]
        # print(rock)
        for point in rock:
          if map[point[0]][point[1]] != ".":
            is_falling = False
            # map = draw_rock(map, temp_rock)
            break
    else: assert False == True
    if not is_falling:
      rock = copy.deepcopy(temp_rock)
    return map, rock, is_falling

  def draw_rock(map:list, rock:list):
    for point in rock:
      map[point[0]][point[1]] = "#"
    return map

  rock_count = -1
  wind_count = 0
  while True:
    rock_count += 1
    rock_img = copy.deepcopy(rocks[rock_count % 5])
    rock_img.reverse()
    rock = []
    # height = 0
    # get highest point
    for i in range(len(map)):
      if ("#" in map[i]) or ("-" in map[i]):
        highest_point = i
        break
    # draw new lines
    for i in range(highest_point):
      map.pop(0)
      # height -= 1
    if rock_count == 2022: 
      break
    limit = 3
    height = 3 + len(rock_img) + len(map)
    k = 0
    for i in range(3 + len(rock_img)):
      map.insert(0, [])
      for j in range(width):
        if (2 <= j and j <= len(rock_img[0]) + 1) and limit <= i:
          # map[0].append(rock_img[k][j-2])
          if rock_img[k][j-2] == "#":
            rock.append([height - len(map), j])
        map[0].append(".")
      if limit <= i:
        k += 1
    # print(rock)
    is_falling = True
    while is_falling:
      dir = input[wind_count % len(input)]
      # print(wind_count % len(input))
      if wind_count % len(input) == 0:
        assert dir == ">"
      map, rock, is_falling = move_rock(dir, rock, width, map)
      # print(dir, rock)
      wind_count += 1
      # if not is_falling:
      #   break
      # fall
      map, rock, is_falling = move_rock("down", rock, width, map)
      # print(rock)
    map = draw_rock(map, rock)
    print(rock_count)
  print(len(map)-1)
      
      
        
    
    # let_rocks_fall(map, highest_point, nr % 5)
    
run()
  