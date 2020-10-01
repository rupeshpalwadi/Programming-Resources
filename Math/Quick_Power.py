# An algorithm that takes raises b to power n mod M in O(log(n)) time
def quick_pow(b, n):
    M = 1_000_000_013
    final = 1

    while n > 0:

        # Odd, multiply it by the result once then when // goes to one
        if n % 2 == 1:
            final = (final * b) % M

        # E.g ((a^2)^2)^... Do this log(n) times
        n //= 2
        b = (b**2) % M

    return final


print(quick_pow(2, 1_000_000))
