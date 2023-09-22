import timeit
import numpy as np

prime_factorization_cache = {}

def betterPrimeFactorization(low=2, high=1000):
    for i in range (low,high):
        uniquePrimes = set()
        currentPrime = i
        for j in range (2,int(i**0.5) + 1):
            checkPrime = j
            flag = False
            if j%2==0:
                flag = True
            else:
                for k in range (3,checkPrime - 1, 2):
                    if (j%k==0):
                        flag = True
                        break
            if (not flag and i%checkPrime==0 and checkPrime <= i) or (checkPrime==2 and i%checkPrime==0):
                while (currentPrime%checkPrime==0):
                    currentPrime/=checkPrime
                if currentPrime in prime_factorization_cache.keys():
                    for q in prime_factorization_cache[currentPrime]:
                        uniquePrimes.add(q)

                uniquePrimes.add(checkPrime)
        if len(uniquePrimes) == 0:
            uniquePrimes.add(i)
        
        if i not in prime_factorization_cache.keys():
            prime_factorization_cache[i] = uniquePrimes

        # print(i, uniquePrimes)

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