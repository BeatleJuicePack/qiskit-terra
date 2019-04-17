# -*- coding: utf-8 -*-

# Copyright 2017, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

""""
Quantum Instantaneous Polynomial Time example

Note: if you have only cloned the Qiskit repository but not
used `pip install`, the examples only work from the root directory.
""""
###############################################################
# Import qiskikt dependencies
###############################################################
from qiskit import *

from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import CommutationAnalysis, CommutationTransformation
from qiskit.transpiler import transpile

###############################################################
# Assign values and build a circuit
###############################################################
qr = QuantumRegister(5, 'qr')
circuit = QuantumCircuit(qr)

###############################################################
# Quantum Instantaneous Polynomial Time example
###############################################################
circuit.cx(qr[0], qr[1])
circuit.cx(qr[2], qr[1])
circuit.cx(qr[4], qr[3])
circuit.cx(qr[2], qr[3]) 
circuit.z(qr[0])
circuit.z(qr[4])
circuit.cx(qr[0], qr[1])
circuit.cx(qr[2], qr[1])
circuit.cx(qr[4], qr[3])
circuit.cx(qr[2], qr[3]) 
circuit.cx(qr[3], qr[2]) 

print(circuit.draw())

pm = PassManager()

pm.append([CommutationAnalysis(), CommutationTransformation()])

###############################################################
# TODO make it not needed to have a backend 
###############################################################
backend_device = BasicAer.get_backend('qasm_simulator')
circuit = transpile(circuit, backend_device, pass_manager=pm)
print(circuit.draw())
