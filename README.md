# 🐍 Snake (Terminal Edition)

A classic Snake game written in pure Python - playable directly in your terminal.
Control the snake, eat fruit, and avoid colliding with yourself or the walls!

---

## 🎮 How to Play

### Docker

You can build the Docker container using the provided Dockerfile.

First, build the image:

```bash
docker build -t python-snake .
```

Then, run it:

```bash
docker run -it python-snake [COMMAND] [ARGUMENTS]
```

**Available commands (`[COMMAND]`):**

* `run [width] [height]` - for running the game (e.g., `docker run -it python-snake run 20 20`)
* `test` - for running tests
* `bash` - for accessing the internal shell

### Native

Run the game from your terminal:

```bash
python main.py <width> <height>
```

Example:

```bash
python main.py 13 13
```

- Both width and height must be between 13 and 45.

- The game will launch with a board of the given dimensions.

- Use WASD to control the snake’s movement.

- Pressing or holding a key makes the snake to go faster!

The game ends if:

- you hit the wall 🧱

- or you run into yourself 🌀

⚙️ Requirements

- Python 3.8+ (tested on 3.13) 

- Curses library (installed by default on Linux and MacOS)

- Works natively in any terminal - no extra external libraries required (unless you added additional features).

📁 Project Structure

```
Python-Snake/
│
├── src/
│   ├── __init__.py              # Ensures proper importing within the project.
│   ├── main.py                  # Main file — runs the game.
│   └── snake/
│       ├── __init__.py          # Ensures proper importing within the project.
│       ├── constants.py         # Defines key game constants.
│       ├── game_objects.py      # Contains the Game and Map classes; defines most of the game’s rules.
│       └── utils.py             # Provides data structures and defines core behaviour.
├── tests/
│   └── test_data_structures.py  # Bundled up tests for data structures located in /src/snake/utils.py.
├── entrypoint.sh                # Entry point for docker image, to be able to run tests, the game, etc.
├── Dockerfile                   # File for easy container creation.
├── pyproject.toml               # Project metadata.
└── README.md                    # Project documentation.
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

- Difficulty levels (in the form of speed adjustment)

- ASCII animations (maybe) and better terminal graphics (necessarily)
