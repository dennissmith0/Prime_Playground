import time


def primes_up_to(n):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not prime.
    for current in range(2, int(n**0.5) + 1):
        if sieve[current]:  # If current is prime
            for multiple in range(current**2, n + 1, current):  # Mark multiples of current
                sieve[multiple] = False
    primes = [x for x, is_prime in enumerate(sieve) if is_prime]
    return primes


if __name__ == "__main__":
    n = 10000000
    # for i in range(n+1):
    #     print(primes_up_to(i))

    start = time.time()

    print(primes_up_to(n))
    print(len(primes_up_to(n)))

    end = time.time()
    print('Time ', end - start)
