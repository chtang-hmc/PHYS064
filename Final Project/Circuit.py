import numpy as np
import scipy as sp

class Gate:
    def __init__(self, n, fidelity = 1,)

class QC:
    def __init__(self, n):
        self.n = n
        self.dm = np.zeros((2**n, 2**n), dtype = complex)
        self.dm[0, 0] = 1
        
    ### gates ###
    
    def x(self, q, error = 0, seed = 0):
        np.random.seed(seed)
        error = np.random.normal(0, error)
        # apply x gate to qubit q
        self.dm = np.dot(np.dot(np.kron(np.eye(2**q), np.array([[0, 1], [1, 0]])), self.dm))
        
        # add an error gate that doesn't show up in the circuit diagram
        if error > 0:
            self.dm = np.dot(np.dot(np.kron(np.eye(2**q), sp.linalg.expm(1j*error*np.array([[0, 1], [1, 0]]))), self.dm)
        
        return self
        
    def u3(self, q, theta, phi, lam, error = 0, seed = 0):
        np.random.seed(seed)
        error = np.random.normal(0, error)
        # apply u3 gate to qubit q
        self.dm = np.dot(np.dot(np.kron(np.eye(2**q), np.array([[np.cos(theta/2), -np.exp(1j*lam)*np.sin(theta/2)], [np.exp(1j*phi)*np.sin(theta/2), np.exp(1j*(phi+lam))*np.cos(theta/2)]])), self.dm)
        
        # add an error gate that doesn't show up in the circuit diagram
        if error > 0:
            self.dm = np.dot(np.dot(np.kron(np.eye(2**q), sp.linalg.expm(1j*error*np.array([[0, 1], [1, 0]]))), self.dm))
        
        return self