input_choices = [[3,4,3,1,2], [1,1,3,5,1,3,2,1,5,3,1,4,4,4,1,1,1,3,1,4,3,1,2,2,2,4,1,1,5,5,4,3,1,1,1,1,1,1,3,4,1,2,2,5,1,3,5,1,3,2,5,2,2,4,1,1,1,4,3,3,3,1,1,1,1,3,1,3,3,4,4,1,1,5,4,2,2,5,4,5,2,5,1,4,2,1,5,5,5,4,3,1,1,4,1,1,3,1,3,4,1,1,2,4,2,1,1,2,3,1,1,1,4,1,3,5,5,5,5,1,2,2,1,3,1,2,5,1,4,4,5,5,4,1,1,3,3,1,5,1,1,4,1,3,3,2,4,2,4,1,5,5,1,2,5,1,5,4,3,1,1,1,5,4,1,1,4,1,2,3,1,3,5,1,1,1,2,4,5,5,5,4,1,4,1,4,1,1,1,1,1,5,2,1,1,1,1,2,3,1,4,5,5,2,4,1,5,1,3,1,4,1,1,1,4,2,3,2,3,1,5,2,1,1,4,2,1,1,5,1,4,1,1,5,5,4,3,5,1,4,3,4,4,5,1,1,1,2,1,1,2,1,1,3,2,4,5,3,5,1,2,2,2,5,1,2,5,3,5,1,1,4,5,2,1,4,1,5,2,1,1,2,5,4,1,3,5,3,1,1,3,1,4,4,2,2,4,3,1,1]]

def first_star(data, number_of_days):
   number_of_fish_per_day = [data.count(x) for x in range(9)]
   for day in range(1, number_of_days + 1):
      number_of_babies = number_of_fish_per_day[0]
      number_of_fish_per_day = number_of_fish_per_day[1:] + [number_of_babies]
      number_of_fish_per_day[6] += number_of_babies
   return sum(number_of_fish_per_day)

def second_star(data, number_of_days):
   return first_star(data, 256)

def run_two_stars(list_of_fish, number_of_days):
   result = first_star(list_of_fish, number_of_days)
   print(f"DATA: {list_of_fish}, first_star: {result}")
   result = second_star(list_of_fish, number_of_days)
   print(f"DATA: {list_of_fish}, second_star: {result}")

def main():
   for input in input_choices:
      run_two_stars(input, 80)

if __name__ == "__main__":
   main()