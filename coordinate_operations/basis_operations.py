import math








# Basis_a is a list of three unit vectors making up basis a
# Basis_b is a list of three unit vectors making up basis b
def find_direction_cosine_matrix(basis_a, basis_b):
    for vec in (basis_a + basis_b):
        if(vec.magnitude != 1):
            raise Exception("all the basis vectors must be unit vectors")

    # Recall, basis vectors are unit vectors - so their magnitude is 1
    # Theta is the angle between the two vectors
    # b dot a = |b||a|cos(theta)
    # b dot a = cos(theta)
    direction_cosine_matrix = []
    for vec_b in basis_b:
        row = []
        for vec_a in basis_a:
            row.append(vec_b.dot(vec_a))
        direction_cosine_matrix.append(row)
    return direction_cosine_matrix



# Prints a 3x3 array
def print_direction_cosine_matrix(mtrx):
    for row in mtrx:
        print('|' + str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + '|')
