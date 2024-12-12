#!/usr/bin/python3
def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Args:
        x (int): Number of rounds
        nums (list): Array of integers, where each integer n represents the
                     range [1, n] for a game round

    Returns:
        str: Name of the player who won the most rounds ("Maria" or "Ben"),
             or None if there is a tie.
    """
    if x <= 0 or not nums:
        return None

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    # Track the winners for each round
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(primes[:n + 1])

        # If the count of primes is odd, Maria wins this round (optimal play)
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None

def sieve_of_eratosthenes(n):
    """
    Generate a list of prime numbers up to n using the Sieve of Eratosthenes.

    Args:
        n (int): The upper limit to check for primes.

    Returns:
        list: A list where the i-th index is True if i is a prime, otherwise False.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    return primes
