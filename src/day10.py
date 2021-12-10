import os

def read_data_from_file(file_name):
   f = open(file_name, "r")
   lines = f.read().splitlines()
   f.close()
   return [list(line) for line in lines]


def first_star(file_name):
   data = read_data_from_file(file_name)
   closing_association = {
      "{": "}",
      "[": "]",
      "(": ")",
      "<": ">"
      }
   chunk_score = {
      ")": 3,
      "]": 57,
      "}": 1197,
      ">": 25137
      }
   count_chunks = {"{": 0, "[": 0, "(": 0, "<": 0}
      
   score = 0
   for line in data:
      list_of_closing_elements = []
      for element in line:
         if element in count_chunks.keys():
            list_of_closing_elements.append(closing_association[element])
         else:
            if list_of_closing_elements[-1] != element:
               score += chunk_score[element]
               break
            else:
               list_of_closing_elements.pop(-1)
   return score

def is_line_corrupted(line):
   closing_association = {"{": "}", "[": "]", "(": ")", "<": ">"}
   count_chunks = {"{": 0, "[": 0, "(": 0, "<": 0}
   list_of_closing_elements = []
   for element in line:
      if element in count_chunks.keys():
         list_of_closing_elements.append(closing_association[element])
      else:
         if list_of_closing_elements[-1] != element:
            return True, None
         else:
            list_of_closing_elements.pop(-1)
   return False, list_of_closing_elements

def second_star(file_name):
   data = read_data_from_file(file_name)
   line_scores = []
   closing_score = {")": 1, "]": 2, "}": 3, ">": 4}
   for line in data:
      line_corrupted, list_of_closing_elements = is_line_corrupted(line)
      if not line_corrupted:
         line_score = 0
         while len(list_of_closing_elements):
            next_closing_element = list_of_closing_elements.pop(-1)
            line_score = (line_score * 5) + closing_score[next_closing_element]
         line_scores.append(line_score)
   return sorted(line_scores)[int((len(line_scores)-1)/2)]

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