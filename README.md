# 🐍 Snake (Terminal Edition)

A classic Snake game written in pure Python, playable directly in your terminal.
Control the snake, eat the fruits, and avoid colliding with yourself or the walls!

---

## 🎮 How to Play

Run the game from your terminal:

```bash
python main.py <width> <height>
```

Example:

```
python main.py 13 13
```

- Both width and height must be between 13 and 45.

- The game will launch with a board of the given dimensions.

- Use WASD, control the snake’s movement.

- Pressing a key more than once (or holding it) causes the snake to go faster!

The game ends if:

- you hit the wall 🧱
- or you run into yourself 🌀

⚙️ Requirements

- Python 3.8+ (probably lower, I've written it on 3.13) 

- Curses library (installed by default on Linux and MacOS)

- Works natively in any terminal — no extra external libraries required (unless you added additional features).

📁 Project Structure
```
snake/
│
├── main.py              # Entry point — runs the game
├── game_obj/
│   ├── __init__.py      # Secures proper importing inside files.
│   ├── constants.py     # Has several useful game-defining numbers.
│   ├── game_objects.py  # Contains the Game class and Map class, determines most of game's rules.
│   └── utils.py         # Holds data structures, defines most of critical behaviour.
└── README.md            # Project documentation.
```

🧩 Features

- Adjustable board size

- Terminal-based interface

- Simple and responsive controls

- Clear error messages for invalid input

- Lightweight and dependency-free

💡 Troubleshooting

If you see:

```
In order to play the game, you need to provide the board dimensions.

```

or

```
Please provide valid integer dimensions (e.g. python main.py 13 13)
```

Try running it again with two numbers (13 <= X,Y <= 45), for example:

```
python main.py 13 13
```

🧑‍💻 Author

Created by Tomasz Dyrka

⚖️ License

This project is licensed under the Creative Commons Attribution–NonCommercial 4.0 International (CC BY-NC 4.0) license.
You are free to:

Share — copy and redistribute the material in any medium or format

Adapt — remix, transform, and build upon the material

Under the following terms:

Attribution — You must give appropriate credit and indicate if changes were made.

NonCommercial — You may not use the material for commercial purposes.

For more details, see the full license text:
https://creativecommons.org/licenses/by-nc/4.0/

🌟 Future Ideas

- Score tracking and leaderboard

- Difficulty levels (in form of speed adjustment)

- ASCII animations (maybe) and better terminal graphics (necessarily)

