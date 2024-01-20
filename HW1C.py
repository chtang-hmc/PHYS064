import numpy as np
import scipy as sp

def pi2by6(accuracy):

# Inputs:
#
# accuracy: A number between 0 and 1 denoting the percent error in the result.
# 
# Outputs:
#  
# Returns (value, N): 
#   value is an approximation to pi square over six.
#   N is the number of terms used in the sum formula.

    def calculate_term(i):
        return 1/((i+1)**2)

    terms = np.fromfunction(calculate_term, (accuracy,), dtype=np.float64)
                                
    sum_terms = np.sum(terms)
        
    return sum_terms, accuracy

def energy(terms, b):
    
# Inputs:
#
# terms: a positive non-zero number determining the desired precision 
# as determined by the number of terms used in the sums above.
# b: The dimensionless quantity hbar omega over k_B T
#
# Outputs:
#
# Returns a floating point number that is the average energy per hbar omega
#
# Notice how we have ensured that the two arguments and output are all 
# dimensionless quantities, measured in the appropriate scales in the problem.

    def calculate_Z(n):
        return np.exp(-b*(n+0.5))
    terms_Z = np.fromfunction(calculate_Z, (terms,), dtype=np.float64)
    Z = np.sum(terms_Z)
    
    def calculate_E_n(n):
        return (n+0.5)*terms_Z[n]
    
    E_average = np.sum(np.fromfunction(calculate_E_n, (terms,), dtype=np.float64))/Z
    
    return E_average
