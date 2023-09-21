import timeit
import numpy as np

def betterPrimeFactorization(low=2, high=1000):
    for i in range (low,high):
        uniquePrimes = []
        currentPrime = i
        for j in range (2,i):
            checkPrime = j
            flag = False
            if (j%2==0):
                flag = True
                break
            for k in range (3,np.ceil(checkPrime**0.5), 2):
                if (j%k==0):
                    flag = True
                    break
            if not flag and i%checkPrime==0 and checkPrime <= i:
                while (currentPrime%checkPrime==0):
                    currentPrime/=checkPrime
                uniquePrimes.append(checkPrime)
        if len(uniquePrimes) == 0:
            uniquePrimes.append(i)

# Benchmark the code
if __name__ == "__main__":
    benchmark_code = "betterPrimeFactorization()"
    setup_code = "from __main__ import betterPrimeFactorization"

    # Measure the execution time of betterPrimeFactorization function
    times = []
    for i in range(0,5):
        times.append(timeit.timeit(benchmark_code, setup=setup_code, number=1))

    res = sum(times)/5

    print(f"Average execution time after 5 runs: {res:.6f} seconds")
