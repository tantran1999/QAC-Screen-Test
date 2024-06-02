import os
from dotenv import load_dotenv

from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService
from qiskit_ibm_runtime import SamplerV2 as Sampler


load_dotenv()

# Create empty circuit
example_circuit = QuantumCircuit(2)
example_circuit.measure_all()

# Create Qiskit runtime service and backend
service = QiskitRuntimeService(
    channel="ibm_quantum",
    token=os.getenv("IBM_QISKIT_TOKEN")
)

print(service.backends())

backend = service.backend(name="ibm_kyoto", instance="ibm-q/open/main")

sampler = Sampler(backend)
job = sampler.run([example_circuit])
print(f"Job ID: {job.job_id}")
result = job.result()
print(result)
