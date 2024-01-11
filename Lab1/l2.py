from qiskit import QuantumRegister, QuantumCircuit, Aer, execute

S_simulator = Aer.backends(name='statevector_simulator')[0]

M_simulator = Aer.backends(name='qasm_simulator')[0]

q = QuantumRegister(1)
hello_qubit = QuantumCircuit(q)
hello_qubit.id(q[0])

job = execute(hello_qubit, S_simulator)
result = job.result()
statevector = result.get_statevector()

print('Simulator:', S_simulator, '\n')
print('Simulator Type:', type(S_simulator), '\n')
print('Aer.backends(name=\'statevector_simulator\'):', Aer.backends(name='statevector_simulator'))