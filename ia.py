"""
The `AStarSolver` module provides a class for solving the 8-puzzle using the A* algorithm.
The 8-puzzle is a sliding puzzle game where the goal is to rearrange the numbered tiles from their initial configuration to a target configuration.
The A* algorithm is used to efficiently search for the optimal solution path.

Classes:
- AStarSolver: Represents an instance of the A* solver for the 8-puzzle.

Methods:
- __init__(initial_state, goal_state): Initializes an instance of the AStarSolver class with the initial and goal states of the puzzle.
- manhattan_dist(x1, y1, x2, y2): Calculates the Manhattan distance between two positions.
- calc_heuristic(state): Calculates the heuristic cost of a state using the Manhattan distance.
- get_goal_position(value): Returns the position of a value in the goal state.
- get_blank_position(state): Returns the position of the blank tile in a state.
- is_goal_state(state): Checks if a state is the goal state.
- generate_next_states(state): Generates the next possible states from a given state.
- solve(): Solves the 8-puzzle using the A* algorithm and returns the solution path.
- reset(): Resets the solver for a new resolution.

Usage:
1. Create an instance of the AStarSolver class with the initial and goal states.
2. Call the `solve()` method to solve the puzzle and retrieve the solution path.
3. Use the solution path to animate the puzzle's solution or perform any other desired operations.
4. Optionally, call the `reset()` method to reset the solver and start a new resolution.

Dependencies:
- The `heapq` module for priority queue implementation.
- The `copy` module for deep copying puzzle states.

Note: The A* solver uses a priority queue to explore states based on their heuristic cost and expected path cost. The Manhattan distance heuristic is used to estimate the cost from a state to the goal state.

Author: [dinoh__sandys]
Date: [08/07/2023]
"""


import heapq as hq
import copy

class AStarSolver:
    def __init__(self, initial_state, goal_state):
        """
        Initializes an instance of the AStarSolver class.

        Parameters:
        - initial_state (list): The initial state of the puzzle as a 3x3 list.
        - goal_state (list): The goal state of the puzzle as a 3x3 list.
        """        
        self.is_running = False
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.solution_path = []

    def manhattan_dist(self, x1, y1, x2, y2):
        """
        Calculates the Manhattan distance between two positions.

        Parameters:
        - x1, y1: The coordinates of the first position.
        - x2, y2: The coordinates of the second position.

        Returns:
        The Manhattan distance between the two positions.
        """
        return abs(x1 - x2) + abs(y1 - y2)

    def calc_heuristic(self, state):
        """
        Calculates the heuristic cost using the Manhattan distance.

        Parameters:
        - state (list): The current state of the puzzle as a 3x3 list.

        Returns:
        The heuristic cost of the state.
        """
        heuristic = 0
        for i in range(3):
            for j in range(3):
                value = state[i][j]
                if value != 0:
                    goal_pos = self.get_goal_position(value)
                    heuristic += self.manhattan_dist(i, j, goal_pos[0], goal_pos[1])
        return heuristic

    def get_goal_position(self, value):
        """
        Returns the position of a value in the goal state.

        Parameters:
        - value: The value to search for in the goal state.

        Returns:
        The position (row, column) of the value in the goal state.
        """
        for i in range(3):
            for j in range(3):
                if self.goal_state[i][j] == value:
                    return (i, j)

    def get_blank_position(self, state):
        """
        Returns the position of the blank tile in the state.

        Parameters:
        - state (list): The current state of the puzzle as a 3x3 list.

        Returns:
        The position (row, column) of the blank tile in the state.
        """
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return (i, j)

    def is_goal_state(self, state):
        """
        Checks if the state is the goal state.

        Parameters:
        - state (list): The current state of the puzzle as a 3x3 list.

        Returns:
        True if the state is the goal state, False otherwise.
        """
        return state == self.goal_state

    def generate_next_states(self, state):
        """
        Generates the next possible states from the current state.

        Parameters:
        - state (list): The current state of the puzzle as a 3x3 list.

        Returns:
        A list of next possible states.
        """
        next_states = []
        blank_pos = self.get_blank_position(state)
        pos_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

        for move in pos_moves:
            new_state = copy.deepcopy(state)
            x, y = blank_pos[0] + move[0], blank_pos[1] + move[1]

            if 0 <= x < 3 and 0 <= y < 3:
                new_state[blank_pos[0]][blank_pos[1]] = new_state[x][y]
                new_state[x][y] = 0
                next_states.append(new_state)

        return next_states

    def solve(self):
        """
        Solves the 8-puzzle using the A* algorithm.

        Returns:
        The solution path as a list of states from the initial state to the goal state.
        """
        priority_queue = []
        hq.heappush(priority_queue, (self.calc_heuristic(self.initial_state), self.initial_state))
        visited_states = set()
        came_from = {}

        while priority_queue:
            current_state = hq.heappop(priority_queue)[1]

            if self.is_goal_state(current_state):
                self.solution_path = [current_state]
                while current_state!=self.initial_state:
                    current_state = came_from[str(current_state)]
                    self.solution_path.append(current_state)

                return self.solution_path

            visited_states.add(str(current_state))
            next_states = self.generate_next_states(current_state)

            for next_state in next_states:
                if str(next_state) not in visited_states:
                    hq.heappush(priority_queue, (self.calc_heuristic(next_state), next_state))
                    came_from[str(next_state)] = current_state

    def reset(self):
        """
        Reset the IA and start a new resolution.
        """
        self.solution_path = []
        self.is_running = False
