import ast
import os
from copy import deepcopy

def read_data_from_file(file_name):
   f = open(file_name, "r")
   lines = f.read().splitlines()
   f.close()
   return [eval(x) for x in lines]

def add(x, y):
    return reduce([x, y])


def reduce(root):
    root = deepcopy(root)

    while action(root):
        pass

    return root


def action(root):
    # We'll keep track of the relevant nodes for exploding and splitting while walking
    # through the tree. Since we don't have pointers to primitives in python we'll have
    # to store the parent pair and index pair so that we can perform updates.
    pair_left, i_left = None, None
    pair_right, i_right = None, None
    pair_split, i_split = None, None

    stack = [(0, [root, None], 0)]

    while stack:
        depth, pair, i = stack.pop()

        if isinstance(pair[i], int):
            # keep track of where to split if we don't end up exploding
            if not pair_split and pair[i] >= 10:
                pair_split, i_split = pair, i

            # keep track of most recent regular number (i.e. left of exploded number)
            pair_left, i_left = pair, i
        else:
            if depth >= 4:
                # keep iterating until the next regular number (i.e. right of exploded number)
                if stack:
                    _, pair_right, i_right = stack.pop()
                    while isinstance(pair_right[i_right], list):
                        pair_right, i_right = pair_right[i_right], 0

                # perform explode
                if pair_left:
                    pair_left[i_left] += pair[i][0]
                if pair_right:
                    pair_right[i_right] += pair[i][1]
                pair[i] = 0

                return True
            else:
                # push child numbers onto the stack
                stack.append((depth + 1, pair[i], 1))
                stack.append((depth + 1, pair[i], 0))

    # perform split
    if pair_split:
        pair_split[i_split] = [pair_split[i_split] // 2, (pair_split[i_split] + 1) // 2]
        return True

    return False


def magnitude(a):
    if isinstance(a, int):
        return a
    else:
        return 3 * magnitude(a[0]) + 2 * magnitude(a[1])

def first_star(file_name):
   data = read_data_from_file(file_name)
   x = data[0]
   for y in data[1:]:
      x = add(x, y)
   return magnitude(x)

def second_star(file_name):
   max_magnitude = 0
   data = read_data_from_file(file_name)
   for i, a in enumerate(data):
      for j, b in enumerate(data):
         if i == j:
               continue
         max_magnitude = max(max_magnitude, magnitude(add(a, b)))
   return max_magnitude

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