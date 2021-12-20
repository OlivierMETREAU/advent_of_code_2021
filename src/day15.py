import os

class Node:
   def __init__(self, row, col, risk):
      self.row = row
      self.col = col
      self.risk = risk
      self.visited = False
      self.tentative_risk = None

   def __repr__(self):
      return f"| R{self.row}C{self.col}, visited={self.visited}, distance={self.tentative_risk}"

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
      for risk in split_line:
         last_node = Node(row, col, risk)
         row_of_nodes.append(last_node)
         col += 1
      list_of_nodes.append(row_of_nodes)
      row += 1
   list_of_nodes[0][0].tentative_risk = 0
   return list_of_nodes, last_node

def read_data_from_file_5_times(file_name):
   list_of_nodes = []
   f = open(file_name, "r")
   lines = f.read().splitlines()
   f.close()
   row = 0
   for line in lines:
      col = 0
      split_line = [int(x) for x in line]
      row_of_nodes = []
      for i in range(5):
         for risk in split_line:
            last_node = Node(row, col, ((risk+i-1)%9)+1)
            row_of_nodes.append(last_node)
            col += 1
      list_of_nodes.append(row_of_nodes)
      row += 1
   number_of_rows_to_copy = row
   for i in range(number_of_rows_to_copy, 5*number_of_rows_to_copy):
      row_of_nodes = []
      col = 0
      for node in list_of_nodes[i-number_of_rows_to_copy]:
         last_node = Node(i, col, (node.risk%9)+1)
         row_of_nodes.append(last_node)
         col += 1
      list_of_nodes.append(row_of_nodes)
   list_of_nodes[0][0].tentative_risk = 0
   return list_of_nodes, last_node

def get_unvisited_neighbors(row, col, list_of_nodes, last_node):
   list_of_unvisited_neighbors = []
   for x in [col-1, col+1]:
      if x >= 0 and x <= last_node.col:
         if not list_of_nodes[row][x].visited:
            list_of_unvisited_neighbors.append(list_of_nodes[row][x])
   for x in [row-1, row+1]:
      if x >= 0 and x <= last_node.row:
         if not list_of_nodes[x][col].visited:
            list_of_unvisited_neighbors.append(list_of_nodes[x][col])
   return list_of_unvisited_neighbors

def get_lowest_risk_unvisited_node(list_of_nodes):
   lowest_risk_node = None
   for row in list_of_nodes:
      for node in row:
         if node.tentative_risk is not None and not node.visited:
            if lowest_risk_node is None:
               lowest_risk_node = node
            else:
               if lowest_risk_node.tentative_risk > node.tentative_risk:
                  lowest_risk_node = node
   return lowest_risk_node

def find_best_path(list_of_nodes, last_node):
   current_node = list_of_nodes[0][0]
   print_index = 0
   while current_node != last_node:
      #print(f"{current_node=}")
      list_of_unvisited_neighbors = get_unvisited_neighbors(current_node.row, current_node.col, list_of_nodes, last_node)
      for neighbor in list_of_unvisited_neighbors:
         tentative_risk = current_node.tentative_risk + neighbor.risk
         if neighbor.tentative_risk == None:
            neighbor.tentative_risk = tentative_risk
         neighbor.tentative_risk = min(tentative_risk, neighbor.tentative_risk)
      current_node.visited = True
      current_node = get_lowest_risk_unvisited_node(list_of_nodes)
      if print_index % 1000 == 0:
         print(current_node)
         print(last_node)
      print_index += 1
   #print(list_of_nodes)
   return last_node.tentative_risk

def print_map(list_of_nodes):
   for row in list_of_nodes:
      print("".join([str(x.risk) for x in row]))

def first_star(file_name):
   list_of_nodes, last_node = read_data_from_file(file_name)
   #print_map(list_of_nodes)
   return find_best_path(list_of_nodes, last_node)

def second_star(file_name):
   list_of_nodes, last_node = read_data_from_file_5_times(file_name)
   #print_map(list_of_nodes)
   return find_best_path(list_of_nodes, last_node)

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