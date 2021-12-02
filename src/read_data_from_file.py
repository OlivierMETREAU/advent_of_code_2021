class DataFile:
   def __init__(self, file_path: str, applied_function = [int]):
      f = open(file_path, "r")
      lines = f.read().splitlines()
      if len(applied_function) > 1:
         lines = [line.split(" ") for line in lines]
         lines_reformated = []
         for line in lines:
            new_line = []
            for x in range(len(applied_function)):
               new_line.append(self.__apply_function(applied_function[x], line[x]))
            lines_reformated.append(new_line)
         self.data_from_file = lines_reformated
      else:
         self.data_from_file = [self.__apply_function(applied_function[0], x) for x in lines]
      f.close()

   def __apply_function(self, function, value):
      if function is not None:
         return function(value)
      else:
         return value

