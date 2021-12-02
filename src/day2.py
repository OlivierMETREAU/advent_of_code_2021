if __name__ == "__main__":
   from read_data_from_file import DataFile
else:
   from ..src.read_data_from_file import DataFile

def forward(depth, horizontal_position, aim, value):
   if aim is not None:
      return depth + (aim * value), horizontal_position + value, aim
   return depth, horizontal_position + value, aim

def down(depth, horizontal_position, aim, value):
   if aim is not None:
      return depth, horizontal_position, aim + value
   return depth + value, horizontal_position, aim

def up(depth, horizontal_position, aim, value):
   if aim is not None:
      return depth, horizontal_position, aim - value
   return depth - value, horizontal_position, aim

def compute_depth_and_horizontal_position(data, aim=None):
   depth = 0
   horizontal_position = 0
   for entry in data:
      depth, horizontal_position, aim = eval(f"{entry[0]}({depth},{horizontal_position},{aim},{entry[1]})")
   return depth * horizontal_position

def first_star(data):
   return compute_depth_and_horizontal_position(data)

def second_star(data):
   return compute_depth_and_horizontal_position(data, aim=0)

def run_two_stars(data_file):
   data = DataFile(data_file, [None, int])
   result = first_star(data.data_from_file)
   print(f"DATA: {data_file}, first_star: {result}")
   result = second_star(data.data_from_file)
   print(f"DATA: {data_file}, second_star: {result}")

def main():
   files = ["./test/day2_data.txt", "./test/day2_real_data.txt"]
   for data_file in files:
      run_two_stars(data_file)

if __name__ == "__main__":
   main()