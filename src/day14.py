import os

def read_data_from_file(file_name):
   pair_insertion_rules = {}
   f = open(file_name, "r")
   lines = f.read().splitlines()
   f.close()
   polymer_template = lines[0]
   for line in lines[2:]:
      rule = line.split(" -> ")
      pair_insertion_rules[rule[0]] = [rule[0][0]+rule[1], rule[1]+rule[0][1]]
   return polymer_template, pair_insertion_rules

def polymer_force(file_name, number_of_iterations):
   polymer_template, pair_insertion_rules = read_data_from_file(file_name)
   actual_pairs = {x:0 for x in pair_insertion_rules.keys()}
   empty_pairs = actual_pairs.copy()
   for index in range(len(polymer_template)-1):
      actual_pairs[polymer_template[index:index+2]] += 1
   for insertion_index in range(number_of_iterations):
      new_pairs = empty_pairs.copy()
      for pair in actual_pairs.keys():
         new_pairs[pair_insertion_rules[pair][0]] += actual_pairs[pair]
         new_pairs[pair_insertion_rules[pair][1]] += actual_pairs[pair]
      actual_pairs = new_pairs.copy()
   occurences = [0] * 26
   for pair in actual_pairs.keys():
      index = ord(pair[0]) - ord("A")
      occurences[index] += actual_pairs[pair]
   occurences[ord(polymer_template[-1])-ord("A")] += 1
   ordered_occurences = sorted(occurences)
   ordered_occurences = [x for x in ordered_occurences if x > 0]
   return ordered_occurences[-1]-ordered_occurences[0]

def first_star(file_name):
   return polymer_force(file_name, 10)

def second_star(file_name):
   return polymer_force(file_name, 40)

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