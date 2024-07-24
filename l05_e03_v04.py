# Task 10: Count Prime Numbers in Range
# Problem: Given an array of integers and multiple queries, each query asks for the number of prime numbers in a specific subarray.

# Example:

# Input: arr = [1, 2, 3, 4, 5, 6], queries = [(0, 3), (1, 4), (2, 5)]
# Output: [2, 3, 2]


# time complexity: O(sqrt(n))
def is_prime(num):
    if num <= 1:
        return False

    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1

    return True


# time complexity: O(n+m)
def solution(A, Q):
    N = len(A)
    sums = [0] * (N+1)
    results = []

    for i in range(N):  # O(n)
        sums[i+1] = sums[i] + (1 if is_prime(A[i]) else 0)

    for start, end in Q:
        results.append(sums[end+1] - sums[start])

    return results


if __name__ == "__main__":
    assert solution([1, 2, 3, 4, 5, 6], [(0, 3), (1, 4), (2, 5)]) == [2, 3, 2]
