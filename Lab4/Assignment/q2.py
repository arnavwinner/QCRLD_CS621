from qiskit import QuantumRegister, QuantumCircuit, Aer, execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name ='statevector_simulator')[0]

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)
qc.h(q[0])
qc.x(q[1])
qc.measure(q, c)
print(qc.draw())
M = execute(qc, M_simulator, shots=100).result().get_counts(qc)
print("Before cNot")
print(M)
qc.cx(q[0], q[1])
qc.measure(q, c)
print(qc.draw())
M = execute(qc, M_simulator, shots=100).result().get_counts(qc)
print("After 1 cNot")
print(M)
qc.cx(q[0], q[1])
qc.measure(q, c)
print(qc.draw())
M = execute(qc, M_simulator, shots=100).result().get_counts(qc)
print("After 2 cNot")
print(M)


# print(circuit_drawer(qc))
# S = execute(qc, S_simulator).result().get_statevector()
# print(S)
