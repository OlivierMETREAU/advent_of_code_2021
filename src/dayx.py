if __name__ == "__main__":
   from read_data_from_file import DataFile
else:
   from ..src.read_data_from_file import DataFile

def first_star(data):
   pass

def second_star(data):
   pass

def run_two_stars(data_file):
   data = DataFile(data_file, [None, int])
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