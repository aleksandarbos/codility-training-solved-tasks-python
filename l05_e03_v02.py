# Task 2: Count of Even Numbers in Range
# Problem: Given an array of integers and multiple queries, each query asks for the number of even numbers in a specific subarray.

# Example:

# Input: arr = [1, 2, 3, 4, 5], queries = [(0, 2), (1, 4), (2, 4)]
# Output: [1, 2, 1]


# time complexity: O(n+m)
# space complexity: O(n+m)
def solution(A, Q):
    N = len(A)
    sums = [0] * (N+1)
    results = []

    for i in range(N):  # O(n)
        sums[i+1] = sums[i] + (1 if A[i] % 2 == 0 else 0)

    for start, stop in Q:  # O(m)
        results.append(sums[stop+1] - sums[start])

    return results


if __name__ == "__main__":
    assert solution([1, 2, 3, 4, 5], [(0, 2), (1, 4), (2, 4)]) == [1, 2, 1]
