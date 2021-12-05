if __name__ == "__main__":
   from read_data_from_file import DataFile
else:
   from ..src.read_data_from_file import DataFile

def bit_array_to_int(bit_array):
   out = 0
   for bit in bit_array:
      out = (out << 1) | bit
   return out

def first_star(data):
   data_by_character = [[int(y) for y in list(x)] for x in data]
   transpose_data_by_character =  [list(i) for i in zip(*data_by_character)]
   column_sums = [sum(x) for x in transpose_data_by_character]
   mid_value = len(transpose_data_by_character[0])/2
   gamma = [int(x/mid_value) for x in column_sums]
   epsilon = [1-x for x in gamma]
   return bit_array_to_int(gamma) * bit_array_to_int(epsilon)

def filter(input_list, bit_position, bit_criteria):
   filtered_list = []
   for line in input_list:
      if line[bit_position] == bit_criteria:
         filtered_list.append(line)
   return filtered_list

def filter_out_by_counting(input_list, bit_position, oxygen_rating):
   sum_column_filtered = 0
   for element in input_list:
         sum_column_filtered += element[bit_position]
   bit_criteria = int(sum_column_filtered / (len(input_list) / 2) )
   bit_criteria = min(1, bit_criteria)
   if not oxygen_rating:
      bit_criteria = 1 - bit_criteria
   return filter(input_list, bit_position, bit_criteria)

def recursive_filter(data, oxygen_rating):
   rating = data
   bit_position = 0
   while True:
      rating = filter_out_by_counting(rating, bit_position, oxygen_rating)
      bit_position += 1
      if len(rating) <= 1:
         break
   return rating

def second_star(data):
   data_by_character = [[int(y) for y in list(x)] for x in data]
   oxygen_rating = bit_array_to_int(recursive_filter(data_by_character, True)[0])
   co2_rating = bit_array_to_int(recursive_filter(data_by_character, False)[0])
   return oxygen_rating * co2_rating

def run_two_stars(data_file):
   data = DataFile(data_file, [None])
   result = first_star(data.data_from_file)
   print(f"DATA: {data_file}, first_star: {result}")
   result = second_star(data.data_from_file)
   print(f"DATA: {data_file}, second_star: {result}")

def main():
   script_name = __file__.split('/')[-1].split('.')[0]
   files = [f"./test/{script_name}_data.txt", f"./test/{script_name}_real_data.txt"]
   for data_file in files:
      run_two_stars(data_file)

if __name__ == "__main__":
   main()