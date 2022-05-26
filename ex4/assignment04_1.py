from itertools import product
from copy import copy

from typing import List


def h(state: List[int]):
    c = 0
    # TODO: implement a heuristic function as asked for on the sheet.
    ss = copy(state)
    for n in state:
        ss.pop(0)
        np = nm = n
        for nn in ss:
            nm -= 1
            np += 1
            if n == nn or nm == nn or np == nn:
                c += 1
    return c


def generate_successors(state: List[int]) -> List[List[int]]:
    dimension = len(state)
    successors = []

    # TODO: Compute all the successor states here. With the 'dimension'-assignment
    # as above, this can be implemented independent of the number of queens.
    for dim in range(dimension):
        for target in range(dimension):
            if target != state[dim]:
                newState = copy(state)
                newState[dim] = target
                successors.append(newState)
    return successors


def hill_climb(start: List[int], double_step=False):
    state, reached_goal, path_to_goal = start, h(start) == 0, [start]
    # TODO: Implement the main Hill Climbing Loop here:
    while True:
        if reached_goal:
            break
        successors = []
        if double_step:
            one_step_successors = generate_successors(state)
            for one_step_successor in one_step_successors:
                two_step_successors = generate_successors(one_step_successor)
                for two_step_successor in two_step_successors:
                    successors.append(two_step_successor)
        else:
            successors = generate_successors(state)
        successors.sort(key=h)
        next_state = successors.pop(0)
        if h(next_state) >= h(state):
            break
        state = next_state
        path_to_goal.append(state)
        if h(state) == 0:
            reached_goal = True
            break
    return path_to_goal, reached_goal


if __name__ == '__main__':
    # TODO: enter your solutions to (d) and (f) here:
    print(hill_climb([1, 7, 0, 3, 6, 4, 2, 0, 5], double_step=False))
    print(hill_climb([1, 7, 0, 3, 6, 4, 2, 0, 5], double_step=True))
    print(hill_climb([2, 4, 6, 3, 0, 7, 1, 8, 5], double_step=True))

    print(h([0, 0, 0, 0]))
    print(h([4, 3, 2, 5, 4, 3, 2, 3]))
    print(hill_climb([0, 3, 1, 2], double_step=True))
    print(hill_climb([0, 3, 1, 2], double_step=False))
    print(hill_climb([0, 0, 0, 0], double_step=True))
    print(hill_climb([0, 0, 0, 0], double_step=False))
    print(hill_climb([0, 0, 0, 0, 0, 0], double_step=False))
    print(hill_climb([0, 0, 0, 0, 0, 0], double_step=True))
