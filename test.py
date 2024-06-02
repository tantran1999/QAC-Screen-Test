import numpy as np
from qiskit import QuantumCircuit
from qiskit.primitives.sampler import Sampler


qc = QuantumCircuit(3)
qc.h(0)
qc.p(np.pi/2, 0)
qc.cx(0, 1)
qc.cx(0, 2)

qc.draw("mpl", filename="test.png")

qc_measured = qc.measure_all(inplace=False)

sampler = Sampler()
job = sampler.run(qc_measured, shots=1000)
result = job.result()
print(f" > Quasi probability distribution: {result.quasi_dists}")