from qiskit import QuantumRegister, QuantumCircuit, Aer, execute
from qiskit import ClassicalRegister
from qiskit.tools.visualization import circuit_drawer

# Define backend simulators
M_simulator = Aer.backends(name='qasm_simulator')[0]
S_simulator = Aer.backends(name ='statevector_simulator')[0]

# Define Alice's circuit
alice_circuit = QuantumCircuit(2)
alice_circuit.h(0)
alice_circuit.cx(0, 1)

# Define Bob's circuit
bob_circuit = QuantumCircuit(2)
bob_circuit.z(1)  # Bob wants to send '01'
bob_circuit.x(0)  # Bob wants to send '10'
bob_circuit.z(1)  # Bob wants to send '11'
bob_circuit.x(0)  # Bob wants to send '11'
bob_circuit.cx(0, 1)
bob_circuit.h(0)

# Combine Alice's and Bob's circuits
combined_circuit = alice_circuit.compose(bob_circuit, range(2))

# Execute the combined circuit
S = execute(combined_circuit, S_simulator).result().get_statevector()
print("State vector after Alice and Bob's operations:", S)

# Measure the combined circuit
combined_circuit.measure_all()
M = execute(combined_circuit, M_simulator, shots=100).result().get_counts(combined_circuit)
print("Measurement results after Alice and Bob's operations:", M)

# Draw the combined circuit
print(combined_circuit.draw())
