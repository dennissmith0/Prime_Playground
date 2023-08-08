import time


# # def create_list(r1, r2):
# #     """Create list of prime numbers between r1 and r2."""

# #     # Testing if range r1 and r2 are equal
# #     if r1 == r2:
# #         return r1
# #     else:
# #         # Create empty lists
# #         res = []  # reserve
# #         poss = []  # possible primes
# #         mult = []  # multiples of primes

# #         # Loop to append successors to list until r2 is reached.
# #         while r1 < r2 + 1:
# #             res.append(r1)
# #             r1 += 1

# #         # Extract all multiples of 6 from reserve list
# #         multiples_6 = [n for n in res if n % 6 == 0]

# #         # Create list with + 1 and - 1 values from each multiple of 6
# #         # because these are the only numbers that can be prime
# #         for val in multiples_6:
# #             poss.append(val - 1)
# #             poss.append(val + 1)

# #         # Create list of multiples with all possible combinations of elements
# #         # in the possible list, unless that value exceeds r2
# #         start = 0

# #         for i in range(len(poss)):
# #             for y in range(i, len(poss)):
# #                 val = poss[i] * poss[y]
# #                 upper_limit = r2
# #                 if val <= upper_limit and val not in mult:
# #                     mult.append(val)
# #                 elif val >= upper_limit:
# #                     break
# #             if val >= upper_limit * 2:
# #                 break

# #         # Subtract the amount of multiples from the amount of possible primes,
# #         # add 2 (for 2 and 3), and this is the amount of primes up to upper_limit
# #         return len(poss) - len(mult) + 2


# # def main():
# #     exit = "N"

# #     while exit.upper() != "Y":

# #         # Driver Code
# #         r1, r2 = 2, int(input("Enter an integer: ")),
# #         start = time.time()

# #         print(create_list(r1, r2))

# #         end = time.time()
# #         print('Time ', end - start)

# #         exit = input("Would you like to exit? (Y/N)")


# # if __name__ == "__main__":
# #     main()


def create_and_count(n):
    # Create list of all multiples of 6 up to n
    multiples_6 = [x for x in range(2, n+1) if x % 6 == 0]
    
    # Create list of all numbers 1 more or 1 less than a multiple of 6 (possible primes)
    poss = [val + delta for val in multiples_6 for delta in (-1, 1) if val + delta <= n]
    
    # Create list of all products of possible primes (multiples)
    mult = [i * j for i_index, i in enumerate(poss) for j in poss[i_index:] if i * j <= n]
    
    # Number of primes is difference of possible primes and multiples, plus 2 (for 2 and 3)
    return len(poss) - len(set(mult)) + 2


def main():
    exit = "N"

    while exit.upper() != "Y":

        n = int(input("Enter an integer: "))
        start = time.time()

        print(create_and_count(n))
        # print(create_and_count(100))  # Should print 25
        # print(create_and_count(1000))  # Should print 168
        # print(create_and_count(10000))  # Should print 1229
        # print(create_and_count(100000))  # Should print 9592

        end = time.time()
        print('Time ', end - start)

        exit = input("Would you like to exit? (Y/N)")


if __name__ == "__main__":
    main()
