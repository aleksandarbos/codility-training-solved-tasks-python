# Task 1: Subarray Sum
# Problem: Given an array of integers and multiple queries, each query asks for the sum of elements in a specific subarray.

# Example:

# Input: arr = [1, 2, 3, 4, 5], queries = [(0, 2), (1, 3), (0, 4)]
# Output: [6, 9, 15]


# time complexity: O(n+m)
# space complexity: O(n+m)
def solution(A, Q):
    N = len(A)
    sums = [0] * (N+1)
    results = []

    for i in range(N):  # O(n)
        sums[i+1] = sums[i] + A[i]

    for start, end in Q:  # O(m)
        results.append(sums[end+1] - sums[start])

    return results


# def solution2(A, Q):
#     N = len(A)
#     sums = [0] * (N)
#     results = []

#     for i in range(N):  # O(n)
#         sums[i] = sums[i-1] + A[i] if i > 0 else sums[i] + A[i]

#     for start, end in Q:  # O(m)
#         if start == 0:
#             results.append(sums[end])
#         else:
#             results.append(sums[end] - sums[start-1])

#     return results


if __name__ == "__main__":
    assert solution([1, 2, 3, 4, 5], [(0, 2), (1, 3), (0, 4)]) == [6, 9, 15]
