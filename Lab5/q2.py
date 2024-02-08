from qiskit import QuantumRegister, QuantumCircuit, Aer, execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer
M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name ='statevector_simulator')[0]

q = QuantumRegister(2)
c = ClassicalRegister(2)
qc = QuantumCircuit(q, c)

for i in range(0, 2): # q[0] 
	for j in range(0, 2): # q[1]

		# this is our assumpted CNOT where Control and Target bits are flipped
		if i == 1:
			# means that we apply 1
			qc.x(q[0])
			# else apply 0

		if j == 1:
			# apply 1
			qc.x(q[1])
			# else apply 0
		qc.h(q[0])
		qc.h(q[1])
		qc.cx(q[0], q[1])
		qc.h(q[0])
		qc.h(q[1])
		S = execute(qc, S_simulator).result().get_statevector()
		print(S)
		qc.measure(q, c)
		M = execute(qc, M_simulator, shots=100).result().get_counts(qc)
		print(M)
		print(qc.draw())
		qc.reset(q)
		print("--------------------------------------------------------------------------------------------------\n")

# I want to reset my qc here

# S = execute(qc, S_simulator).result().get_statevector()
# print(S)
# qc.measure(q, c)
# M = execute(qc, M_simulator, shots=100).result().get_counts(qc)
# print(M)
# # S = execute(qc, S_simulator).result().get_statevector()
# # print(S)
# print(qc.draw())
# qc.reset(q)
# print(qc.draw())

# print(circuit_drawer(qc))
# S = execute(qc, S_simulator).result().get_statevector()
# print(S)
