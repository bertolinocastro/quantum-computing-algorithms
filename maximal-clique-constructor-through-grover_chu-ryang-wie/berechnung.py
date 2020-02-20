from sympy import *
#import sympy.physics.quantum as qp # quantum physics
from sympy.physics.quantum.qubit import *

# base network G:
# 1 <-> 2 <-> 3
# Nodes: 1, 2, 3
# Edges: (1,2), (2,3)

# Adjacency matrix for network G
A = Matrix([
	[0, 1, 0],
	[1, 0, 1],
	[0, 1, 0]
])


# creating qubits for n=3 basis
q = [Qubit(f'{dummy:03b}') for dummy in range(2**3)]
pprint(q)

# step: constructing the U operator basics using a network with n=3
# function to represent qubit as matrix: qubit_to_matrix()

