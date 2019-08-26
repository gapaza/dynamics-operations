import os
import sys
import math




# Vectors are defined by a class
# These vectors will only have three dimensions
# These vectors will have a specific coordinate system assigned to them
# All angle values are in radians

# Cartesian
# dim1 = x
# dim2 = y
# dim3 = z

# Cylindrical
# dim1 = r
# dim2 = theta
# dim3 = z


class Vector:
    def __init__(self, system, a1, a2, a3):
        if(system != "cartesian" and system != "cylindrical"):
            raise Exception("invalid coordinate system specified")
        self.system        = system
        self.dim1          = a1
        self.dim2          = a2
        self.dim3          = a3
        self.valid_systems = ['cartesian', 'cylindrical']

    def __str__(self):
        to_return = "Coordinate System: " + str(self.system) + "\nx = " + str(self.dim1) + "\ny = " + str(self.dim2) + "\nz = " + str(self.dim3)
        return to_return

    def __add__(self, vec):
        if(self.system != vec.system):
            raise Exception("the basis must be the same when adding vectors")
        if(self.system == "cartesian"):
            return Vector("cartesian", self.dim1 + vec.dim1, self.dim2 + vec.dim2, self.dim3 + vec.dim3)

    def change_system(self, new_system):
        if(self.system == new_system):
            return True
        if(new_system not in self.valid_systems):
            raise Exception('the new coordinate system is not valid')

        if(self.system == 'cartesian'):
            if(new_system == 'cylindrical'):
                r     = sqrt(pow(self.dim1,2) + pow(self.dim2,2))
                theta = atan(self.dim2 / self.dim1)
                z     = self.dim3
                self.dim1 = r
                self.dim2 = theta
                self.dim3 = z
                return True
        if(self.system == 'cylindrical'):
            if(new_system == 'cartesian'):
                x = self.dim1 * cos(self.dim2)
                y = self.dim1 * sin(self.dim2)
                z = z
                self.dim1 = x
                self.dim2 = y
                self.dim3 = z
                return True


        print("No change occurred")
        return False
