

# A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

# A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

# You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

# For example, given:

#         N = 15 and M = 75, the prime divisors are the same: {3, 5};
#         N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
#         N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.

# Write a function:

#     def solution(A, B)

# that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

# For example, given:
#     A[0] = 15   B[0] = 75
#     A[1] = 10   B[1] = 30
#     A[2] = 3    B[2] = 5

# the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

# Write an efficient algorithm for the following assumptions:

#         Z is an integer within the range [1..6,000];
#         each element of arrays A and B is an integer within the range [1..2,147,483,647].


def get_primes(n):
    result = set()

    k = 2
    while k*k <= n:  # calculate Trial division primes
        if n % k == 0:
            result.add(k)
        k += 1

    j = n
    for prime_factor in result:  # calculate cofactor
        while j % prime_factor == 0:
            j //= prime_factor
    if j > 1:
        result.add(j)
    return result


def solution(A, B):
    Z = len(A)
    prime_divisors = {}
    result = 0

    for i in range(Z):
        a, b = A[i], B[i]

        if not a in prime_divisors:
            prime_divisors[a] = get_primes(a)

        if not b in prime_divisors:
            prime_divisors[b] = get_primes(b)

        if prime_divisors[a] and (prime_divisors[a] == prime_divisors[b]):
            result += 1

    return result


if __name__ == "__main__":
    assert solution([15, 10, 3], [75, 30, 5]) == 1
    assert solution([1], [1]) == 0
    assert solution([1, 75], [5, 15]) == 1
    assert solution([2147483647], [2147483646]) == 0
