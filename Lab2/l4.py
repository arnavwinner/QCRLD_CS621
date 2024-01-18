# P3: Hadamard 2-Qubit Superposition state

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, assemble, Aer,execute
import numpy as np
import math as m

S_simulator = Aer.backends(name='statevector_simulator')[0]


q=QuantumRegister(2)
hello=QuantumCircuit(q)
hello.h(q[0])
hello.h(q[1])
# assuming q0 as msb and q3 as lsb[q0 q1 q2 q3]

job= execute(hello,S_simulator)
result=job.result()
print(result.get_statevector())