# goit-algo-hw-10
Algo homework 10

## Pulp example + Monte-Carlo method implementation

1. pulp_calculation.py -> Example of using pulp to solve optimization problem
2. monte_carlo.py -> Implementation of Monte-Carlo algorithm

## Monte-Carlo results
Test on f(x) = x^3
    Integral for f(x) = x^3 via Monte-Carlo method is: 319.73184000, samples used for randomization: 500
    Integral for f(x) = x^3 via Monte-Carlo method is: 318.12480000, samples used for randomization: 5000
    Integral for f(x) = x^3 via Monte-Carlo method is: 320.45760000, samples used for randomization: 50000
    Integral for f(x) = x^3 via scipy is: 320.00000000

As we can see, Monte-Carlo gives close result, but still not as close as scipy.quad().
Precision of Monte-Carlo calculation grows as we use more samples count for randomization. 
But it may be not predictable, for example in calculations about calculation with 500 samples was even more precise than calculation with 5000 samples. 
