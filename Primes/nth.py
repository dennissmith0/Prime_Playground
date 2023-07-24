def nth_prime(n):
    primes = [2]
    candidate = 3
    while len(primes) < n:
        is_prime = True
        for prime in primes:
            if prime * prime > candidate:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(candidate)
        candidate += 2
    return primes[-1]


if __name__ == "__main__":
    n = 111
    for i in range(n+1):
        print(nth_prime(i))