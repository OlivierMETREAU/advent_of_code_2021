from ..src.read_data_from_file import DataFile
from ..src import day1


def test_day1_first():
   data = DataFile("./test/day1_data.txt").data_from_file
   assert 7 == day1.first_star(data)

def test_day1_second():
   data = DataFile("./test/day1_data.txt").data_from_file
   assert 5 == day1.second_star(data)
