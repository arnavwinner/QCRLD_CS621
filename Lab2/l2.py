# Creating a Mutli-Qubit State

# Creating |010> ket

from qiskit import QuantumRegister, QuantumCircuit, Aer, execute

q = QuantumRegister(3)
three_qubits = QuantumCircuit(q)
three_qubits.id(q[0])
three_qubits.x(q[1])
three_qubits.x(q[2])

backend = Aer.get_backend('statevector_simulator')  # Use 'statevector_simulator' for statevector simulation
job = execute(three_qubits, backend)
result = job.result()
statevector = result.get_statevector()

print(statevector)
