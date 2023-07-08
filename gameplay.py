"""
The 'gameplay' module provides a Game class that manages the logic of the 8-puzzle game. It handles generating valid game boards, shuffling the tiles, moving tiles based on user input, checking for a solved state, drawing the game board on the screen, and resetting the game.

Usage:
- Create an instance of the Game class to start a new game.
- Use the 'move_tile' method to move tiles on the board based on user input.
- Use the 'is_solved' method to check if the game is solved.
- Use the 'draw_board' method to draw the current game board on the screen.
- Use the 'reset' method to reset the game and generate a new valid board.

Classes:
- Game: Manages the game logic of the 8-puzzle game.

Attributes (Game class):
- solved (bool): Indicates whether the game is solved.
- goal_state (list): The target state of the game.
- initial_state (list): The initial state of the game.

Methods (Game class):
- __init__: Initializes a Game object.
- generate_valid_board: Generates a valid game board by shuffling the goal state.
- shuffle: Shuffles the entire state by performing random swaps.
- swap: Swaps two numbers in different positions on the board.
- is_solvable: Determines if the board is solvable or not.
- get_blank_pos: Returns the position of the blank tile on the board.
- is_neighbor: Determines if a position is a neighbor of another position.
- move_tile: Moves a tile to the specified position.
- is_solved: Checks if the game is solved.
- draw_win: Draws the "You Won!" message on the screen.
- draw_board: Draws the game board on the screen.
- reset: Resets the game by generating a new valid board.

Dependencies:
- The 'copy' module for performing deep copies.
- The 'random' module for generating random numbers.
- The 'pygame' module for GUI functionality.
- The 'constants' module for defining various constants used in the game.

Author: [dinoh__sandys]
Date: [08/07/2023]
"""


import copy
import random
import pygame
from constants import *

