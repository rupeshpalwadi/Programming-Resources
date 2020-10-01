# Calculaing the GCD using the Euclidean Algorithm and recursion
def gcd(m, n):
    # Base case:
    if n == 0: 
        return m

    return gcd(n, m%n)


# Calculating the LCM using the GCD function
def lcm(m, n):
    return m*n // gcd(m, n)

print(gcd(8, 24))
print(lcm(5, 6))
