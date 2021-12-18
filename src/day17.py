import math

data = [
   {
      "x": [20, 30],
      "y":[-10, -5]
   },
   {
      "x": [79, 137],
      "y":[-176, -117]
   }
]

def first_star(data):
   highest_velocity = abs(data["y"][0] + 1)
   return highest_velocity * (highest_velocity + 1) / 2

def check_solution(data, position, velocity):
   new_position = [x + y for x, y in zip(position, velocity)]
   new_velocity = [max(0, velocity[0]-1), velocity[1]-1]
   if data["x"][0] <= new_position[0] <= data["x"][1]:
      if data["y"][0] <= new_position[1] <= data["y"][1]:
         return True
   if new_position[1] < data["y"][0]:
      return False
   return check_solution(data, new_position, new_velocity)

def second_star(data):
   # get the min x velocity
   min_x = 0
   number_of_solutions = 0
   while True:
      if data["x"][0] <= (min_x)*(min_x+1)/2:
         break
      min_x += 1
   highest_velocity = abs(data["y"][0] + 1)
   for x in range(min_x, data["x"][1] + 1):
      for y in range(-(highest_velocity+1), highest_velocity+1):
         if check_solution(data, [0,0], [x,y]):
            # print(f"{x}, {y}")
            number_of_solutions += 1
   return number_of_solutions

def run_two_stars(data):
   result = first_star(data)
   print(f"DATA: {data}, first_star: {result}")
   result = second_star(data)
   print(f"DATA: {data}, second_star: {result}")

def main():
   for input in data:
      run_two_stars(input)
      

if __name__ == "__main__":
   main()

