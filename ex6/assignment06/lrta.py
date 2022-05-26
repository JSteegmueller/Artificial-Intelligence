# # Assignment 06 - LRTA

#########################################
# Student1 Name:
# Matriculation No1:

# Student2 Name:
# Matriculation No2:
#########################################
# ## Initialization


class GridNode:
    def __init__(self, name, neighbours=[], dist_neighbours=[], h=None, H=None):
        """
        Args:
            name: The name of this / current node
            neighbours: A list containing of all the neighbour gridnodes
            dist_neighbours: The distance to each neighbor of the node (same order as self.neighbours)
            h: The heuristic h(s)
            H: H(s) the H table cost
        """
        self.neighbours = neighbours
        self.dist_neighbours = dist_neighbours
        self.name = name
        self.h = h
        self.H = H
        assert len(self.dist_neighbours) == len(self.neighbours)

    def get_distance(self, neighbour_node):
        """
        function to calculate the distance between node and its neighbour
        Args:
            neighbour_node: neighbour of the current object (self) whose distance we want to find

        Returns: distance between current node (self) and its neighbour node (neighbour_node)

        """
        idx = self.neighbours.index(neighbour_node)
        dist = self.dist_neighbours[idx]
        return dist


def initialize_all_nodes():
    """
       initialize all the nodes
    """
    node = {}
    node['A1'] = GridNode(name='A1', h=6, H=6)
    node['A2'] = GridNode(name='A2', h=6, H=6)
    node['A3'] = GridNode(name='A3', h=4, H=4)
    node['A4'] = GridNode(name='A4', h=3, H=3)
    node['A5'] = GridNode(name='A5', h=3, H=3)
    node['B1'] = GridNode(name='B1', h=5, H=5)
    node['B2'] = GridNode(name='B2', h=6, H=6)
    node['B3'] = GridNode(name='B3', h=5, H=5)
    node['B4'] = GridNode(name='B4', h=4, H=4)
    node['B5'] = GridNode(name='B5', h=2, H=2)
    node['C1'] = GridNode(name='C1', h=1, H=1)
    node['C2'] = GridNode(name='C2', h=1, H=1)
    node['C3'] = GridNode(name='C3', h=4, H=4)
    node['C4'] = GridNode(name='C4', h=3, H=3)
    node['C5'] = GridNode(name='C5', h=2, H=2)
    node['D1'] = GridNode(name='D1', h=5, H=5)
    node['D2'] = GridNode(name='D2', h=1, H=1)
    node['D3'] = GridNode(name='D3', h=3, H=3)
    node['D4'] = GridNode(name='D4', h=2, H=2)
    node['D5'] = GridNode(name='D5', h=1, H=1)
    node['E1'] = GridNode(name='E1', h=4, H=4)
    node['E2'] = GridNode(name='E2', h=3, H=3)
    node['E3'] = GridNode(name='E3', h=2, H=2)
    node['E4'] = GridNode(name='E4', h=1, H=1)
    node['E5'] = GridNode(name='E5', h=0, H=0)
    node['A1'].neighbours = [node['A2'], node['B1']]
    node['A1'].dist_neighbours = [1, 1]
    node['A2'].neighbours = [node['A1'], node['B2'], node['A3']]
    node['A2'].dist_neighbours = [1, 1, 1]
    node['A3'].neighbours = [node['A2'], node['B3'], node['A4']]
    node['A3'].dist_neighbours = [1, 1, 1]
    node['A4'].neighbours = [node['A3'], node['B4'], node['A5']]
    node['A4'].dist_neighbours = [1, 1, 1]
    node['A5'].neighbours = [node['A4'], node['B5']]
    node['A5'].dist_neighbours = [1, 1]
    node['B1'].neighbours = [node['A1'], node['B2'], node['C1']]
    node['B1'].dist_neighbours = [1, 1, 1]
    node['B2'].neighbours = [node['B1'], node['A2'], node['B3'], node['C2']]
    node['B2'].dist_neighbours = [1, 1, 1, 1]
    node['B3'].neighbours = [node['B2'], node['A3'], node['B4'], node['C3']]
    node['B3'].dist_neighbours = [1, 1, 1, 1]
    node['B4'].neighbours = [node['B3'], node['A4'], node['B5'], node['C4']]
    node['B4'].dist_neighbours = [1, 1, 1, 1]
    node['B5'].neighbours = [node['B4'], node['A5'], node['C5']]
    node['B5'].dist_neighbours = [1, 1, 1]
    node['C1'].neighbours = [node['B1'], node['C2'], node['D1']]
    node['C1'].dist_neighbours = [1, 1, 1]
    node['C2'].neighbours = [node['C1'], node['B2'], node['C3'], node['D2']]
    node['C2'].dist_neighbours = [1, 1, 1, 1]
    node['C3'].neighbours = [node['C2'], node['B3'], node['C4'], node['D3']]
    node['C3'].dist_neighbours = [1, 1, 1, 1]
    node['C4'].neighbours = [node['C3'], node['B4'], node['C5'], node['D4']]
    node['C4'].dist_neighbours = [1, 1, 1, 1]
    node['C5'].neighbours = [node['C4'], node['B5'], node['D5']]
    node['C5'].dist_neighbours = [1, 1, 1]
    node['D1'].neighbours = [node['C1'], node['D2'], node['E1']]
    node['D1'].dist_neighbours = [1, 1, 1]
    node['D2'].neighbours = [node['D1'], node['C2'], node['D3'], node['E2']]
    node['D2'].dist_neighbours = [1, 1, 1, 1]
    node['D3'].neighbours = [node['D2'], node['C3'], node['D4'], node['E3']]
    node['D3'].dist_neighbours = [1, 1, 1, 1]
    node['D4'].neighbours = [node['D3'], node['C4'], node['D5'], node['E4']]
    node['D4'].dist_neighbours = [1, 1, 1, 1]
    node['D5'].neighbours = [node['D4'], node['C5'], node['E5']]
    node['D5'].dist_neighbours = [1, 1, 1]
    node['E1'].neighbours = [node['D1'], node['E2']]
    node['E1'].dist_neighbours = [1, 1]
    node['E2'].neighbours = [node['E1'], node['D2'], node['E3']]
    node['E2'].dist_neighbours = [1, 1, 1]
    node['E3'].neighbours = [node['E2'], node['D3'], node['E4']]
    node['E3'].dist_neighbours = [1, 1, 1]
    node['E4'].neighbours = [node['E3'], node['D4'], node['E5']]
    node['E4'].dist_neighbours = [1, 1, 1]
    node['E5'].neighbours = [node['E4'], node['D5']]
    node['E5'].dist_neighbours = [1, 1]
    return node


