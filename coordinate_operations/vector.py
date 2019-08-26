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
        if(system == 'cartesian'):
            self.magnitude = sqrt(pow(a1,2) + pow(a2,2) + pow(a3,2))
        elif(system == 'cylindrical'):
            self.magnitude = sqrt(pow(a1,2) + pow(a3,2))

        self.valid_systems = ['cartesian', 'cylindrical']

    def __str__(self):
        to_return = "Coordinate System: " + str(self.system) + "\nx = " + str(self.dim1) + "\ny = " + str(self.dim2) + "\nz = " + str(self.dim3)
        return to_return


    # Adds two Vectors
    # Supports: cartesian, cylindrical
    def __add__(self, vec):
        if(self.system != vec.system):
            raise Exception("the basis must be the same when adding vectors")
        elif(self.system == "cartesian"):
            return Vector("cartesian", self.dim1 + vec.dim1, self.dim2 + vec.dim2, self.dim3 + vec.dim3)
        elif(self.system == 'cylindrical'):
            cart1 = self.change_system('cartesian')
            cart2 = vec.change_system('cartesian')
            vadd = Vector('cartesian',cart1.dim1 + cart2.dim1, cart1.dim2 + cart2.dim2, cart1.dim3 + cart2.dim3)
            return vadd.change_system('cylindrical')




    # A dot B is equal to the magnitude of A times the magnitude of B projected onto A
    # a dot b = |a| |b| cos(theta) --> where |b| cos(theta) is the magnitude of B projected on to A
    def dot(self, vec):
        if(self.system == 'cartesian' and vec.system == 'cartesian'):
            return ((self.dim1 * vec.dim1) + (self.dim2 * vec.dim2) + (self.dim3 * vec.dim3))
        else(self.system == 'cylindrical' and vec.system == 'cylindrical'):
            cart1 = self.change_system('cartesian')
            cart2 = vec.change_system('cartesian')
            return cart1.dot(cart2)

        return False



    # Changes the coordinate system of the vector
    # Supports: cartesian, cylindrical
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
                return Vector('cylindrical',r,theta,z)
        if(self.system == 'cylindrical'):
            if(new_system == 'cartesian'):
                x = self.dim1 * cos(self.dim2)
                y = self.dim1 * sin(self.dim2)
                z = z
                return Vector('cartesian',x,y,z)
        print("No change occurred")
        return False
