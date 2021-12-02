from ..src.read_data_from_file import DataFile
from ..src import day1
from ..src import day2


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
