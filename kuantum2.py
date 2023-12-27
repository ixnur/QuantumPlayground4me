from qiskit import QuantumCircuit, Aer, transpile, assemble
import matplotlib.pyplot as plt

devre = QuantumCircuit(3, 3)
devre.h(range(3))
devre.ccx(0, 1, 2)
devre.measure(range(3), range(3))

simülatör = Aer.get_backend('aer_simulator')
derlenmiş_devre = transpile(devre, simülatör)
sonuç = simülatör.run(derlenmiş_devre).result()

counts = sonuç.get_counts(devre)
plt.bar(counts.keys(), counts.values())
plt.xlabel('State')
plt.ylabel('Counts')
plt.show()
