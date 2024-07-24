# Write a function:

# def solution(A, B, K)

# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

# { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

# Write an efficient algorithm for the following assumptions:

# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.

# time complexity: O(1)
# space complexity: O(1)
def solution(A, B, K):
    result = B//K - max(A-1, 0) // K
    # every number is dividable by 0, therefore if 0, include it
    return result + 1 if A == 0 else result


if __name__ == "__main__":
    assert solution(0, 0, 1) == 1
    assert solution(0, 1, 1) == 2
    assert solution(0, 5, 5) == 2
    assert solution(0, 5, 6) == 1
    assert solution(0, 10, 1) == 11
    assert solution(0, 10, 2) == 6
