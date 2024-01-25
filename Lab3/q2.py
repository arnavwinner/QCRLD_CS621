from qiskit import QuantumRegister, QuantumCircuit, Aer, execute 
from qiskit import ClassicalRegister 
M_simulator = Aer.backends(name = 'qasm_simulator')[0]

q = QuantumRegister(1)
c = ClassicalRegister(1)
qc = QuantumCircuit(q,c) 
qc.h(q[0]) 
qc.measure(q,c) 

M = execute(qc, M_simulator).result().get_counts(qc)
print('Dictionary entry "0" : ',M['0'])
print('Dictionary entry "1" : ',M['1'])