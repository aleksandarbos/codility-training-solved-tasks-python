# A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P ≤ Q < N, is called a slice of array A. The sum of a slice (P, Q) is the total of A[P] + A[P+1] + ... + A[Q].

# Write a function:

# def solution(A)

# that, given an array A consisting of N integers, returns the maximum sum of any slice of A.

# For example, given array A such that:

# A[0] = 3  A[1] = 2  A[2] = -6
# A[3] = 4  A[4] = 0
# the function should return 5 because:

# (3, 4) is a slice of A that has sum 4,
# (2, 2) is a slice of A that has sum −6,
# (0, 1) is a slice of A that has sum 5,
# no other slice of A has sum greater than (0, 1).
# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..1,000,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000];
# the result will be an integer within the range [−2,147,483,648..2,147,483,647].

# time complexity: O(n)
# space complexity: O(1)
def solution(A):
    max_slice = 0
    base = 0

    if len(A) == 1:
        return A[0]

    max_el = max(A)  # O(n)
    if max_el < 0:
        return max_el

    for num in A:  # O(n)
        base = max(0, base + num)  # O(1)
        max_slice = max(max_slice, base)  # O(1)
    return max_slice


if __name__ == "__main__":
    assert solution([-4, -6, -2, -3]) == -2
    assert solution([-1]) == -1
    assert solution([0]) == 0
    assert solution([-1, 1]) == 1
    assert solution([-5, 6]) == 6
    assert solution([-1, 0, 2]) == 2
    assert solution([4, -1, 0, 2]) == 5
