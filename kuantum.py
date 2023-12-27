from qiskit import QuantumCircuit, Aer, transpile, assemble
from qiskit.visualization import plot_histogram

oracle_value = '101'
grover_devresi = QuantumCircuit(len(oracle_value) + 1, len(oracle_value))
grover_devresi.h(range(len(oracle_value) + 1))
for qubit in range(len(oracle_value)):
    if oracle_value[qubit] == '1':
        grover_devresi.x(qubit)

grover_devresi.mcx(list(range(len(oracle_value))), len(oracle_value))
for qubit in range(len(oracle_value)):
    if oracle_value[qubit] == '1':
        grover_devresi.x(qubit)

grover_devresi.h(range(len(oracle_value)))
grover_devresi.z(len(oracle_value))
grover_devresi.h(range(len(oracle_value)))
grover_devresi.measure(range(len(oracle_value)), range(len(oracle_value)))
simulator = Aer.get_backend('aer_simulator')
compiled_grover_circuit = transpile(grover_devresi, simulator)
result = simulator.run(compiled_grover_circuit).result()
counts = result.get_counts(grover_devresi)
plot_histogram(counts)
