from qiskit import QuantumRegister, QuantumCircuit, Aer, execute 
from qiskit import ClassicalRegister 
M_simulator = Aer.backends(name = 'qasm_simulator')[0]
S_simulator = Aer.backends(name ='statevector_simulator')[0]

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c) 

qc.h(q[0])

qc.h(q[1])
qc.measure(q,c) 
S = execute(qc, S_simulator).result().get_statevector()
print(S)
#M = execute(qc, M_simulator).result().get_counts(qc)
#print(M)
