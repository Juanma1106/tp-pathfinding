from ..models.grid import Grid
from ..models.frontier import *
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Inicializar un nodo con la posición inicial
        nodo_inicio = Node("", grid.start, 0)

        # Inicializar el diccionario de nodos explorados como vacío
        explorado = {}

        # Inicializar la frontera con una cola de prioridad
        frontera = PriorityQueueFrontier()

        # Agregar el nodo inicial a la frontera
        frontera.add(nodo_inicio, nodo_inicio.cost)

        # Comenzar la búsqueda
        while not frontera.is_empty():
            # Sacar el nodo de costo mínimo de la frontera
            nodo_actual = frontera.pop()

            # Comprobar si el nodo actual es el objetivo
            if nodo_actual.state == grid.end:
                return Solution(nodo_actual, explorado)

            # Marcar el nodo actual como explorado
            explorado[nodo_actual.state] = True

            # Obtener los nodos vecinos del nodo actual
            vecinos = grid.get_neighbours(nodo_actual.state)

            # Expandir los nodos vecinos
            for accion, estado in vecinos.items():
                # Calcular el costo acumulado para llegar al vecino desde el nodo actual
                nuevo_costo = nodo_actual.cost + grid.get_cost(estado)

                # Si el vecino no ha sido explorado o está en la frontera con un costo menor, agregarlo a la frontera
                if estado not in explorado:
                    frontera.add(Node("", estado, nuevo_costo, nodo_actual, accion), nuevo_costo)
                    explorado[estado] = True  # Marcar el vecino como explorado
                elif frontera.get(estado) is None or frontera.get(estado)[0] > nuevo_costo: # type: ignore
                    frontera.add(Node("", estado, nuevo_costo, nodo_actual, accion), nuevo_costo)

        # Si no se encuentra una solución
        return NoSolution(explorado)
#class UniformCostSearch:
   # @staticmethod
   # def search(grid: Grid) -> Solution:
   #     """Find path between two points in a grid using Uniform Cost Search

     #   Args:
     #       grid (Grid): Grid of points

      #  Returns:
        #    Solution: Solution found
      #  """
       # # Initialize a node with the initial position
       # node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
       # explored = {} 
        
        # Add the node to the explored dictionary
       # explored[node.state] = True
        
        #return NoSolution(explored)
