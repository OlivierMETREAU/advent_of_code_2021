if __name__ == "__main__":
   from read_data_from_file import DataFile
else:
   from ..src.read_data_from_file import DataFile

def count_incresing(data):
   delta = [y-x for x,y in zip(data, data[1:])]
   positives = [x>0 for x in delta]
   return positives.count(True)

def first_star(data):
   return count_incresing(data)

def second_star(data):
   three_measurement_windows = [x+y+z for x,y,z in zip(data, data[1:], data[2:])]
   return count_incresing(three_measurement_windows)

def run_two_stars(data_file):
   data = DataFile(data_file)
   result = first_star(data.data_from_file)
   print(f"DATA: {data_file}, first_star: {result}")
   result = second_star(data.data_from_file)
   print(f"DATA: {data_file}, second_star: {result}")

def main():
   files = ["./test/day1_data.txt", "./test/day1_real_data.txt"]
   for data_file in files:
      run_two_stars(data_file)

if __name__ == "__main__":
   main()