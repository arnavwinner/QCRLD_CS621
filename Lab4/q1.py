from qiskit import QuantumRegister, QuantumCircuit, Aer, execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
M_simulator = Aer.backends(name='qasm_simulator')[0]
# S_simulator = Aer.backends(name ='statevector_simulator')[0]

q = QuantumRegister(2, name='q')
c = ClassicalRegister(2, name='c')
qc = QuantumCircuit(q, c, name='qc')
qc.h(q[0])
qc.h(q[1])
qc.measure(q, c)


print(circuit_drawer(qc))
# S = execute(qc, S_simulator).result().get_statevector()
# print(S)
