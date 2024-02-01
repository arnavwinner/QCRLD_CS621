from qiskit import QuantumRegister, QuantumCircuit, Aer, execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name ='statevector_simulator')[0]

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

qc.h(q[0])
qc.id(q[1])

S = execute(qc, S_simulator).result().get_statevector()
print(S)

qc.cx(q[0], q[1])

S = execute(qc, S_simulator).result().get_statevector()
print(S)
print("------------------------------------------")
qc.measure(q, c)

M = execute(qc, M_simulator, shots=100).result().get_counts(qc)
print("After Measurement: ", M)
print(qc.draw())


# print(circuit_drawer(qc))
# S = execute(qc, S_simulator).result().get_statevector()
# print(S)
