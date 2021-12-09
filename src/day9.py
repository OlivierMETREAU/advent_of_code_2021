import os

def read_data_from_file(file_name):
   f = open(file_name, "r")
   lines = f.read().splitlines()
   f.close()
   return [[int(x) for x in list(line)] for line in lines]

def is_low_point(row, column, number_of_rows, number_of_columns, data):
   if is_lower_than_left(row, column, data) and \
      is_lower_than_right(row, column, number_of_columns, data) and \
      is_lower_than_above(row, column, data) and \
      is_lower_than_below(row, column, number_of_rows, data):
      return True
   return False

def is_lower_than_left(row, column, data):
   if column == 0:
      return True
   if data[row][column] < data[row][column-1]:
      return True
   return False

def is_lower_than_right(row, column, number_of_columns, data):
   if column == number_of_columns-1:
      return True
   if data[row][column] < data[row][column+1]:
      return True
   return False

def is_lower_than_above(row, column, data):
   if row == 0:
      return True
   if data[row][column] < data[row-1][column]:
      return True
   return False

def is_lower_than_below(row, column, number_of_rows, data):
   if row == number_of_rows-1:
      return True
   if data[row][column] < data[row+1][column]:
      return True
   return False

def first_star(file_name):
   data = read_data_from_file(file_name)
   number_of_rows = len(data)
   number_of_columns = len(data[0])
   risk_level = 0
   for row in range(number_of_rows):
      for column in range(number_of_columns):
         if is_low_point(row, column, number_of_rows, number_of_columns, data):
            risk_level += data[row][column] + 1
   return risk_level

def find_around_point_not_high(row, column, number_of_rows, number_of_columns, data):
   size = 0
   if row > 0 and data[row-1][column] < 9:
      data[row-1][column] = 9
      size += 1 + find_around_point_not_high(row-1, column, number_of_rows, number_of_columns, data)
   if row < number_of_rows - 1 and data[row+1][column] < 9:
      data[row+1][column] = 9
      size += 1 + find_around_point_not_high(row+1, column, number_of_rows, number_of_columns, data)
   if column > 0 and data[row][column-1] < 9:
      data[row][column-1] = 9
      size += 1 + find_around_point_not_high(row, column-1, number_of_rows, number_of_columns, data)
   if column < number_of_columns-1 and data[row][column+1] < 9:
      data[row][column+1] = 9
      size += 1 + find_around_point_not_high(row, column+1, number_of_rows, number_of_columns, data)
   return size

def find_bassin_size_from_low_point(row, column, number_of_rows, number_of_columns, data):
   return find_around_point_not_high(row, column, number_of_rows, number_of_columns, data)

def second_star(file_name):
   data = read_data_from_file(file_name)
   number_of_rows = len(data)
   number_of_columns = len(data[0])
   list_of_areas = []
   for row in range(number_of_rows):
      for column in range(number_of_columns):
         if is_low_point(row, column, number_of_rows, number_of_columns, data):
            list_of_areas.append(find_bassin_size_from_low_point(row, column, number_of_rows, number_of_columns, data))
   three_biger_areas = sorted(list_of_areas, key=int, reverse=True)[0:3]
   return three_biger_areas[0] * three_biger_areas[1] * three_biger_areas[2]

def run_two_stars(file_name):
   result = first_star(file_name)
   print(f"DATA: {file_name}, first_star: {result}")
   result = second_star(file_name)
   print(f"DATA: {file_name}, second_star: {result}")

def main():
   script_name = __file__.split(os.sep)[-1].split('.')[0]
   files = [f"./test/{script_name}_data.txt", f"./test/{script_name}_real_data.txt"]
   for data_file in files:
      run_two_stars(data_file)

if __name__ == "__main__":
   main()