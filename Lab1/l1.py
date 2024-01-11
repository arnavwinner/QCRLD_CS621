from qiskit import QuantumRegister, QuantumCircuit, Aer, execute

q = QuantumRegister(1)
hello = QuantumCircuit(q)
hello.id(q[0])

backend = Aer.get_backend('statevector_simulator')  # Use 'statevector_simulator' for statevector simulation
job = execute(hello, backend)
result = job.result()
statevector = result.get_statevector()

print(statevector)
