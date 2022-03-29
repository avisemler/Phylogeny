import functools
from pandas import *
import numpy as np

class Clade:
    def __init__(self, data = None, name = None):
        self.data = data
        self.name = None
        self.children = []

    def add_child(self, clade):
        self.children.append(clade)

    def string(self, indent):
        result = str(self.data)
        for c in self.children:
            result += "\n" + " "* indent + "|" + "_ " + c.string(indent + 4)
        return result

    def __str__(self):
        return self.string(indent = 1).replace("None", "Node")

class Phylogeny:
    
    def __init__(self, distance_function):
        #function that returns a number indicating how different the
        #data on two nodes are
        self.distance_function = distance_function

        self.tree = Clade()

    def construct(self, data_list):
        clades = []

        #initialise clades just consisting of each data point
        for d in data_list:
            tree = Clade(d)
            clades.append(tree)
        size = len(clades)
        while size > 3:
            size = len(clades)

            #find best matching pair of nodes
            least_distance = self.get_distance(clades[0], clades[1])
            coordinates = (0, 1)
            for x in range(size):
                for y in range(size):
                    distance = self.get_distance(clades[x], clades[y])
                    if x != y and distance < least_distance:
                        least_distance = distance
                        coordinates = (x, y)
            x, y = coordinates
            print(clades[x], clades[y], least_distance)
            #form a new clade from the closest two clades
            new_clade = Clade()
            new_clade.add_child(clades[x])
            new_clade.add_child(clades[y])

            temp = clades[y]
            clades.remove(clades[x])
            clades.remove(temp)
            clades.append(new_clade)

        print(clades)
        self.tree.add_child(clades[0])
        self.tree.add_child(clades[1])
        print(self.tree)

    @functools.cache
    def get_distance(self, clade1:Clade, clade2:Clade):
        children1 = clade1.children
        children2 = clade2.children
        if children1 != [] and children2 == []:
            #we only want to explicitly handle the case where first one is 
            #data and the second a clade
            return self.get_distance(clade2, clade1)
        elif children1 == [] and children2 != []:
            #return the arithmetic mean of the differences from node1 from each 
            #member of the clade
            return sum(map(lambda x: self.get_distance(x, clade1), children2)) / len(children2)
        elif children1 != [] and children2 != []:
            #both represent clades
            #calculate the convolution
            count = 0
            total = 0
            for child1 in children1:
                for child2 in children1:
                    total += self.get_distance(child1, child2)
                    count += 1
            return total / count
        else:
            #both represent data, not clades
            return self.distance_function(clade1.data, clade2.data)

import random

tree = Phylogeny(lambda x, y: abs(y - x))
tree.construct([625, 390, 400, 410, 605])
