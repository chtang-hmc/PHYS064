import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector

class QC(QuantumCircuit):
    def __init__(self, n):
        super().__init__(n)
        
    def x(self, q, error = 0, seed = 0):
        np.random.seed(seed)
        error = np.random.normal(0, error)
        # apply x gate to qubit q
        super().x(q)
        
        # add an error gate that doesn't show up in the circuit diagram
        if error > 0:
            super().u(error, 0, 0, q)
        
        return self
    
    def z(self, q, error = 0, seed = 0):
        np.random.seed(seed)
        error = np.random.normal(0, error)
        # apply z gate to qubit q
        super().z(q)
        
        # add an error gate that doesn't show up in the circuit diagram
        if error > 0:
            super().u(0, 0, error, q)
        
        return self
    
    def h(self, q, error = 0, seed = 0):
        np.random.seed(seed)
        error = np.random.normal(0, error)
        # apply h gate to qubit q
        super().h(q)
        
        # add an error gate that doesn't show up in the circuit diagram
        if error > 0:
            super().u(error, error, error, q)
        
        return self
    
    def get_state(self):
        '''
        Get the statevector of the quantum circuit
        '''
        return Statevector.from_instruction(self).data

    def get_amplitudes(self):
        '''
        Get the amplitudes of the quantum circuit
        '''
        return np.abs(get_state(self))**2

    def states(self):
        '''
        Get the statevector of the quantum circuit as a dictionary
        '''
        # get a list of basis states
        n = self.num_qubits
        states = [format(i, '0'+str(n)+'b') for i in range(2**n)]
        # make states-statevector dictionary
        sv = np.round(get_state(self), 3)
        states_dict = dict(zip(states, sv))
        return states_dict