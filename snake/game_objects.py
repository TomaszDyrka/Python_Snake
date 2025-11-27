import random
import curses
import sys
import snake.constants as constants
import snake.utils as utils

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
        self.game_window = curses.newwin(height+2, (width*3)+2, 0, 0) # every horizontal element is in 'space 3 wide','+2' is for the borders
        self.game_window.border()
        self.game_window.timeout(constants.DEFAULT_FRAME_WAIT)
        curses.noecho()
        curses.cbreak()

        self.input_ = -1
        self.direction = (1,0) # snake going right by default
        self.status_code = 1 # -1 - game over, 1 - all good, 2 - game won

    def run(self):  
        """Method with main game loop. Consists of 3 next parts: input -> logic -> printing"""

        self.map.print_board(self.game_window)

        while(True):
            self.input_ = chr(value) if (value := self.game_window.getch()) != -1 else value

            self.update_handler() # logic

            self.print_handler() # printing

   
    def update_handler(self):
        """Handles game logic, snake position, etc.""" 

        # 1) move snake - pos = (x,y)

        # down:    (0,1)
        # up:      (0,-1)
        # left:    (-1,0)
        # right:   (1,0)

        match self.input_:
            case 's':
                if utils.is_reverse(self.direction, (0,1)):
                    self.direction = (0,1)
            case 'w':
                if utils.is_reverse(self.direction, (0,-1)):
                    self.direction = (0,-1)
            case 'a':
                if utils.is_reverse(self.direction, (-1,0)):
                    self.direction = (-1,0)
            case 'd':
                if utils.is_reverse(self.direction, (1,0)):
                    self.direction = (1,0)
            case _:
                pass

        self.map.main_list.move_snake(self.direction)

        # 2) check collisions
        s_pos_x, s_pos_y = self.map.main_list[-1] # head coords
        f_pos_x, f_pos_y = self.map.main_list.get_fruit() # fruit coords
        
        if (0 <= s_pos_x < self.map.board_size[0]) and (0 <= s_pos_y < self.map.board_size[1]): # if head doesnt hit the wall
            for i in range(self.map.main_list.length - 2): # '-2' is for not counting fruit and head
                body_part_pos = self.map.main_list[i+1]

                if (s_pos_x == body_part_pos[0]) and (s_pos_y == body_part_pos[1]): # if head hits the body
                    self.status_code = -1
                    return

            # now that lose conditions were checked, need to check fruit collision
            if (s_pos_x == f_pos_x) and (s_pos_y == f_pos_y): # if head hits fruit
                self.status_code = self.map.spawn_fruit()
                return 

        else: # if head hits the wall
            self.status_code = -1
            return        

        self.status_code = 1

        
    def print_handler(self):
        """Prints current state of the board"""

        if self.status_code == -1: # game over
            curses.echo()
            curses.endwin()
            print("GAME OVER! | SCORE: " + str(self.map.main_list.length - 1))
            sys.exit(1)

        elif self.status_code == 1: # normal print        
            self.map.print_board(self.game_window)

        elif self.status_code == 2: # game won
            curses.endwin()
            print("YOU WON!")
            sys.exit(0)

        else:
            curses.endwin()
            print(self.status_code)
        

class Map:
    # random
    # 
    # 0 - empty  -> .
    # 1 - body   -> #
    # 2 - head   -> @
    # 3 - fruit  -> *

    def __init__( self, n: int, m: int):
        """
        Initialize new class instance.
        """
        self.board_size = (n,m)
        self.board_list = [(i,j) for i in range(n) for j in range(m)] # all the possible positions
        self.main_list = utils.SnakeLinked_List(constants.DEFAULT_FRUIT, constants.DEFAULT_SNAKE) # list containing snake and fruit

        # main_list[index]:
        # 0  -> current position of fruit
        # 1  -> snakes tail
        # -1 -> snakes head

        # fruit starts at (8,6), snake at ([3-5],6)

    def spawn_fruit( self ) -> int:
        """Spawns new fruit after previous eaten and assigns it to the main list, expands the snake afterwards
        Returns:
            return code (int): code for: 1 - normal spawn; 2 - end of the game (no more tiles to spawn)"""

        self.main_list.expand_snake()

        points_pool = self.main_list.diff(self.board_size[0], self.board_size[1])

        if not points_pool:
            return 2

        self.main_list.set_fruit(random.choice(points_pool))
        return 1

    def print_board( self, window:curses.window ) -> None:
        """Prints board in the given window"""
        occupied_set = self.main_list.to_set()

        for y in range( self.board_size[1] ):    
            to_print = ''

            for x in range( self.board_size[0] ):
                current_pos = (x, y)

                if current_pos in occupied_set and current_pos == self.main_list[0]:
                    to_print += ' * '

                elif current_pos in occupied_set and current_pos == self.main_list[-1]:
                    to_print += ' @ '

                elif current_pos in occupied_set:
                    to_print += ' # '

                else:
                    to_print += '   '
            
            window.addstr(y+1, 1, to_print)

        x_pos, y_pos = self.main_list[-1]
        # for testing correct input
        # to_print = str(x_pos) + ',' + str(y_pos) + ':' + str(len(self.main_list))
        # window.addstr(0,0,to_print)
        curses.curs_set(0)
        window.refresh()
            

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