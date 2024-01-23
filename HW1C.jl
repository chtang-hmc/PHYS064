# Problem 2
function pi2by6(accuracy)
# Inputs:
#
# accuracy: A number between 0 and 1 denoting the percent error in the result.
# 
# Outputs:
#  
# Returns (value, N): 
#   value is an approximation to pi square over six.
#   N is the number of terms used in the sum formula.

    sum_terms = 0
    for i = 1:accuracy
        sum_terms += 1/(i^2)
    end
    return (sum_terms, accuracy)
end

# Problem 4
function energy(terms, b)
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
    Z = 0
    for i = 0:terms
        Z += exp(-b*(i+0.5))
    end

    E_average = 0
    for i = 0:terms
        E_average += (i+0.5)*exp(-b*(i+0.5))
    end

    return E_average/Z
end