from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, assemble, Aer,execute
import Our_Qiskit_Functions as oq
import numpy as np
import math as m

S_simulator = Aer.backends(name='statevector_simulator')[0]



q=QuantumRegister(3)
hello=QuantumCircuit(q)
hello.id(q[0])
hello.id(q[1])
hello.id(q[2])

oq.wavefunction(hello)





