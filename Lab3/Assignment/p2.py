from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute

def quantum_coin_flip():
    # Create quantum and classical registers
    q = QuantumRegister(1, name="q")
    c = ClassicalRegister(1, name="c")

    # Create a quantum circuit
    qc = QuantumCircuit(q, c)

    # Apply Hadamard gate to create a superposition
    qc.h(q[0])

    # Measure the qubit
    qc.measure(q, c)

    # Execute the circuit on the simulator
    backend = Aer.get_backend('qasm_simulator')
    result = execute(qc, backend).result()
    counts = result.get_counts()

    # Determine the outcome based on the measurement result
    outcome = int(list(counts.keys())[0])

    return outcome

# Simulate a quantum coin flip
result = quantum_coin_flip()

# Print the outcome (0 or 1)
print("Quantum Coin Flip Outcome:", result)
