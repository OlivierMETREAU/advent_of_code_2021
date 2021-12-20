import ast
import os
from copy import deepcopy

def pretty_print_2d_table(matrix):
   print('\n'.join([''.join([str(cell) for cell in row]) for row in matrix]))

def read_data_from_file(file_name):
   f = open(file_name, "r")
   lines = f.read().splitlines()
   f.close()
   image_enhancement_algorithm = lines[0]
   input_image = [[x for x in line.replace(".", "0").replace("#", "1")] for line in lines[2:]]
   return {"algorithm": image_enhancement_algorithm, "input": input_image}

def enlarge_picture_by_two_pixels(input_image, number_of_iteration, algorithm_inifite_character):
    row_len = len(input_image[0])+4
    c = "0"
    if algorithm_inifite_character == "#" and number_of_iteration%2:
        c = "1"
    image = [[c] * 2 + row + [c] * 2 for row in input_image]
    image =  [[c] * row_len, [c] * row_len]
    for row in input_image:
        image.append([c] * 2 + row + [c] * 2)
    image.append([c] * row_len)
    image.append([c] * row_len)
    return image

def enhance_image(input_image, algorithm, number_of_iteration):
    image = enlarge_picture_by_two_pixels(input_image, number_of_iteration, algorithm[0])
    enhanced_image = []
    for i in range(1, len(image) - 1):
        row = []
        for j in range(1, len(image[i])-1):
           pixels = "".join([str(image[i_pixel][j_pixel]) for i_pixel in range(i-1, i+2) for j_pixel in range(j-1, j+2)])
           index_pixels = int(pixels, 2)
           row.append(0 if algorithm[index_pixels] == "." else 1)
        enhanced_image.append(row)
    return enhanced_image

def count_lit_pixels(image):
    lit_pixels = 0
    for line in image:
        lit_pixels += sum(line)
    return lit_pixels

def first_star(file_name):
    data = read_data_from_file(file_name)
    image = data["input"]
    for i in range(2):
        image = enhance_image(image, data["algorithm"], i)
    return count_lit_pixels(image)

def second_star(file_name):
    data = read_data_from_file(file_name)
    image = data["input"]
    for i in range(50):
        image = enhance_image(image, data["algorithm"], i)
    return count_lit_pixels(image)

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