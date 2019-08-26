import math
from vector import *








# Basis_1 is a list of three unit vectors making up basis 1
# Basis_2 is a list of three unit vectors making up basis 2
def direction_cosine_matrix(basis_1, basis_2):
    for vec in (basis_1 + basis_2):
        if(vec.magnitude != 1):
            raise Exception("all the basis vectors must be unit vectors")
