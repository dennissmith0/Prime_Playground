import time


def create_list(r1, r2):
    """Create list of prime numbers between r1 and r2."""

    # Testing if range r1 and r2 are equal
    if r1 == r2:
        return r1
    else:
        # Create empty lists
        res = []  # reserve
        poss = []  # possible primes
        mult = []  # multiples of primes

        # Loop to append successors to list until r2 is reached.
        while r1 < r2 + 1:
            res.append(r1)
            r1 += 1

        # Extract all multiples of 6 from reserve list
        multiples_6 = [n for n in res if n % 6 == 0]

        # Create list with + 1 and - 1 values from each multiple of 6
        # because these are the only numbers that can be prime
        for val in multiples_6:
            poss.append(val - 1)
            poss.append(val + 1)

        # Create list of multiples with all possible combinations of elements
        # in the possible list, unless that value exceeds r2
        start = 0

        for i in range(len(poss)):
            for y in range(i, len(poss)):
                val = poss[i] * poss[y]
                upper_limit = r2
                if val <= upper_limit and val not in mult:
                    mult.append(val)
                elif val >= upper_limit:
                    break
            if val >= upper_limit * 2:
                break

        # Subtract the amount of multiples from the amount of possible primes,
        # add 2 (for 2 and 3), and this is the amount of primes up to upper_limit
        return len(poss) - len(mult) + 2


def main():
    exit = "N"

    while exit.upper() != "Y":

        # Driver Code
        r1, r2 = 2, int(input("Enter an integer: ")),
        start = time.time()

        print(create_list(r1, r2))

        end = time.time()
        print('Time ', end - start)

        exit = input("Would you like to exit? (Y/N)")


if __name__ == "__main__":
    main()
