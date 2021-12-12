import os

caves = ["""start-A
start-b
A-c
A-b
b-d
A-end
b-end""", """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""", """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""", """ey-dv
AL-ms
ey-lx
zw-YT
hm-zw
start-YT
start-ms
dv-YT
hm-ms
end-ey
AL-ey
end-hm
rh-hm
dv-ms
AL-dv
ey-SP
hm-lx
dv-start
end-lx
zw-AL
hm-AL
lx-zw
ey-zw
zw-dv
YT-ms"""]

def build_possible_paths_from_cave_map(map):
   possible_ways = {}
   cave_map = map.split("\n")
   for path in cave_map:
      path_split = path.split("-")
      if path_split[0] != "end":
         if path_split[0] not in possible_ways.keys():
            possible_ways[path_split[0]] = []
         if path_split[1] != "start":
            possible_ways[path_split[0]].append(path_split[1])
      if path_split[1] != "end":
         if path_split[1] not in possible_ways.keys():
            possible_ways[path_split[1]] = []
         if path_split[0] != "start":
            possible_ways[path_split[1]].append(path_split[0])
   return possible_ways

def loop_all_path_from_point(possible_ways, actual_route, solutions):
   if actual_route[-1] != "end":
      for next_position in possible_ways[actual_route[-1]]:
         if next_position.isupper() or next_position not in actual_route:
            actual_route.append(next_position)
            solutions, actual_route = loop_all_path_from_point(possible_ways, actual_route, solutions)
            actual_route.pop()
   else:
      solutions.append(actual_route.copy())
   return solutions, actual_route

def are_there_lower_duplicates(route):
   only_lowers = [x for x in route if x.islower()]
   return len(only_lowers) > len(set(only_lowers))
   
def loop_all_path_from_point_one_small_cave_twice(possible_ways, actual_route, solutions):
   if actual_route[-1] != "end":
      for next_position in possible_ways[actual_route[-1]]:
         if next_position.isupper() or next_position not in actual_route or not are_there_lower_duplicates(actual_route):
            actual_route.append(next_position)
            solutions, actual_route = loop_all_path_from_point_one_small_cave_twice(possible_ways, actual_route, solutions)
            actual_route.pop()
   else:
      solutions.append(actual_route.copy())
   return solutions, actual_route
   
def first_star(cave):
   possible_ways = build_possible_paths_from_cave_map(cave)
   routes, last_route = loop_all_path_from_point(possible_ways, ["start"], [])
   return(len(routes))

def second_star(cave):
   possible_ways = build_possible_paths_from_cave_map(cave)
   routes, last_route = loop_all_path_from_point_one_small_cave_twice(possible_ways, ["start"], [])
   return(len(routes))

def run_two_stars(cave):
   result = first_star(cave)
   print(f"DATA: {cave[:10]}..., first_star: {result}")
   result = second_star(cave)
   print(f"DATA: {cave[:10]}..., second_star: {result}")

def main():
   for cave in caves:
      run_two_stars(cave)

if __name__ == "__main__":
   main()