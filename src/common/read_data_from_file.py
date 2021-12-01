class DataFile:
   def __init__(self, file_path: str):
         f = open(file_path, "r")
         lines = f.read().splitlines() 
         self.data_from_file = [int(x) for x in lines]
         f.close()

