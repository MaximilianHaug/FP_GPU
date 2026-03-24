from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit

bits = 4
qreg_q = QuantumRegister(bits + 1, "q")
creg_c = ClassicalRegister(bits, "c")
circuit = QuantumCircuit(qreg_q, creg_c)


circuit.h(qreg_q[0])
circuit.cx(qreg_q[0], qreg_q[1])
circuit.cx(qreg_q[1], qreg_q[2])
circuit.cx(qreg_q[2], qreg_q[3])


circuit.measure(range(bits), range(bits))

circuit.draw(output="mpl", idle_wires=False, style="iqp")
