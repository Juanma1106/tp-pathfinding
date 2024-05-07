from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Inicializar un nodo con la posición inicial
        node = Node("", grid.start, 0)

        # Inicializar el diccionario de nodos explorados como vacío
        explored = {}

        # Inicializar la frontera con una cola de prioridad
        frontier = PriorityQueueFrontier()

        # Agregar el nodo inicial a la frontera
        frontier.add(node, int(grid.heuristic(grid.start, grid.end)))

        # Comenzar la búsqueda
        while not frontier.is_empty():
            # Sacar el nodo con mayor prioridad de la frontera
            current_node = frontier.pop()

            # Comprobar si el nodo actual es el objetivo
            if current_node.state == grid.end:
                return Solution(current_node, explored)

            # Marcar el nodo actual como explorado
            explored[current_node.state] = True

            # Obtener los vecinos del nodo actual
            neighbors = grid.get_neighbours(current_node.state)

            # Expandir los vecinos
            for action, neighbor_state in neighbors.items():
                # Calcular el valor heurístico para el estado del vecino
                heuristic_value = grid.heuristic(neighbor_state, grid.end)

                # Crear un nuevo nodo para el vecino
                new_node = Node("", neighbor_state, current_node.cost + 1)

                # Si el vecino no ha sido explorado y no está en la frontera, agregarlo a la frontera
                if neighbor_state not in explored and not frontier.contains_state(neighbor_state):
                    frontier.add(new_node, int(heuristic_value))

        # Si no se encuentra una solución
        return NoSolution(explored)
#class GreedyBestFirstSearch:
 #   @staticmethod
   # def search(grid: Grid) -> Solution:
     #   """Find path between two points in a grid using Greedy Best First Search

      #  Args:
       #     grid (Grid): Grid of points

       # Returns:
       #     Solution: Solution found
       # """
        # Initialize a node with the initial position
        #node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
      #  explored = {} 
        
        # Add the node to the explored dictionary
       # explored[node.state] = True
        
      #  return NoSolution(explored)
