import os
import sys
import pandas
import numpy
import scipy




# Vectors are defined by a class
# These vectors will only have three dimensions
# These vectors will have a specific coordinate system assigned to them


class Vector:
    def __init__(self, system, a1, a2, a3):
        if(system != "cartesian" and system != "spherical" and system != "cylindrical"):
            raise Exception("invalid coordinate system specified")
        self.system = system
        self.x      = a1
        self.y      = a2
        self.z      = a3

    def __str__(self):
        return self.system, self.x, self.y, self.z

    def __add__(self, vec):
        if(self.system != vec.system):
            raise Exception("the basis must be the same when adding vectors")
        if(self.system == "cartesian"):
            return Vector("cartesian", self.x + vec.x, self.y + vec.y, self.z + vec.z)
