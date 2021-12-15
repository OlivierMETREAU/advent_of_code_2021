import os

class Node:
   def __init__(self, row, col):
      self.row = row
      self.col = col
      self.visited = False
      self.tentative_distance = None

   def __repr__(self):
      return f"| R{self.row}C{self.col}, visited={self.visited}, distance={self.tentative_distance}"

def read_data_from_file(file_name):
   list_of_nodes = []
   f = open(file_name, "r")
   lines = f.read().splitlines()
   f.close()
   row = 0
   for line in lines:
      col = 0
      split_line = [int(x) for x in line]
      row_of_nodes = []
      for node in split_line:
         row_of_nodes.append(Node(row, col))
         col += 1
      list_of_nodes.append(row_of_nodes)
      row += 1
   list_of_nodes[0][0].tentative_distance = 0
   return list_of_nodes

def first_star(file_name):
   list_of_nodes = read_data_from_file(file_name)
   current_node = list_of_nodes[0][0]
   
   print(list_of_nodes)
   pass

def second_star(file_name):
   list_of_nodes = read_data_from_file(file_name)
   pass

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
      break

if __name__ == "__main__":
   main()

""" Djikstra algorithm

Let the node at which we are starting at be called the initial node.
Let the distance of node Y be the distance from the initial node to Y. Dijkstra's algorithm
will initially start with infinite distances and will try to improve them step by step.

1. Mark all nodes unvisited. Create a set of all the unvisited nodes called the unvisited set.
2. Assign to every node a tentative distance value: set it to zero for our initial node and to infinity for all other nodes. 
   The tentative distance of a node v is the length of the shortest path discovered so far between the node v and the starting node.
   Since initially no path is known to any other vertex than the source itself (which is a path of length zero), 
   all other tentative distances are initially set to infinity. Set the initial node as current.[15]
3. For the current node, consider all of its unvisited neighbors and calculate their tentative distances
   through the current node. Compare the newly calculated tentative distance to the current assigned value
   and assign the smaller one. For example, if the current node A is marked with a distance of 6, 
   and the edge connecting it with a neighbor B has length 2, then the distance to B through A will be 6 + 2 = 8. 
   If B was previously marked with a distance greater than 8 then change it to 8. Otherwise, the current value will be kept.
4. When we are done considering all of the unvisited neighbors of the current node, mark the current node as visited 
   and remove it from the unvisited set. A visited node will never be checked again.
5. If the destination node has been marked visited (when planning a route between two specific nodes) 
   or if the smallest tentative distance among the nodes in the unvisited set is infinity 
   (when planning a complete traversal; occurs when there is no connection between the initial node and remaining unvisited nodes),
   then stop. The algorithm has finished.
6.Otherwise, select the unvisited node that is marked with the smallest tentative distance, set it as the new current node,
   and go back to step 3.

When planning a route, it is actually not necessary to wait until the destination node is "visited" as above: 
   the algorithm can stop once the destination node has the smallest tentative distance among all "unvisited" nodes 
   (and thus could be selected as the next "current").
"""