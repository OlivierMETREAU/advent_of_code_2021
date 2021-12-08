def read_data_from_file(file_name):
   f = open(file_name, "r")
   lines = f.read().splitlines()
   f.close()
   return [[line.split('|')[x].split() for x in range(2)] for line in lines]

def first_star(file_name):
   data = read_data_from_file(file_name)
   count = 0
   for line in data:
      for digit in line[1]:
         if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
            count += 1
   return count

def get_all_entries(signal):
   # ecdbfag deacfb acdgb cdg acdbf gdfb efacdg gd cagdbf beacg | cdg dcebgaf gbdf bdacg
   signal_list = []
   for digit in signal:
      signal_list.append(''.join(sorted(digit)))
   return list(sorted(signal_list, key = len))

def second_star(file_name):
   data = read_data_from_file(file_name)
   sum_numbers = 0
   for line in data:
      signals = get_all_entries(line[0])
      list_decoding = [None, signals[0], None, None, signals[2], None, None, signals[1], signals[9], None]
      decoding = {
         signals[0]: 1,
         signals[1]: 7,
         signals[2]: 4,
         signals[9]: 8
      }
      for index in range(3, 6):
         if set(signals[0]) <= set(signals[index]):
            decoding[signals[index]] = 3
            list_decoding[3] = signals[index]
      nine = ''.join(sorted(set(list_decoding[3]).union(list_decoding[4])))
      list_decoding[9] = nine
      decoding[nine] = 9
      b = set(list_decoding[9]) - set(list_decoding[3])
      for index in range(3, 6):
         if signals[index] not in decoding:
            if b < set(signals[index]):
               decoding[signals[index]] = 5
               list_decoding[5] = signals[index]
            else:
               decoding[signals[index]] = 2
               list_decoding[2] = signals[index]
      for index in range(6, 9):
         if signals[index] not in decoding:
            if set(list_decoding[1]) < set(signals[index]):
               decoding[signals[index]] = 0
               list_decoding[0] = signals[index]
            else:
               decoding[signals[index]] = 6
               list_decoding[6] = signals[index]
      gain = 1000
      number = 0
      for digit in line[1]:
         number += gain * decoding[''.join(sorted(digit))]
         gain = gain / 10
      sum_numbers += int(number)
   return sum_numbers

def run_two_stars(file_name):
   result = first_star(file_name)
   print(f"DATA: {file_name}, first_star: {result}")
   result = second_star(file_name)
   print(f"DATA: {file_name}, second_star: {result}")

def main():
   script_name = __file__.split('/')[-1].split('.')[0]
   files = [f"./test/{script_name}_data.txt", f"./test/{script_name}_real_data.txt"]
   for data_file in files:
      run_two_stars(data_file)

if __name__ == "__main__":
   main()