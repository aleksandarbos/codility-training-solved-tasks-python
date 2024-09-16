

# A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

# A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

# You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

# Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

# For example, consider an integer N = 26 and arrays P, Q such that:
#     P[0] = 1    Q[0] = 26
#     P[1] = 4    Q[1] = 10
#     P[2] = 16   Q[2] = 20

# The number of semiprimes within each of these ranges is as follows:

#         (1, 26) is 10,
#         (4, 10) is 4,
#         (16, 20) is 0.

# Write a function:

#     def solution(N, P, Q)

# that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

# For example, given an integer N = 26 and arrays P, Q such that:
#     P[0] = 1    Q[0] = 26
#     P[1] = 4    Q[1] = 10
#     P[2] = 16   Q[2] = 20

# the function should return the values [10, 4, 0], as explained above.

# Write an efficient algorithm for the following assumptions:

#         N is an integer within the range [1..50,000];
#         M is an integer within the range [1..30,000];
#         each element of arrays P and Q is an integer within the range [1..N];
#         P[i] ≤ Q[i].

def prime_f(n):
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


# def factorization(n, F):  # O(log(n))
#     prime_factors = []
#     while F[n] > 0:
#         prime_factors.append(F[n])
#         n = n // F[n]
#     prime_factors.append(n)
#     return prime_factors


# def solution(N, P, Q): # O(n*log(n))
#     F = prime_f(N)
#     semiprimes = [0] * (N+1)
#     M = len(P)  # same as len(Q)
#     result = []

#     for i in range(4, N+1):  # first semiprime is at 4
#         factors = factorization(i, F)
#         if len(factors) == 2:
#             semiprimes[i] = 1

#     for k in range(M):
#         p, q = P[k], Q[k]
#         result.append(sum(semiprimes[p:q+1]))

#     return result


def is_semiprime(n, F):  # each semiprime num has exactly 2 prime factors
    if F[n] == 0:
        return False
    n = n // F[n]
    if F[n] != 0:
        return False
    return True


def solution(N, P, Q):  # optimized solution
    F = prime_f(N)
    M = len(P)  # same as len(Q)
    cnt_array = [0] * (N+1)
    semiprimes_cnt = 0
    result = []

    for i in range(4, N+1):  # first semiprime is at 4
        if is_semiprime(i, F):
            cnt_array[i] += semiprimes_cnt + 1
            semiprimes_cnt += 1
        else:
            cnt_array[i] = semiprimes_cnt

    for k in range(M):
        p, q = P[k], Q[k]
        result.append(cnt_array[q]-cnt_array[p-1])

    return result


if __name__ == "__main__":
    assert solution(26, [1, 4, 16], [26, 10, 20]) == [10, 4, 0]
    assert solution(26, [1], [4]) == [1]
    assert solution(26, [1], [6]) == [2]
    assert solution(26, [1, 5], [26, 6]) == [10, 1]
