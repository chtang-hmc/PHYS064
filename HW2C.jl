# Problem 4
using Pkg
Pkg.add("Plots")

function plot_Fourier()

    x = range(0, 10, length=100)
    y = sin.(x)
    plot(x, y)

end

plot_Fourier()

# Problem 5 (c)
function verifypi2()

    # Outputs: the value of pi square to 0.1% accuracy

    i = 0
    result = 0
    while abs(result - pi^2) > 0.001*pi^2
        result += 8/((2*i+1)^2)
        i += 1
    end

    println(sqrt(result))
    
    return (result, i)
end

# Problem 6 (a)
function tri(B,b)

# Inputs
#
# B: a tridiagonal matrix given as an array with N rows and three columns. 
# The first and last entries would necessarily be unused. 
# b: An N-component array representing the b vector
#
# Outputs:
#
# x: the solution vector to A x = b
#
# You can find the algorithm to implement, known as the Thomas algorithm, below.

end
