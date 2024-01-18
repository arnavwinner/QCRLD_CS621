# P1: Roll Number, second-to-largest 

from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, assemble, Aer,execute
import numpy as np
import math as m

S_simulator = Aer.backends(name='statevector_simulator')[0]


# my roll number = 12140280 , n = 4
q=QuantumRegister(4)
hello=QuantumCircuit(q)
hello.x(q[0])
hello.id(q[1])
hello.id(q[2])
hello.id(q[3])
# assuming q0 as msb and q3 as lsb[q0 q1 q2 q3]

job= execute(hello,S_simulator)
result=job.result()
print(result.get_statevector())