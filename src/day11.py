import os

octopuses = ["""5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""", """6111821767
1763611615
3512683131
8582771473
8214813874
2325823217
2222482823
5471356782
3738671287
8675226574"""
]

def get_octopuses_list(string_of_octopuses):
   list_of_octopuses = []
   for line in string_of_octopuses.split("\n"):
      list_of_octopuses.append([int(x) for x in line])
   return list_of_octopuses

def increment_octopus_power(row, col, data):
   data[row][col] += 1
   if data[row][col] == 10:
      for i in [row-1, row, row+1]:
         for j in [col-1, col, col+1]:
            if i != row or j != col:
               if i >= 0 and j >= 0 and i < len(data) and j < len(data[0]):
                  increment_octopus_power(i, j, data)

def first_star(octopuse_data):
   data = get_octopuses_list(octopuse_data)
   count_flash = 0
   for i in range(100):
      for row_index in range(len(data)):
         for col_index in range(len(data[0])):
            increment_octopus_power(row_index, col_index, data)
      for row_index in range(len(data)):
         for col_index in range(len(data[0])):
            if data[row_index][col_index] >= 10:
               data[row_index][col_index] = 0
               count_flash += 1
   return count_flash

def second_star(octopuse_data):
   data = get_octopuses_list(octopuse_data)
   iteration_index = 1
   while True:
      for row_index in range(len(data)):
         for col_index in range(len(data[0])):
            increment_octopus_power(row_index, col_index, data)
      all_flash = True
      for row_index in range(len(data)):
         for col_index in range(len(data[0])):
            if data[row_index][col_index] >= 10:
               data[row_index][col_index] = 0
            else:
               all_flash = False
      if all_flash:
         break
      iteration_index += 1
   return iteration_index

def run_two_stars(octopuse_data):
   result = first_star(octopuse_data)
   print_data = octopuse_data.split('\n')[0]
   print(f"DATA: {print_data}, first_star: {result}")
   result = second_star(octopuse_data)
   print(f"DATA: {print_data}, second_star: {result}")

def main():
   for octopuse_data in octopuses:
      run_two_stars(octopuse_data)
      

if __name__ == "__main__":
   main()