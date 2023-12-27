from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram

def grover_search(oracle, n):
    # Kuantum devresi oluştur
    grover_circuit = QuantumCircuit(n + 1, n)
    
    # Hadamard kapısı uygula
    grover_circuit.h(range(n + 1))
    
    # Grover iterasyonları
    iterations = 1  # İterasyon sayısını isteğe bağlı olarak ayarlayabilirsin
    for _ in range(iterations):
        grover_circuit += oracle
        grover_circuit.h(range(n + 1))
        grover_circuit.x(range(n + 1))
        grover_circuit.h(n)
        grover_circuit.mct(list(range(n)), n)
        grover_circuit.h(n)
        grover_circuit.x(range(n + 1))
        grover_circuit.h(range(n + 1))

    grover_circuit.measure(range(n), range(n))

    return grover_circuit

# Orakül devresini tanımla (örneğin, hedef durumu belirleyen bir durum)
oracle_circuit = QuantumCircuit(3)
oracle_circuit.x(2)
oracle_circuit.cz(0, 2)
oracle_circuit.x(2)

# Grover devresini oluştur
grover_circuit = grover_search(oracle_circuit, 2)

# Simülasyon için Aer backend kullan
simulator = Aer.get_backend('qasm_simulator')
compiled_grover_circuit = transpile(grover_circuit, simulator)
job = execute(compiled_grover_circuit, simulator, shots=1024)
result = job.result()

# Sonuçları görselleştir
counts = result.get_counts(compiled_grover_circuit)
print("Simülasyon Sonuçları:")
print(counts)

# Ölçüm sonuçlarını histogram olarak göster
plot_histogram(counts)