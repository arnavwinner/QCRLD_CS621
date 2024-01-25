from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute

# Create quantum and classical registers
q = QuantumRegister(3, name="q")
c = ClassicalRegister(3, name="c")

# Create a quantum circuit
qc = QuantumCircuit(q, c)

# Apply operations as described
qc.x(q[0])       # X gate on the first qubit
qc.h(q[1])       # Hadamard gate on the second qubit
qc.id(q[2])       # Identical gate (identity gate) on the third qubit

# Measure the entire quantum system 
qc.measure(q, c) # Here we are measuring the total quantum system

# Execute the circuit and print the state vector
backend = Aer.get_backend('statevector_simulator')
result = execute(qc, backend).result()
statevector = result.get_statevector()
print("State vector (total measurement):", statevector)

# Reset the circuit and measure only the second qubit
qc = QuantumCircuit(q, c)
qc.x(q[0])
qc.h(q[1])
qc.id(q[2])
qc.measure(q[1], c[1]) # Measuring only the second qubit (index 1)

# Execute the circuit and print the state vector
result = execute(qc, backend).result()
statevector = result.get_statevector()
print("State vector (measurement at only one qubit):", statevector)
