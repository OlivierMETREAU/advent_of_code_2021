from pandas import *

def pretty_print_2d_table(matrix):
   print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

def read_data_from_file(file_path):
   f = open(file_path, "r")
   lines = f.read().splitlines()
   paths = []
   max_coordinate = 0
   for line in lines:
      coordinates = line.split()
      origin = [int(x) for x in coordinates[0].split(",")]
      destination = [int(x) for x in coordinates[2].split(",")]
      max_coordinate = max(max_coordinate, origin[0], origin[1], destination[0], destination[1])
      paths.append([origin, destination])
   return paths, max_coordinate

def horizontal_path(paths_map, row_index, y1, length):
   for y in range(y1, y1 + length + 1):
      paths_map[row_index][y] += 1
   return paths_map

def vertical_path(paths_map, col_index, x1, length):
   for x in range(x1, x1 + length + 1):
      paths_map[x][col_index] += 1
   return paths_map

def diag_path(paths_map, x1, x2, y1, y2):
   x_increment = 1 if x2 >= x1 else -1
   y_increment = 1 if y2 >= y1 else -1
   position = 0
   for x in range(x1, x2 + x_increment, x_increment):
      paths_map[x][y1 + position * y_increment] += 1
      position += 1
   return paths_map

def count_two_lines_overlap(paths_map):
   count_overlap = 0
   for row in paths_map:
      for y in row:
         if y > 1:
            count_overlap += 1
   return count_overlap

def first_star(data_file):
   data_paths, max_coordinate = read_data_from_file(data_file)
   print(max_coordinate)
   paths_map = [ [0] * (max_coordinate+1) for _ in range(max_coordinate+1)]
   for path in data_paths:
      if path[0][0] == path[1][0]:
         #print(f"PATH:{path} call HORIZONTAL({path[0][0]}, {path[0][1]}, {path[1][1]})")
         paths_map = horizontal_path(paths_map, path[0][0], min(path[0][1], path[1][1]), abs(path[0][1]- path[1][1]))
      elif path[0][1] == path[1][1]:
         #print(f"PATH:{path} call VERTICAL({path[0][1]}, {path[0][0]}, {path[1][0]})")
         paths_map = vertical_path(paths_map, path[0][1], min(path[0][0], path[1][0]), abs(path[0][0] - path[1][0]))
      else:
         pass
   return count_two_lines_overlap(paths_map)

def second_star(data_file):
   data_paths, max_coordinate = read_data_from_file(data_file)
   paths_map = [ [0] * (max_coordinate+1) for _ in range(max_coordinate+1)]
   for path in data_paths:
      if path[0][0] == path[1][0]:
         #print(f"PATH:{path} call HORIZONTAL({path[0][0]}, {path[0][1]}, {path[1][1]})")
         paths_map = horizontal_path(paths_map, path[0][0], min(path[0][1], path[1][1]), abs(path[0][1]- path[1][1]))
      elif path[0][1] == path[1][1]:
         #print(f"PATH:{path} call VERTICAL({path[0][1]}, {path[0][0]}, {path[1][0]})")
         paths_map = vertical_path(paths_map, path[0][1], min(path[0][0], path[1][0]), abs(path[0][0] - path[1][0]))
      else:
         #print(f"PATH:{path} call VERTICAL({path[0][1]}, {path[0][0]}, {path[1][0]})")
         paths_map = diag_path(paths_map, path[0][0], path[1][0], path[0][1], path[1][1])
   return count_two_lines_overlap(paths_map)

def run_two_stars(data_file):
   result = first_star(data_file)
   print(f"DATA: {data_file}, first_star: {result}")
   result = second_star(data_file)
   print(f"DATA: {data_file}, second_star: {result}")

def main():
   script_name = __file__.split('/')[-1].split('.')[0]
   files = [f"./test/{script_name}_data.txt", f"./test/{script_name}_real_data.txt"]
   for data_file in files:
      run_two_stars(data_file)

if __name__ == "__main__":
   main()