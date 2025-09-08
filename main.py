from dataclasses import dataclass
from snake import utils
from snake import constants
from threading import Thread
import time
import random
import sys, termios, tty

class Game:
    def __init__(self, width:int, height:int):
        self.map = Map(width, height)
        self.input_ = None
        self.direction = (1,0) # snake going right by default

    def run(self):  
        while(True):
            t_now = time.time()

            direction = self.input_handler()
            self.update_handler(direction)

            delta = time.time() - t_now 
            if(delta < constants.DEFAULT_FRAME_STEP):
                time.sleep(constants.DEFAULT_FRAME_STEP - delta)

            self.print_handler()
            

    def input_handler(self):
        def getch():
            import sys, termios, tty

            fd = sys.stdin.fileno()
            orig = termios.tcgetattr(fd)

            try:
                tty.setcbreak(fd)  # or tty.setraw(fd) if you prefer raw mode's behavior.
                return sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSAFLUSH, orig)


        def check():
            time.sleep(1)
            if self.input_ != None:
                print(self.input_)
                return
            print("Too Slow")

        Thread(target = check).start()

        self.input_ = getch()


    def update_handler(self):
        
        # left:     (1,0)
        # right:    (-1,0)
        # up:       (0,1)
        # down:     (0,-1)

        match self.input_:
            case 'a':
                direction = (1,0)
            case 'd':
                direction = (-1,0)
            case 'w':
                direction = (0,1)
            case 's':
                direction = (0,-1)


        pass
    def print_handler(self):
        pass

class Map:
    # random
    # 
    # 0 - empty  -> .
    # 1 - body   -> #
    # 2 - head   -> @
    # 3 - fruit  -> *

    def __init__( self, n: int = 13, m: int = 13):
        """
        Initialize new class instance

        Args:
            n (int): board width (x); min value - 13, max - 45
            m (int): board height (y); min value - 13, max - 45
        """

        self.board_size = ( (min(max(n,13),45)) , min(max(m,13),45) ) # 13 <= n/m <= 45; 45*45 < 2048

        self.board_list = [(i,j) for i in range(self.board_size[0]) for j in range(self.board_size[1])] 
        self.main_list = utils.SnakeLinked_List(constants.DEFAULT_FRUIT, constants.DEFAULT_SNAKE)

        # main_list[index]:
        # 0  -> current position of fruit
        # 1  -> snakes tail
        # -1 -> snakes head

        # fruit starts at (8,6), snake at ([3-5],6)

    def spawn_fruit( self ) -> None:
        """Spawns new fruit after previous eaten and assigns it to the main list"""

        points_pool = self.main_list.diff(self.board_size[0], self.board_size[1])
        self.main_list.set_fruit(random.choice(points_pool))

    def print_board( self ) -> None:
        """Prints board"""
        occupied_set = self.main_list.to_set()

        print("+" + ("-" * 3) * self.board_size[0] + "+")
        for i in range( self.board_size[0] ):    
            to_print = '|'

            for j in range( self.board_size[1] ):
                current_pos = (i, j)

                if current_pos in occupied_set and current_pos == self.main_list[0]:
                    to_print += ' * '

                elif current_pos in occupied_set and current_pos == self.main_list[-1]:
                    to_print += ' @ '

                elif current_pos in occupied_set:
                    to_print += ' # '

                else:
                    to_print += '   '
            
            print(to_print + "|")

        print("+" + ("-" * 3) * self.board_size[0] + "+")

m1 = Map(7,7)
m2 = Map(46,46)
m3 = Map(13,13)

print(m1.board_size)
print(m2.board_size)
print(m3.board_size)

#m3.print_board()
#m3.spawn_fruit()
#m3.print_board()

g_test = Game(3,3)

g_test.input_handler()