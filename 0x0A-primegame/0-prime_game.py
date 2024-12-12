#!/usr/bin/python3

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if not nums or x <= 0:
        return None

    wins_maria = 0
    wins_ben = 0

    for n in nums:
        primes_left = [i for i in range(1, n + 1) if is_prime(i)]

        current_player = "Maria"
        while primes_left:
            move = min(primes_left)
            primes_left = [num for num in primes_left if num % move != 0]

            if not primes_left:
                break

            if current_player == "Maria":
                current_player = "Ben"
            else:
                current_player = "Maria"

        if current_player == "Maria":
            wins_maria += 1
        else:
            wins_ben += 1

    if wins_maria > wins_ben:
        return "Maria"
    elif wins_ben > wins_maria:
        return "Ben"
    else:
        return None

if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
