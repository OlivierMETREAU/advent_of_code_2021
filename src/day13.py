import os

def read_data_from_file(file_name):
   dots = []
   fold_instructions = []
   f = open(file_name, "r")
   lines = f.read().splitlines()
   f.close()
   for line in lines:
      if line.startswith("fold"):
         line = line[11:]
         fields = line.split("=")
         fold_instructions.append([fields[0], int(fields[1])])
      else:
         if len(line)>1:
            dot = [int(x) for x in line.split(",")]
            dots.append([dot[1], dot[0]])
   return dots, fold_instructions

def vertical_fold(fold_index, dots):
   for dot in dots:
      if dot[1] > fold_index:
         dot[1] = 2 * fold_index - dot[1]
   return dots

def horizontal_fold(fold_index, dots):
   for dot in dots:
      if dot[0] > fold_index:
         dot[0] = 2 * fold_index - dot[0]
   return dots

def pretty_print_dots(dots):
   xmax = 0
   ymax = 0
   number_of_dots_remaining = 0
   for dot in dots:
      xmax = max(xmax, dot[0])
      ymax = max(ymax, dot[1])
   pretty_dots=[]
   for row in range(xmax+1):
      pretty_dots.append(["."] * (ymax+1))
   for dot in dots:
      if pretty_dots[dot[0]][dot[1]] != "X":
         pretty_dots[dot[0]][dot[1]] = "X"
         number_of_dots_remaining += 1
   pretty_dots = "\n".join(["".join(row) for row in pretty_dots])
   #print()
   #print(pretty_dots)
   return number_of_dots_remaining

def first_star(file_name):
   dots, fold_instructions = read_data_from_file(file_name)
   for fold_instruction in fold_instructions:
      if fold_instruction[0] == "x":
         dots = vertical_fold(fold_instruction[1], dots)
      else:
         dots = horizontal_fold(fold_instruction[1], dots)
      print(f"NUMBER OF DOTS = {pretty_print_dots(dots)}")
   pass

def second_star(file_name):
   dots, fold_instructions = read_data_from_file(file_name)
   pass

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