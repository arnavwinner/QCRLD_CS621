#AND GATE USING CCNOT

from qiskit import QuantumRegister, QuantumCircuit, Aer, execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name ='statevector_simulator')[0]

q = QuantumRegister(3)
c = ClassicalRegister(3)
qc = QuantumCircuit(q, c)
qc.h(q[0]) #x = 1
qc.h(q[1]) #y = 1/0
qc.id(q[2]) #z = 0 -- z ^ (x & y)
qc.ccx(q[0], q[1], q[2]) # final value is y
qc.measure(q, c)
print(qc.draw())
M = execute(qc, M_simulator, shots=100).result().get_counts(qc)
print(M)

# print(circuit_drawer(qc))
# S = execute(qc, S_simulator).result().get_statevector()
# print(S)
