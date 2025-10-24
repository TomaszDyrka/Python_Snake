import snake.game_objects as game_obj
import curses
import sys

def main():
    if len(sys.argv) != 3:
        print("In order to play the game, you need to provide the board dimensions.\n"
              "Example: python main.py 13 13 (where 13 <= X,Y <= 45)")
        sys.exit(2)

    try:
        x = int(sys.argv[1])
        y = int(sys.argv[2])

        Game = game_obj.Game(x, y)
        Game.run()

    except ValueError:
        print("Please provide valid integer dimensions (e.g. python main.py 13 13).")
        sys.exit(3)
    except Exception as e:
        print("Something went wrong!\n")
        print(e)
        sys.exit(4)

if __name__ == '__main__':
    main()
