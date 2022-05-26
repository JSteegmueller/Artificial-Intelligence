import copy
import sys
from typing import List


class DefineCity:
    def __init__(self, location, name, neighbours=[], dist_neighbours=[], parent=None, f=10000, sum_g=0):
        self.neighbours = neighbours
        self.location = location
        self.dist_neighbours = dist_neighbours
        self.parent = parent
        self.name = name
        self.f = f
        self.sum_g = sum_g
        assert len(self.dist_neighbours) == len(self.neighbours)

    def g(self, city):
        idx = self.neighbours.index(city)
        dist = self.dist_neighbours[idx]
        return dist

    def h(self, city2):
        l1 = self.location
        l2 = city2.location
        dist = int(((l1[0] - l2[0]) ** 2 + (l1[1] - l2[1]) ** 2) ** 0.5)
        return dist


def initialize_all_cities():
    city = {}
    city['Aachen'] = DefineCity(
        location=[-209.60379, 249.47157], name='Aachen')
    city['Augsburg'] = DefineCity(
        location=[134.80635, -18.575178], name='Augsburg')
    city['Bayreuth'] = DefineCity(
        location=[179.32399, 157.053], name='Bayreuth')
    city['Berlin'] = DefineCity(location=[293.09943, 442.5178], name='Berlin')
    city['Bremen'] = DefineCity(
        location=[-16.931591, 504.64734], name='Bremen')
    city['Cottbus'] = DefineCity(
        location=[361.43076, 358.53146], name='Cottbus')
    city['Chemnitz'] = DefineCity(
        location=[269.5081, 254.68588], name='Chemnitz')
    city['Dresden'] = DefineCity(
        location=[325.56674, 279.0941], name='Dresden')
    city['Erfurt'] = DefineCity(location=[136.25624, 271.9933], name='Erfurt')
    city['Essen'] = DefineCity(location=[-141.96866, 325.35834], name='Essen')
    city['Frankfurt/Main'] = DefineCity(location=[-27.608,
                                        175.58119], name='Frankfurt/Main')
    city['Frankfurt/Oder'] = DefineCity(location=[371.03522,
                                        422.43652], name='Frankfurt/Oder')
    city['Freiburg'] = DefineCity(
        location=[-90.64952, -59.292046], name='Freiburg')
    city['Fulda'] = DefineCity(location=[43.13819, 223.62091], name='Fulda')
    city['Garmisch-Part.'] = DefineCity(
        location=[152.07657, -114.76524], name='Garmisch-Part.')
    city['Hamburg'] = DefineCity(
        location=[63.380383, 558.3458], name='Hamburg')
    city['Hannover'] = DefineCity(
        location=[44.825264, 426.9851], name='Hannover')
    city['Karlsruhe'] = DefineCity(
        location=[-48.82897, 53.54009], name='Karlsruhe')
    city['Kassel'] = DefineCity(location=[29.742897, 308.71664], name='Kassel')
    city['Kiel'] = DefineCity(location=[68.695816, 643.33014], name='Kiel')
    city['Koblenz'] = DefineCity(
        location=[-104.14378, 201.43147], name='Koblenz')
    city['Koeln'] = DefineCity(location=[-148.25447, 267.99976], name='Koeln')
    city['Leipzig'] = DefineCity(
        location=[229.1317, 311.15707], name='Leipzig')
    city['Lindau'] = DefineCity(
        location=[45.822735, -109.21826], name='Lindau')
    city['Magdeburg'] = DefineCity(
        location=[173.56235, 398.0283], name='Magdeburg')
    city['Mannheim'] = DefineCity(
        location=[-43.54089, 105.24141], name='Mannheim')
    city['Muenchen'] = DefineCity(
        location=[184.8133, -44.536476], name='Muenchen')
    city['Muenster'] = DefineCity(
        location=[-98.30054, 380.8315], name='Muenster')
    city['Neubrandenburg'] = DefineCity(
        location=[276.2144, 557.0144], name='Neubrandenburg')
    city['Nuernberg'] = DefineCity(
        location=[145.11511, 101.5798], name='Nuernberg')
    city['Osnabrueck'] = DefineCity(
        location=[-69.30297, 415.89078], name='Osnabrueck')
    city['Passau'] = DefineCity(location=[322.74014, 3.6142504], name='Passau')
    city['Regensburg'] = DefineCity(
        location=[220.39214, 53.54009], name='Regensburg')
    city['Rostock'] = DefineCity(
        location=[198.72835, 616.2598], name='Rostock')
    city['Saarbruecken'] = DefineCity(
        location=[-150.04137, 77.505005], name='Saarbruecken')
    city['Schwerin'] = DefineCity(
        location=[154.01888, 565.11285], name='Schwerin')
    city['Stuttgart'] = DefineCity(
        location=[8.18225, 27.57841], name='Stuttgart')
    city['Trier'] = DefineCity(location=[-173.55475, 134.86357], name='Trier')
    city['Ulm'] = DefineCity(location=[67.17258, -14.913567], name='Ulm')
    city['Wilhelmshaven'] = DefineCity(
        location=[-62.93731, 552.79846], name='Wilhelmshaven')
    city['Wuerzburg'] = DefineCity(
        location=[61.723507, 140.4113], name='Wuerzburg')

    city['Aachen'].neighbours = [city['Essen'], city['Koblenz'], city['Koeln']]
    city['Aachen'].dist_neighbours = [123, 145, 65]
    city['Augsburg'].neighbours = [city['Garmisch-Part.'],
                                   city['Muenchen'], city['Stuttgart'], city['Ulm']]
    city['Augsburg'].dist_neighbours = [117, 81, 149, 83]
    city['Bayreuth'].neighbours = [city['Nuernberg'], city['Wuerzburg']]
    city['Bayreuth'].dist_neighbours = [74, 147]
    city['Berlin'].neighbours = [city['Cottbus'], city['Frankfurt/Oder'],
                                 city['Magdeburg'], city['Neubrandenburg']]
    city['Berlin'].dist_neighbours = [125, 91, 131, 130]
    city['Bremen'].neighbours = [city['Hamburg'], city['Hannover'],
                                 city['Osnabrueck'], city['Wilhelmshaven']]
    city['Bremen'].dist_neighbours = [110, 118, 120, 110]
    city['Cottbus'].neighbours = [city['Berlin'],
                                  city['Dresden'], city['Frankfurt/Oder']]
    city['Cottbus'].dist_neighbours = [125, 138, 119]
    city['Chemnitz'].neighbours = [city['Erfurt'], city['Leipzig']]
    city['Chemnitz'].dist_neighbours = [160, 90]
    city['Dresden'].neighbours = [city['Cottbus'], city['Leipzig']]
    city['Dresden'].dist_neighbours = [138, 140]
    city['Erfurt'].neighbours = [city['Kassel'], city['Chemnitz']]
    city['Erfurt'].dist_neighbours = [135, 160]
    city['Essen'].neighbours = [city['Aachen'],
                                city['Koeln'], city['Muenster'], city['Osnabrueck']]
    city['Essen'].dist_neighbours = [123, 75, 87, 135]
    city['Frankfurt/Main'].neighbours = [city['Fulda'], city['Karlsruhe'], city['Koblenz'], city['Mannheim'],
                                         city['Wuerzburg']]
    city['Frankfurt/Main'].dist_neighbours = [95, 135, 125, 106, 130]
    city['Frankfurt/Oder'].neighbours = [city['Berlin'], city['Cottbus']]
    city['Frankfurt/Oder'].dist_neighbours = [91, 119]
    city['Freiburg'].neighbours = [city['Karlsruhe']]
    city['Freiburg'].dist_neighbours = [130]
    city['Fulda'].neighbours = [city['Frankfurt/Main'],
                                city['Kassel'], city['Wuerzburg']]
    city['Fulda'].dist_neighbours = [95, 105, 100]
    city['Garmisch-Part.'].neighbours = [city['Augsburg'], city['Muenchen']]
    city['Garmisch-Part.'].dist_neighbours = [117, 89]
    city['Hamburg'].neighbours = [city['Bremen'],
                                  city['Kiel'], city['Rostock'], city['Schwerin']]
    city['Hamburg'].dist_neighbours = [110, 90, 150, 120]
    city['Hannover'].neighbours = [city['Bremen'],
                                   city['Magdeburg'], city['Osnabrueck']]
    city['Hannover'].dist_neighbours = [118, 136, 135]
    city['Karlsruhe'].neighbours = [city['Frankfurt/Main'],
                                    city['Freiburg'], city['Mannheim'], city['Stuttgart']]
    city['Karlsruhe'].dist_neighbours = [135, 130, 58, 81]
    city['Kassel'].neighbours = [city['Erfurt'], city['Fulda']]
    city['Kassel'].dist_neighbours = [135, 105]
    city['Kiel'].neighbours = [city['Hamburg'], city['Schwerin']]
    city['Kiel'].dist_neighbours = [90, 139]
    city['Koblenz'].neighbours = [city['Aachen'], city['Frankfurt/Main'], city['Koeln'], city['Mannheim'],
                                  city['Trier']]
    city['Koblenz'].dist_neighbours = [145, 125, 110, 145, 128]
    city['Koeln'].neighbours = [city['Aachen'],
                                city['Essen'], city['Koblenz'], city['Muenster']]
    city['Koeln'].dist_neighbours = [65, 75, 110, 144]
    city['Leipzig'].neighbours = [city['Dresden'],
                                  city['Magdeburg'], city['Chemnitz']]
    city['Leipzig'].dist_neighbours = [140, 108, 90]
    city['Lindau'].neighbours = [city['Ulm']]
    city['Lindau'].dist_neighbours = [126]
    city['Magdeburg'].neighbours = [
        city['Berlin'], city['Hannover'], city['Leipzig']]
    city['Magdeburg'].dist_neighbours = [131, 136, 108]
    city['Mannheim'].neighbours = [city['Frankfurt/Main'], city['Karlsruhe'], city['Koblenz'], city['Saarbruecken'],
                                   city['Stuttgart'], city['Trier']]
    city['Mannheim'].dist_neighbours = [106, 58, 145, 117, 138, 146]
    city['Muenchen'].neighbours = [city['Augsburg'],
                                   city['Garmisch-Part.'], city['Regensburg'], city['Ulm']]
    city['Muenchen'].dist_neighbours = [81, 89, 106, 124]
    city['Muenster'].neighbours = [
        city['Essen'], city['Koeln'], city['Osnabrueck']]
    city['Muenster'].dist_neighbours = [87, 144, 60]
    city['Neubrandenburg'].neighbours = [city['Berlin'], city['Rostock']]
    city['Neubrandenburg'].dist_neighbours = [130, 103]
    city['Nuernberg'].neighbours = [city['Bayreuth'],
                                    city['Regensburg'], city['Wuerzburg']]
    city['Nuernberg'].dist_neighbours = [74, 105, 108]
    city['Osnabrueck'].neighbours = [city['Bremen'],
                                     city['Essen'], city['Hannover'], city['Muenster']]
    city['Osnabrueck'].dist_neighbours = [120, 135, 135, 60]
    city['Passau'].neighbours = [city['Regensburg']]
    city['Passau'].dist_neighbours = [128]
    city['Regensburg'].neighbours = [
        city['Muenchen'], city['Nuernberg'], city['Passau']]
    city['Regensburg'].dist_neighbours = [106, 105, 128]
    city['Rostock'].neighbours = [city['Hamburg'],
                                  city['Neubrandenburg'], city['Schwerin']]
    city['Rostock'].dist_neighbours = [150, 103, 90]
    city['Saarbruecken'].neighbours = [city['Mannheim'], city['Trier']]
    city['Saarbruecken'].dist_neighbours = [117, 103]
    city['Schwerin'].neighbours = [
        city['Hamburg'], city['Kiel'], city['Rostock']]
    city['Schwerin'].dist_neighbours = [120, 139, 90]
    city['Stuttgart'].neighbours = [city['Augsburg'],
                                    city['Karlsruhe'], city['Mannheim'], city['Ulm']]
    city['Stuttgart'].dist_neighbours = [149, 81, 138, 100]
    city['Trier'].neighbours = [city['Koblenz'],
                                city['Mannheim'], city['Saarbruecken']]
    city['Trier'].dist_neighbours = [128, 146, 103]
    city['Ulm'].neighbours = [city['Augsburg'],
                              city['Lindau'], city['Muenchen'], city['Stuttgart']]
    city['Ulm'].dist_neighbours = [83, 126, 124, 100]
    city['Wilhelmshaven'].neighbours = [city['Bremen']]
    city['Wilhelmshaven'].dist_neighbours = [110]
    city['Wuerzburg'].neighbours = [city['Bayreuth'],
                                    city['Frankfurt/Main'], city['Fulda'], city['Nuernberg']]
    city['Wuerzburg'].dist_neighbours = [147, 130, 100, 108]
    return city


