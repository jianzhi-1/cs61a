def is_prime(n):
  return (n > 1) and smallest_factor(n) == n

def smallest_factor(n):
  k = 2
  while (k <= n):
    if (n % k == 0): return k
    k += 1

def print_factors(n):
  while (n != 1):
    x = smallest_factor(n)
    print(x)
    n //= x
