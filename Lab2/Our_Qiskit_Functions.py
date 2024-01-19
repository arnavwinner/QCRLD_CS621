from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, assemble, Aer,execute

def wavefunction(h):
    S_simulator = Aer.backends(name='statevector_simulator')[0]
    job = execute(h, S_simulator)
    result = job.result()
    statevector = result.get_statevector()

    for index, coefficient in enumerate(statevector):
        if coefficient != 0:
            binary_string = bin(index)[2:]
            reversed_string = binary_string[::-1]
            print(f"coefficients: {coefficient} |{reversed_string})")