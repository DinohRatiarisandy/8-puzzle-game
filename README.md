# 8-Puzzle Game

This repository contains a Python implementation of the classic 8-puzzle game using the Pygame library. The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with eight numbered tiles and one blank tile. The goal of the game is to rearrange the tiles to reach a specific target configuration.

## Features

- Interactive GUI-based gameplay
- Randomly generated valid game boards
- A* algorithm solver to find the optimal solution path
- Mouse controls for moving tiles
- Visual indication of the solved state and win message

## Requirements

- Python (version 3.6 or higher)
- Pygame library 2.3.0

## Usage

1. Clone the repository to your local machine.
2. Install the required dependencies using `pip` or any package manager of your choice.
3. Run the `8-puzzle.py` script to start the 8-puzzle game.
4. Use the mouse to click on a tile adjacent to the empty space to move it into the empty space.
5. Press the SPACE key to start the solver and find the solution path. The solver will automatically move the tiles to reach the goal state.
6. Press the RETURN key to reset the game and generate a new random puzzle configuration.
7. Press the ESCAPE key or close the game window to exit the game.

## Credits

The implementation of the 8-puzzle game in this repository was created by [https://github.com/DinohRatiarisandy]. The A* algorithm solver is based on the work of `Peter Hart`, `Nils Nilsson` and `Bertram Raphael`, available at [https://en.wikipedia.org/wiki/A*_search_algorithm].

## License

MIT License

