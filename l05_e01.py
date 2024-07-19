# A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

# Array A contains only 0s and/or 1s:

# 0 represents a car traveling east,
# 1 represents a car traveling west.
# The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

# For example, consider array A such that:

#   A[0] = 0
#   A[1] = 1
#   A[2] = 0
#   A[3] = 1
#   A[4] = 1
# We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

# Write a function:

# def solution(A)

# that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

# The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

# For example, given:

#   A[0] = 0
#   A[1] = 1
#   A[2] = 0
#   A[3] = 1
#   A[4] = 1
# the function should return 5, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer that can have one of the following values: 0, 1.

# time complexity: 2 * O(n) => O(n)
# space complexity: O(1)
def solution(A):
    total = sum(A) # O(n)
    sum_cnt = 0
    total_pairs = 0

    for car in A: # O(n)
        sum_cnt += car
        if car == 0: # east
            total_pairs += total - sum_cnt
    if total_pairs > 10**9:
        return -1
    return total_pairs


if __name__ == "__main__":
    assert solution([0]) == 0
    assert solution([1]) == 0
    assert solution([0, 0]) == 0
    assert solution([0, 1]) == 1
    assert solution([1, 0]) == 0
    assert solution([0, 1, 1]) == 2
    assert solution([0, 1, 0, 1, 1]) == 5
