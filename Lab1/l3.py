from qiskit import QuantumRegister, QuantumCircuit, Aer, execute

S_simulator = Aer.backends(name="statevector_simulator")[0]
q = QuantumRegister(1)
hello_qubit = QuantumCircuit(q)
hello_qubit.id(q[0])
job = execute(hello_qubit, S_simulator)
result = job.result()
result.get_statevector()

job = execute(hello_qubit, S_simulator)
print("Job = AerJob class: ", type(job))
result = job.result()
print("result = Result Class: ", type(result))

