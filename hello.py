from qibo.models import QFT

# Create a QFT circuit with 15 qubits
circuit = QFT(15)

# Simulate final state wavefunction default initial state is |00>
final_state = circuit()

import numpy as np
from qibo import Circuit, gates

circuit = Circuit(2)
circuit.add(gates.X(0))

# Add a measurement register on both qubits
circuit.add(gates.M(0, 1))

# Execute the circuit with the default initial state |00>.
result = circuit(nshots=100)