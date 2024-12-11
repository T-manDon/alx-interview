#!/usr/bin/python3
"""
Solution to the Prime Game problem. This script defines the function isWinner 
that determines the winner of the game based on prime number counts.
"""

def primes(n):
    """Generate a list of prime numbers up to the specified limit (inclusive).
       Args:
        n (int): The upper boundary of the range, starting from 1.
       Returns:
        List of prime numbers between 1 and n.
    """
    prime = []  # List to store prime numbers
    sieve = [True] * (n + 1)  # Sieve of Eratosthenes setup for finding primes
    for p in range(2, n + 1):  # Check each number from 2 to n
        if sieve[p]:  # If p is still marked as prime
            prime.append(p)  # Add prime to the list
            # Mark multiples of p as non-prime
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime  # Return the list of primes found


def isWinner(x, nums):
    """
    Determines the winner of the Prime Game.
    Args:
        x (int): The number of rounds in the game.
        nums (list): List of integers where each number represents 
                     the upper boundary of the prime number range for a round.
    Returns:
        The name of the winner ('Maria' or 'Ben'), or None if there is no winner.
    """
    # If input parameters are invalid, return None
    if x is None or nums is None or x == 0 or nums == []:
        return None
    
    Maria = Ben = 0  # Initialize scores for Maria and Ben
    for i in range(x):  # Loop through each round
        prime = primes(nums[i])  # Get the list of primes up to nums[i]
        # If the number of primes is even, Ben wins that round
        if len(prime) % 2 == 0:
            Ben += 1
        else:  # If the number of primes is odd, Maria wins that round
            Maria += 1
    
    # Return the name of the player with the most rounds won
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None  # In case of a tie, return None

