# A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

# For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the number of its factors.

# For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].


# if there is integer M, that means that N/D must be integer too,
# since M = N/D, therefore no reminder on division between N and D.

# time complexity: O(sqrt(n))
# space complexity: O(1)
def solution(N):
    cnt = 0
    i = 1

    while i * i < N:
        if N % i == 0:
            cnt += 2  # that number and it's symmetric divisor

        i += 1

    if i * i == N:
        cnt += 1

    return cnt