cities = initialize_all_cities()

max_city = DefineCity(location=[-209.60379, 249.47157], name='Aachen')
max_city.f = sys.maxsize


def rbfs(start: DefineCity, goal: DefineCity, f_limit: int, count=0):
    """This function should follow the algorithm shown in Figure 3.26 in the book.
        input arguments:
            start: The initial city object of DefineCity class. The city from where rbfs should start its search.
            goal: The goal city object of DefineCity class. The city at which rbfs should end its search.
            f_limit (float): The f limit in RBFS algorithm.
            count (int): The integer which counts the total number of times the algorithm expands nodes. Default=0
        output arguments:
            result (bool): True if algorithm successfully finds the goal, False otherwise
            final_city: The last city (goal city) expanded. Needed for finding the optimal path
            count (int): The integer which counts the total number of times the algorithm expands nodes.
    """
    # Note: This function should follow the algorithm shown in Figure 3.26 in the book.
    #       You are allowed to change the input arguments if you like to do so.

    # TODO: Goal test here
    if start.name == goal.name:
        return True, start, count

    # TODO: Add all possible neighbours of the current city here in successors list
    #  - Use copy.copy() to add new nodes
    #  - Update the f cost and parent in each successor object
    successors: List[DefineCity] = []
    for idx, successor in enumerate(start.neighbours):
        successor.sum_g = start.sum_g + start.g(successor)
        successor.f = max(successor.sum_g + successor.h(goal), start.f)
        successors.append(copy.copy(successor))
        successors[idx].parent = start

    # TODO: Check if there are no successors
    if len(successors) == 0:
        return False, max_city, count
    # TODO: Run the loop here. In the loop you should
    #  - Choose the next city to be expanded (Lowest f-cost city in successors)
    #  - Check if the minimum f cost exceeds the f limit
    #  - Find the second best (alternative) cost
    #  - Recursively call this function with the selected successor and new f limit
    #  - Stop this function if goal is found
    count += 1
    while True:
        successors.sort(key=lambda city: city.f)
        best = successors[0]
        if best.f > f_limit:
            return False, best, count
        alternative = successors[1] if len(successors) > 1 else max_city
        result, node, count = rbfs(
            best, goal, min(f_limit, alternative.f), count)
        best.f = node.f
        if result:
            return True, node, count


def graphsearch_rbfs(start_name, goal_name):
    current_city: DefineCity = cities[start_name]
    goal_city: DefineCity = cities[goal_name]
    current_city.sum_g = 0
    current_city.f = current_city.h(goal_city)
    # TODO: call rbfs and unroll the returned cities here:
    result, final_city, count = rbfs(current_city, goal_city, sys.maxsize, 0)
    reverse: DefineCity = final_city
    path = []
    while reverse:
        path.append(reverse.name)
        reverse = reverse.parent
    # Note: The path list is in the order from goal to start.
    # Therefore, when returning or printing the path we reverse its order
    # Leave the print statements as they are as the serve for automated testing.
    print(start_name, '-->', goal_name)
    print('Number of cities Visited:', count)
    print('Path:', path[::-1])

    return path[::-1], count


print('\n----------------- RBFS ---------------------')
path, num_visited_cities = graphsearch_rbfs('Hamburg', 'Muenchen')
path, num_visited_cities = graphsearch_rbfs('Stuttgart', 'Essen')
path, num_visited_cities = graphsearch_rbfs('Rostock', 'Lindau')
path, num_visited_cities = graphsearch_rbfs('Muenchen', 'Berlin')
