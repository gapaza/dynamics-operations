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
