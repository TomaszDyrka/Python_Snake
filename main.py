from dataclasses import dataclass
from snake import utils
from snake import constants
from threading import Thread
import time
import random
import curses
import sys, termios, tty

class Game:
    def __init__(self, width:int, height:int):
        """Initialize new class instance
        Args:
            n (int): board width (x); min value - 13, max - 45
            m (int): board height (y); min value - 13, max - 45
        """

        width = min(max(width,13),45) 
        height = min(max(height,13),45)
        
        # 13 <= n/m <= 45; 45*45 < 2048

        self.map = Map(width, height) # all the data of the state of the game

        self.scr = curses.initscr()
        self.game_window = curses.newwin(width+2, height+2, 0,0) # '+2' for the borders
        self.game_window.border()

        self.input_ = None
        self.direction = (1,0) # snake going right by default
        self.status_code = -1 # -1 - game over, 1 - all good, 2 - game won

    def run(self):  
        """Method with main game loop. Consists of 3 next parts: input -> logic -> printing"""

        while(True):
            t_now = time.time()

            direction = self.input_handler()
            self.update_handler(direction)

            delta = time.time() - t_now 
            if(delta < constants.DEFAULT_FRAME_STEP):
                time.sleep(constants.DEFAULT_FRAME_STEP - delta)

            self.print_handler()
            

    def input_handler(self):
        """Handles user input"""

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
        """Handles game logic, snake position, etc.""" 

        # 1) move snake

        # right:     (1,0)
        # left:      (-1,0)
        # up:        (0,-1)
        # down:      (0,1)

        match self.input_:
            case 'a':
                direction = (1,0)
            case 'd':
                direction = (-1,0)
            case 'w':
                direction = (0,1)
            case 's':
                direction = (0,-1)

        self.map.main_list.move_snake(direction)

        # 2) check collisions
        s_pos_x, s_pos_y = self.map.main_list[-1] # head coords
        f_pos_x, f_pos_y = self.map.main_list.get_fruit()
        
        if (0 <= s_pos_x <= self.map.self.map.board_size[0]) and (0 <= s_pos_y <= self.map.self.map.board_size[0]): # if head doesnt hit wall
            for body_part_pos in self.map.main_list:
                if (s_pos_x is body_part_pos[0]) and (s_pos_y is body_part_pos[1]): # if head hits the body
                    # now that lose conditions were checked, need to check fruit collision
                    self.status_code = -1
                    return

            if (s_pos_x is f_pos_x) and (s_pos_y is f_pos_y): # if head doesnt hit the body
                self.status_code = self.map.spawn_fruit()
                return 

        
    def print_handler(self):
        """Prints current state of the board"""

        if self.status_code is -1: # game over
            print("GAME OVER! | SCORE: " + self.map.main_list.length)
            sys.exit(1)

        elif self.status_code is 1: # normal print        
            self.map.print_board()

        elif self.status_code is 2: # game won
            print("YOU WON!")

        else:
            print(self.status_code)


class Map:
    # random
    # 
    # 0 - empty  -> .
    # 1 - body   -> #
    # 2 - head   -> @
    # 3 - fruit  -> *

    def __init__( self, n: int = 13, m: int = 13):
        """
        Initialize new class instance.

        

        self.board_list = [(i,j) for i in range(self.board_size[0]) for j in range(self.board_size[1])] # all the possible positions
        self.main_list = utils.SnakeLinked_List(constants.DEFAULT_FRUIT, constants.DEFAULT_SNAKE)       # list containing snake and fruit

        # main_list[index]:
        # 0  -> current position of fruit
        # 1  -> snakes tail
        # -1 -> snakes head

        # fruit starts at (8,6), snake at ([3-5],6)

    def spawn_fruit( self ) -> None:
        """Spawns new fruit after previous eaten and assigns it to the main list, expands the snake afterwards
        Returns:
            return code (int): code for: 1 - normal spawn; 2 - end of the game (no more tiles to spawn)"""

        self.main_list.expand_snake()

        points_pool = self.main_list.diff(self.board_size[0], self.board_size[1])

        if not points_pool:
            return 2

        self.main_list.set_fruit(random.choice(points_pool))
        return 1

    def print_board( self, window ) -> None:



    def old_print_board( self ) -> None:
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

m3.old_print_board()
m3.spawn_fruit()
m3.old_print_board()

#g_test = Game(3,3)

#g_test.input_handler()