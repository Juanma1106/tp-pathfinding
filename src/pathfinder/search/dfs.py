from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Inicializar un nodo con la posición inicial
        nodo_inicio = Node("", grid.start, 0)

        # Inicializar el diccionario de nodos explorados como vacío
        explorado = {}

        # Inicializar la frontera como una pila
        frontera = StackFrontier()
        
        # Agregar el nodo inicial a la frontera
        frontera.add(nodo_inicio)
        
        # Comenzar la búsqueda
        while not frontera.is_empty():
            # Sacar el nodo más reciente de la frontera
            nodo_actual = frontera.remove()

            # Marcar el nodo actual como explorado
            explorado[nodo_actual.state] = True
            
            # Comprobar si el nodo actual es el objetivo
            if nodo_actual.state == grid.end:
                return Solution(nodo_actual, explorado)
            
            # Obtener los nodos vecinos del nodo actual
            vecinos = grid.get_neighbours(nodo_actual.state)
            
            # Expandir los nodos vecinos
            for accion, estado in vecinos.items():
                # Crear un nuevo nodo para el vecino
                nuevo_nodo = Node("", estado, nodo_actual.cost + grid.get_cost(estado), nodo_actual, accion)
                
                # Si el vecino no ha sido explorado ni está en la frontera, agregarlo a la frontera
                if estado not in explorado and not frontera.contains_state(estado):
                    frontera.add(nuevo_nodo)
        
        # Si no se encuentra una solución
        return NoSolution(explorado)
#class DepthFirstSearch:
  #  @staticmethod
  #  def search(grid: Grid) -> Solution:
    #    """Find path between two points in a grid using Depth First Search

      #  Args:
      #     grid (Grid): Grid of points
            
      # Returns:
      #      Solution: Solution found
       # """
        # Initialize a node with the initial position
      #  node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
       # explored = {} 
        
        # Add the node to the explored dictionary
       # explored[node.state] = True
        
        #return NoSolution(explored)
