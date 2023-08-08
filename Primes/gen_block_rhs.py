def get_user_input():
    try:
        n = int(input("Enter an integer (we will find all prime blocks up to this n): "))
        k = n // 6
        return n, k
    except ValueError:
        print("Please enter a valid integer.")
        return get_user_input()
    

def generate_rhs(k):
    # Start with the first prime one less than a multiple of 6
    prime = 7
    primes = [prime]

    # Generate the rest of the possible primes up to k
    while prime <= k:
        prime += 6  # Add 6 to get the next prime one less than a multiple of 6
        # Check if the number is a perfect square
        if int(prime ** 0.5) ** 2 != prime and prime**2 <= n:            
            primes.append(prime)
    return primes


# Function to convert a sequence and index position back to an integer
def position_to_integer(sequence, index):
    if index == 5:
        return (sequence + 1) * 6 + 1
    elif index == 3:
        return (sequence + 1) * 6 - 1


def generate_blocking_positions(n, primes):
    blocking_positions_dict = {}

    # Calculate the number of sequences
    num_sequences = n // 6 + 1
    row = 0

    for i, p in enumerate(primes):
        blocking_positions = []
        row += 1
        # Generate blocking positions for multiples of `p` on RHS
        # Start from sequence `p` - 2 and increment by `p` each time
        for sequence in range((7 * row) - p, num_sequences, p):
            if position_to_integer(sequence, 5) >= p**2:
                blocking_positions.append((sequence, 5))

        # Generate blocking positions for multiples of `p` on LHS
        # Start from sequence `p` + 5 and increment by `p` each time
        for sequence in range(p - (row + 1), num_sequences, p):
            if position_to_integer(sequence, 3) >= p**2:
                blocking_positions.append((sequence, 3))

        blocking_positions_dict[p] = blocking_positions
        
    return blocking_positions_dict

n, k = get_user_input()
blocking_positions_dict = generate_blocking_positions(n, generate_rhs(k))

for p, blocking_positions in blocking_positions_dict.items():
    print(f"Blocking positions for {p}:")
    print(blocking_positions)
    print()

# Print the integer values corresponding to the blocking positions
blocking_integers_dict = {p: sorted([position_to_integer(sequence, index) for sequence, index in blocking_positions]) for p, blocking_positions in blocking_positions_dict.items()}

print(blocking_integers_dict)
