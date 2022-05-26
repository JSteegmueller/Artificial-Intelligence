# # Assignment 06 - Simulated Annealing

#########################################
# Student1 Name:
# Matriculation No1:

# Student2 Name:
# Matriculation No2:
#########################################

import copy
import numpy as np
import random
import math

np.random.seed(2021)
random.seed(2021)


def number_inversions(board):
    """
    E1: number of inversions
    Args:
        board: 
    Returns:
        number of inversions of the board
    """
    out = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            for k in range(i, len(board)):
                if k == i:
                    for m in range(j, len(board[0])):
                        if board[k][m] > 0 and board[k][m] < board[i][j]:
                            out += 1
                else:
                    for m in range(len(board[0])):
                        if board[k][m] > 0 and board[k][m] < board[i][j]:
                            out += 1
    return out


def number_misplaced(board):
    """
    E2: number of misplaced tiles
    Args:
        board:
    Returns:
        number of misplaced tiles
    """
    out = 0
    for k in range(len(board)):
        for j in range(len(board[0])):
            if board[k][j] > 0 and not board[k][j] == goal[k][j]:
                out += 1
    return out


def manhattan_distance(board):
    """
      E3: Manhattan distance between the tiles
      Args:
          board:
      Returns:
         distance
    """
    out = 0
    dimx = len(board[0])
    for k in range(len(board)):
        for j in range(len(board[0])):
            if not board[k][j] == 0:
                distance_x = np.abs((board[k][j] % dimx) - j)
                distance_y = np.abs(np.floor(board[k][j] / 3) - k)
                out += distance_x + distance_y
    return out


def energy(board, which_one):
    """
      For given board compute the energy according to the selected energy function
      Args:
          board:
          which_one: energy function to choose between 1, 2 or 3
      Returns:
         the energy
    """

    if which_one == 1:
        return number_inversions(board)
    elif which_one == 2:
        return number_misplaced(board)
    elif which_one == 3:
        return manhattan_distance(board)


def successor(board):
    """
    This function selects the successor state from the current board state
    Args:
          board:
      Returns:
         the successor state
    """
    posx = 0
    posy = 0
    swapped = copy.deepcopy(board)
    for k in range(len(board)):
        for j in range(len(board[0])):
            if board[k][j] == 0:
                posx = k
                posy = j
    randx = 0
    randy = 0
    if np.random.randint(low=0, high=2) == 1:
        randx = 2 * np.random.randint(low=0, high=2) - 1
    else:
        randy = 2 * np.random.randint(low=0, high=2) - 1
    while (randx + posx >= len(board) or randx + posx < 0) or (randy + posy >= len(board[0]) or randy + posy < 0):
        randx = 0
        randy = 0
        if np.random.randint(low=0, high=2) == 1:
            randx = 2 * np.random.randint(low=0, high=2) - 1
        else:
            randy = 2 * np.random.randint(low=0, high=2) - 1
    swapped[posx][posy] = swapped[posx + randx][posy + randy]
    swapped[posx + randx][posy + randy] = 0
    return swapped


def scheduler(step):
    """Scheduler should be a function that takes an integer step parameter.
      Args:
          step: current step
      Returns:
         computed scheduler value
    """
    return 1/(math.sqrt(step)) + 1

def simulated_annealing(board, which_energy=1):
    """Implements the simulated annealing algorithm
    Args:
          board: initial board state
          which_energy: (default E1) what energy function to use
    Returns:
         number of steps taken to solve the problem
    """
    step = 1
    current = copy.deepcopy(board)
    while True:
        if current == [[0,1,2],[3,4,5],[6,7,8]]:
            break
        # TODO: Q3(a-ii)

        t = scheduler(step)
        next = successor(current)
        de = energy(current, which_energy) - energy(next, which_energy)
        probability = math.exp(de/t)
        step += 1
        if step % 10000 == 0: print('step =', step)
        if step > 1000000: break
        if de > 0 or random.random() < probability:
            current = next
            continue
    return step


def compare_energies(num_runs=20):
    """
    Execute the simulated annealing multiple times (20 by default)
    and average the results.
       Args:
          num_runs: (default 20) number of runs per energy function to do for averaging
        Returns:
        dictionary containing average number of steps required in num_runs
       """
    results = {"E1": 0, "E2": 0, "E3": 0}  # TODO fill this dictionary with average number of steps over num_runs
    # TODO: Q3(b)
    for i in range(1,4):
        avg = 0
        for _ in range(num_runs):
            intial_state = [[8, 1, 7], [5, 4, 2], [0, 6, 3]]
            avg += simulated_annealing(intial_state, i)
        avg /= num_runs
        results[f"E{i}"] = avg
    return results

if __name__ == "__main__":
    """ 8-puzzle problem """
    goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    intial_state = [[8, 1, 7], [5, 4, 2], [0, 6, 3]]

    simulated_annealing(intial_state, which_energy = 1)

    results = compare_energies(20)
    print(results)