class Game:
    def __init__(self):
        """
        Initializes a Game object.

        Attributes:
        - solved (bool): Indicates whether the game is solved.
        - goal_state (list): The target state of the game.
        - initial_state (list): The initial state of the game.
        """
        self.solved = False
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.initial_state = self.generate_valid_board(copy.deepcopy(self.goal_state))
    
    def generate_valid_board(self, state):
        """
        Generates a valid board by shuffling the given state.

        Parameters:
        - state (list): The state to be shuffled.

        Returns:
        - board (list): The shuffled board.
        """
        board = self.shuffle(state)
        
        while not self.is_solvable(board):
            board = self.shuffle(state)
        
        return board
    
    def shuffle(self, state):
        """
        Shuffles the entire state by performing random swaps.

        Parameters:
        - state (list): The state to be shuffled.

        Returns:
        - state (list): The shuffled state.
        """
        for _ in range(50):
            pos_A = (random.randint(0, 2), random.randint(0, 2))
            pos_B = (random.randint(0, 2), random.randint(0, 2))

            while pos_A == pos_B:
                pos_B = (random.randint(0, 2), random.randint(0, 2))
                pos_A = (random.randint(0, 2), random.randint(0, 2))

            self.swap(pos_A, pos_B, state)

        return state

    def swap(self, pos_A, pos_B, board):
        """
        Swaps two numbers in different positions on the board.

        Parameters:
        - pos_A (tuple): The position of the first number to swap.
        - pos_B (tuple): The position of the second number to swap.
        - board (list): The game board.

        Returns:
        None
        """
        i, j = pos_A
        k, l = pos_B
        board[i][j], board[k][l] = board[k][l], board[i][j]

    def is_solvable(self, state):
        """
        Determines if the board is solvable or not.

        Parameters:
        - state (list): The game state.

        Returns:
        - solvable (bool): True if the board is solvable, False otherwise.
        """
        flatten_state = [num for row in state for num in row]
        inversions = 0

        for i in range(len(flatten_state)):
            if flatten_state[i] == 0:
                continue
            for j in range(i + 1, len(flatten_state)):
                if flatten_state[j] == 0:
                    continue
                if flatten_state[i] > flatten_state[j]:
                    inversions += 1

        return inversions % 2 == 0

    def get_blank_pos(self):
        """
        Returns the position of the blank tile on the board.

        Returns:
        - pos (tuple): The position of the blank tile.
        """
        for i in range(3):
            for j in range(3):
                if self.initial_state[i][j] == 0:
                    return (i, j)
    
    def is_neighbor(self, pos_A, pos_B):
        """
        Determines if pos_A is a neighbor of pos_B.

        Parameters:
        - pos_A (tuple): The position to check.
        - pos_B (tuple): The reference position.

        Returns:
        - neighbor (bool): True if pos_A is a neighbor of pos_B, False otherwise.
        """
        if pos_A[0] == pos_B[0] and abs(pos_A[1] - pos_B[1]) == 1:
            return True
        elif pos_A[1] == pos_B[1] and abs(pos_A[0] - pos_B[0]) == 1:
            return True
    
    def move_tile(self, pos_x, pos_y):
        """
        Moves the tile to the specified position.

        Parameters:
        - pos_x (int): The x-coordinate of the tile's position.
        - pos_y (int): The y-coordinate of the tile's position.

        Returns:
        None
        """
        blank_pos = self.get_blank_pos()

        if blank_pos != (pos_x, pos_y):
            if blank_pos[0] == pos_x or blank_pos[1] == pos_y:
                if self.is_neighbor(blank_pos, (pos_x, pos_y)):
                    self.swap(blank_pos, (pos_x, pos_y), self.initial_state)

    def is_solved(self):
        """
        Checks if the game is solved.

        Returns:
        - solved (bool): True if the game is solved, False otherwise.
        """
        if self.initial_state == self.goal_state:
            self.solved = True
            return True

        return False

    def draw_win(self):
        """
        Draws the "You Won!" message on the screen.

        Returns:
        None
        """
        font = pygame.font.Font('freesansbold.ttf', 24)

        pygame.draw.rect(SCREEN, 'black', [50, 50, 300, 200], 0, 10)

        won_text1 = font.render(f'You Won!', True, 'white')
        won_text2 = font.render('Press ENTER to restart', True, 'white')
        won_text3 = font.render('Press ESCAPE to quit', True, 'white')

        SCREEN.blit(won_text1, (140, 65))
        SCREEN.blit(won_text2, (70, 145))
        SCREEN.blit(won_text3, (70, 185))

    def draw_board(self):
        """
        Draws the game board on the screen.

        Returns:
        None
        """
        font = pygame.font.Font('freesansbold.ttf', 42)
        for i in range(3):
            for j in range(3):
                val = self.initial_state[i][j]
                pos_x = j * WIDTH // 3 + SPACECING
                pos_y = i * HEIGHT // 3 + SPACECING
                width_rect = WIDTH // 3 - 2 * SPACECING
                height_rect = HEIGHT // 3 - 2 * SPACECING

                board_rect = pygame.Rect(pos_x, pos_y, width_rect, height_rect)

                if val:
                    border_rect = pygame.Rect(pos_x, pos_y, width_rect, height_rect)
                    pygame.draw.rect(SCREEN, (43, 52, 66), border_rect, 1, 5)
                    pygame.draw.rect(SCREEN, COLR_TILE, board_rect, border_radius=5)
                    text_surface = font.render(str(val), True, COLR_NUM)
                    text_rect = text_surface.get_rect(center=(pos_x + width_rect//2, pos_y + height_rect//2))
                    SCREEN.blit(text_surface, text_rect)
                    pygame.draw.rect(
                        SCREEN, 'black',
                        [pos_x, pos_y, WIDTH//3-2*SPACECING, HEIGHT//3-2*SPACECING],
                        1, 5
                    )
                else:
                    pygame.draw.rect(SCREEN, BACKGROUND, board_rect, border_radius=5)

    def reset(self):
        """
        Resets the game by generating a new valid board.

        Returns:
        None
        """
        self.solved = False
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        self.initial_state = self.generate_valid_board(copy.deepcopy(self.goal_state))