######################################################
# Implement LRTA*-COST() at slide 77 here
######################################################
def lrta_cost(previous_state: GridNode, state: GridNode):
    """
    Function computes  the cost estimate of a node using the distance between
    the nodes (previous state and state) and the H table

    Args:
        previous_state: s
        state: s'

    Returns: The cost estimate

    """
    if not previous_state:
        return state.h
    return state.get_distance(previous_state) + state.H


######################################################
# Implement LRTA*-AGENT() at slide 77 here
######################################################
def lrta_agent(state: GridNode = None, previous_state: GridNode = None, goal: GridNode = None):
    """
    Function identifies and returns  the next node to be expanded given the current and previous states
    Args:
        state: s'
        goal: goal state
        previous_state: s

    Returns: The next node to be expanded

    """
    neighbour_costs = [lrta_cost(state, n) for n in state.neighbours]
    min_cost = min(neighbour_costs)
    min_neightbour_idx = neighbour_costs.index(min_cost)

    state.H = min_cost

    return state.neighbours[min_neightbour_idx]


def lrta_graphsearch(start_node: GridNode, goal_node: GridNode):
    """
    Function returns the path and the number of steps taken by the agent from the start node to goal node

    Args:
        start_node:
        goal_node:

    Returns: path: list of names of all the nodes traversed / visited i.e. path taken from 'start_node' to arrive at 'goal_node'
            steps: number of steps taken (nodes visited) from 'start_node' to arrive at 'goal_node'

    """
    steps = 0
    path = [start_node.name]
    previous_state = None
    current_state = start_node
    while (current_state != goal_node):

        result = lrta_agent(current_state, previous_state, goal_node)
        previous_state = current_state
        current_state = result

        steps += 1
        path.append(current_state.name)

    return path, steps


if __name__ == "__main__":
    # driver code for the main algorithm
    nodes = initialize_all_nodes()
    start_node = nodes['A1']
    goal_node = nodes['E5']
    path, steps = lrta_graphsearch(start_node, goal_node)
    print('\nThe path from', start_node.name,
          'to', goal_node.name, 'is:\n', path)
    print('Total number of steps taken:', steps)
