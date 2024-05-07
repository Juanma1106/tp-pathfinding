from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Step 1: Initialize the initial node
        node = Node("", grid.start, 0)

        # Step 2: Initialize the explored dictionary to be empty
        explored = {}

        # Step 3: Add the node to the explored dictionary
        explored[node.state] = True

        # Step 4: Initialize the frontier with a priority queue
        frontier = PriorityQueueFrontier()

        # Step 5: Add the initial node to the frontier
        frontier.add(node, int(node.cost + grid.heuristic(node.state, grid.end)))

        # Step 6: Start the search
        while not frontier.is_empty():
            # Step 7: Get the node with the highest priority from the frontier
            current_node = frontier.pop()

            # Step 8: Check if the current node is the goal
            if current_node.state == grid.end:
                return Solution(current_node, explored)

            # Step 9: Mark the current node as explored
            explored[current_node.state] = True

            # Step 10: Get the neighbors of the current node
            neighbors = grid.get_neighbours(current_node.state)

            # Step 11: Expand the neighbors
            for action, neighbor_state in neighbors.items():
                # Step 12: Calculate the cost for the neighbor node
                new_cost = current_node.cost + grid.get_cost(neighbor_state)

                # Step 13: Create a new node for the neighbor
                new_node = Node("", neighbor_state, new_cost)

                # Step 14: If the neighbor has not been explored or is not in the frontier, add it to the frontier
                if neighbor_state not in explored and not frontier.contains_state(neighbor_state):
                    frontier.add(new_node, int(new_node.cost + grid.heuristic(neighbor_state, grid.end)))

        # Step 15: If no solution is found
        return NoSolution(explored)
#class AStarSearch:
 #   @staticmethod
  #  def search(grid: Grid) -> Solution:
  #      """Find path between two points in a grid using A* Search

    #    Args:
    #        grid (Grid): Grid of points

    #    Returns:
    #        Solution: Solution found
     #   """
        # Initialize a node with the initial position
     #   node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
      #  explored = {} 
        
        # Add the node to the explored dictionary
        #explored[node.state] = True
        
       # return NoSolution(explored)
