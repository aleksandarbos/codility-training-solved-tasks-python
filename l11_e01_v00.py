# 11.1: Sieve of Eratosthenes.


# time complexity: O(n*log log(n))
# space complexity: O(n)
def get_primes(n):
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False

    i = 2
    while i*i <= n:
        if sieve[i]:
            k = i*i
            while k <= n:
                sieve[k] = False
                k += i
        i += 1
    return sieve


# time complexity: O(n*log log(n))
# space complexity: O(n)
def array_F(n):
    F = [0] * (n+1)

    i = 2
    while i*i <= n:
        if F[i] == 0:
            k = i*i
            while k <= n:
                if F[k] == 0:
                    F[k] = i
                k += i
        i += 1
    return F


# time complexity: O(log(x))
# space complexity: O(pf)  # pf - number of prime factors for num x
def factorization(x, F):
    prime_factors = []
    while F[x] > 0:
        prime_factors += [F[x]]
        x //= F[x]
    prime_factors += [x]
    return prime_factors


def fact(x):
    F = array_F(x)
    return factorization(x, F)


if __name__ == "__main__":
    assert [i for i, is_prime in enumerate(get_primes(17)) if is_prime] == [
        2, 3, 5, 7, 11, 13, 17]

    assert array_F(20) == [0, 0, 0, 0, 2, 0, 2, 0, 2, 3,
                           2, 0, 2, 0, 2, 3, 2, 0, 2, 0, 2]

    assert fact(14) == [2, 7]
    assert fact(20) == [2, 2, 5]
