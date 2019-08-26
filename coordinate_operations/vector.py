import os
import sys




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
        to_return = "Coordinate System: " + str(self.system) + "\n x = " + str(self.x) + "\n y = " + str(self.y) + "\n z = " + str(self.z)
        return to_return

    def __add__(self, vec):
        if(self.system != vec.system):
            raise Exception("the basis must be the same when adding vectors")
        if(self.system == "cartesian"):
            return Vector("cartesian", self.x + vec.x, self.y + vec.y, self.z + vec.z)
