import random
from dataclasses import dataclass

class Map:
    # random
    # 
    # 0 - pusto -> .
    # 1 - ciało -> #
    # 2 - głowa -> @
    # 3 - owoc  -> *

    def __init__( self, n: int, snake: "Snake" ):
        
        self.board_size = max(n, 8)
        self.board = [ [ 0 for _ in range(self.board_size) ] for _ in range(self.board_size) ]

        self.snake = snake

        # indeksy:
        # 0  - owoc
        # 1  - najdalsze ciało (ogon)
        # -1 - głowa
        self.taken_squares = [0]

        for point in self.snake.body:
            self.board[point.x][point.y] = 1 
            self.taken_squares.append(point)

        self.spawn_fruit()

        print(self.taken_squares)

    def spawn_fruit( self ) -> None:
        x_axis_used = set()
        y_axis_used = set()
        
        for point in self.taken_squares[1:]:
            x_axis_used.add(point.x)
            y_axis_used.add(point.y)

        x_fruit = random.choice(set(range(self.board_size)) - x_axis_used)
        y_fruit = random.choice(set(range(self.board_size)) - y_axis_used)

        self.taken_squares[0] = Point(x_fruit, y_fruit)
        


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



@dataclass
class Point:
    # dataclasses
    x: int
    y: int

class Snake:
    
    body = [Point(1,3),Point(1,4),Point(1,5)]        


class Snake_Head(Snake):
    pass

class Snake_Body(Snake):
    pass

class Fruit(Point):
    pass


s = Snake
m = Map(3,s)
