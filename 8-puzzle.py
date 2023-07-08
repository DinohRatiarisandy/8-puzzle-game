"""
This script creates an interactive GUI-based 8-puzzle game using the Pygame library. The player can move tiles by clicking on them.
The goal of the game is to rearrange the tiles to reach the desired goal state.
1 2 3
4 5 6
7 8

The game includes an A* algorithm solver, implemented in the 'ia' module, to find the solution path for the current puzzle configuration.
The solver utilizes the A* search algorithm to efficiently explore the puzzle state space and determine the optimal sequence of moves.

Usage:
1. Run the script to start the 8-puzzle game.
2. Use the mouse to click on a tile adjacent to the empty space to move it into the empty space.
3. Press the SPACE key to start the solver and find the solution path. The solver will automatically move the tiles to reach the goal state.
4. Press the RETURN key to reset the game and generate a new random puzzle configuration.
5. Press the ESCAPE key or close the game window to exit the game.

Note: The game will run at a frame rate of 60 frames per second.

Dependencies:
- pygame 2.3.0 (SDL 2.24.2, Python 3.11.2)
- The 'gameplay' module, which contains the Game class for managing the game logic.
- The 'constants' module, which defines various constants used in the game.
- The 'ia' module, which includes the AStarSolver class for solving the puzzle using the A* algorithm.

Author: [dinoh__sandys]
Date: [08/07/2023]
"""

import pygame
import sys
from gameplay import Game
from constants import *
from ia import AStarSolver

# Initialize Pygame
pygame.init()

# Set the window caption
pygame.display.set_caption('8-PUZZLE')

# Initialize the clock
CLOCK = pygame.time.Clock()

# Create a new game instance
game = Game()

# Create an A* solver instance
resolver_ia = AStarSolver(game.initial_state, game.goal_state)

# Main game loop
while True:
    # Fill the screen with the background color
    SCREEN.fill(BACKGROUND)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game if the window is closed
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Reset the game if ENTER key is pressed
                # Generate a new game (new state)
                game.reset()
                resolver_ia = AStarSolver(game.initial_state, game.goal_state)
                resolver_ia.reset()

            if event.key == pygame.K_ESCAPE:
                # Quit the game if ESCAPE key is pressed
                pygame.quit()
                sys.exit()

            if event.key == pygame.K_SPACE and not game.solved and not resolver_ia.is_running:
                # Solve the puzzle if SPACE key is pressed and the game is not already solved or the solver is already running
                solution_path = resolver_ia.solve()
                resolver_ia.is_running = True

        if event.type == pygame.MOUSEBUTTONDOWN and not game.solved:
            # Move a tile when a mouse button is clicked, if the game is not already solved
            pos_x = event.pos[1] // (WIDTH // 3 - SPACECING)
            pos_y = event.pos[0] // (HEIGHT // 3 - SPACECING)
            game.move_tile(pos_x, pos_y)

    if resolver_ia.solution_path:
        # Update the game board with the next state from the solution path, with a delay
        game.initial_state = solution_path.pop()
        pygame.time.wait(270)

    # Draw the game board
    game.draw_board()

    if game.is_solved():
        # Draw the winning message if the game is solved
        game.draw_win()

    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    CLOCK.tick(60)
