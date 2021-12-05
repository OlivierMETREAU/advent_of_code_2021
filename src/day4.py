if __name__ == "__main__":
   from read_data_from_file import DataFile
else:
   from ..src.read_data_from_file import DataFile

def read_data_from_file(file_path):
   f = open(file_path, "r")
   lines = f.read().splitlines()
   draw_number = [int(x) for x in lines[0].split(",")]
   set_of_boards = {"winners": 0, "boards": []}
   for i in range(int(len(lines)/ 6)):
      board = {"winner": False, "called_on_columns" : [0, 0, 0, 0, 0], "board": []}
      for line in lines[6*i+2:6*i+7]:
         board["board"].append({"called_on_line": 0, "line": [{"number": int(x), "called": False} for x in line.split()]})
      set_of_boards["boards"].append(board)
   return draw_number, set_of_boards

def find_the_first_winner(draw_number, set_of_boards):
   for number in draw_number:
      for board in set_of_boards["boards"]:
         for line in board["board"]:
            col_index = 0
            for card_number in line["line"]:
               if card_number["number"] == number:
                  card_number["called"] = True
                  line["called_on_line"] += 1
                  board["called_on_columns"][col_index] += 1
                  if line["called_on_line"] == 5 or board["called_on_columns"][col_index] == 5:
                     board["winner"] = True
                     return number, board
               col_index += 1

def find_remaining_one(set_of_boards):
   boards = []
   for board in set_of_boards["boards"]:
      if not board["winner"]:
         return board

def find_the_last_winner(draw_number, set_of_boards):
   for number in draw_number:
      for board in set_of_boards["boards"]:
         if not board["winner"]:
            for line in board["board"]:
               col_index = 0
               for card_number in line["line"]:
                  if card_number["number"] == number:
                     card_number["called"] = True
                     line["called_on_line"] += 1
                     board["called_on_columns"][col_index] += 1
                     if line["called_on_line"] == 5 or board["called_on_columns"][col_index] == 5:
                        set_of_boards["winners"] += 1
                        if set_of_boards["winners"] == len(set_of_boards["boards"]):
                           return number, find_remaining_one(set_of_boards)
                        board["winner"] = True
                  col_index += 1

def calc_result_from_board(last_number, winner_board):
   sum_unmarked = 0
   for line in winner_board["board"]:
      for card_number in line["line"]:
         if not card_number["called"]:
            sum_unmarked += card_number["number"]
   return last_number * sum_unmarked

def first_star(data_file):
   draw_number, set_of_boards = read_data_from_file(data_file)
   last_number, winner_board = find_the_first_winner(draw_number, set_of_boards)
   return calc_result_from_board(last_number, winner_board)

def second_star(data_file):
   draw_number, set_of_boards = read_data_from_file(data_file)
   last_number, winner_board = find_the_last_winner(draw_number, set_of_boards)
   return calc_result_from_board(last_number, winner_board)

def run_two_stars(data_file):
   result = first_star(data_file)
   print(f"DATA: {data_file}, first_star: {result}")
   result = second_star(data_file)
   print(f"DATA: {data_file}, second_star: {result}")

def main():
   script_name = __file__.split('/')[-1].split('.')[0]
   files = [f"./test/{script_name}_data.txt", f"./test/{script_name}_real_data.txt"]
   for data_file in files:
      run_two_stars(data_file)

if __name__ == "__main__":
   main()