from dataclasses import dataclass
from snake import utils
from snake import constants
import random

class Map:
    # random
    # 
    # 0 - empty  -> .
    # 1 - body   -> #
    # 2 - head   -> @
    # 3 - fruit  -> *

    def __init__( self, n: int, m: int):
        self.board_size = ( (min(max(n,13),45)) , min(max(m,13),45) ) # 13 <= n/m <= 45; 45*45 < 2048

        self.board_list = [(i,j) for i in range(self.board_size(0)) for j in range(self.board_size(1))] 
        self.main_list = utils.SnakeLinked_List(constants.DEFAULT_FRUIT, constants.DEFAULT_SNAKE)

        # occupied [index]:
        # 0  -> current position of fruit
        # 1  -> snakes tail
        # -1 -> snakes head

        # fruit starts at (8,6), snake at ([3-5],6)

    def spawn_fruit( self ) -> None:
        """Spawns new fruit after previous eaten and assigns it to the main list"""

        points_pool = set(self.board_list) - self.main_list.to_set()
        self.main_list.set_fruit(random.choice(points_pool))

    def print_board( self ) -> None:
        to_print = 'w'

        for i in range( self.board_size ):    
            for j in range( self.board_size ):
                match self.board[i][j]:
                    case 0:
                        to_print = '.'

                    case 1:
                        to_print = '#'

                    case 2:
                        to_print = '@'

                    case 3:
                        to_print = '*'
                    
                    case _:
                        to_print = 'e'

                print( to_print , end=" " )
            
            print()


s = Snake
m = Map(3,s)
