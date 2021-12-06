from ..src.read_data_from_file import DataFile
from ..src import day1
from ..src import day2
from ..src import day3
from ..src import day4
from ..src import day5
from ..src import day6

def test_day1_first():
   data = DataFile("./test/day1_data.txt").data_from_file
   assert 7 == day1.first_star(data)

def test_day1_second():
   data = DataFile("./test/day1_data.txt").data_from_file
   assert 5 == day1.second_star(data)

def test_day2_first():
   data = DataFile("./test/day2_data.txt", applied_function=[None, int]).data_from_file
   assert 150 == day2.first_star(data)

def test_day2_second():
   data = DataFile("./test/day2_data.txt", applied_function=[None, int]).data_from_file
   assert 900 == day2.second_star(data)

def test_day3_first():
   data = DataFile("./test/day3_data.txt", applied_function=[None]).data_from_file
   assert 198 == day3.first_star(data)

def test_day3_second():
   data = DataFile("./test/day3_data.txt", applied_function=[None]).data_from_file
   assert 230 == day3.second_star(data)

def test_day4_first():
   assert 4512 == day4.first_star("./test/day4_data.txt")

def test_day4_second():
   assert 1924 == day4.second_star("./test/day4_data.txt")

def test_day5_first():
   assert 5 == day5.first_star("./test/day5_data.txt")

def test_day5_second():
   assert 12 == day5.second_star("./test/day5_data.txt")

def test_day6_first():
   assert 26 == day6.first_star([3,4,3,1,2], 18)

def test_day6_second():
   assert 26984457539 == day6.first_star([3,4,3,1,2], 256)