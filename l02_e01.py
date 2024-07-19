# An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).

# The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.

# Write a function:

# def solution(A, K)

# that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.

# For example, given

#     A = [3, 8, 9, 7, 6]
#     K = 3
# the function should return [9, 7, 6, 3, 8]. Three rotations were made:

#     [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
#     [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
#     [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
# For another example, given

#     A = [0, 0, 0]
#     K = 1
# the function should return [0, 0, 0]

# Given

#     A = [1, 2, 3, 4]
#     K = 4
# the function should return [1, 2, 3, 4]

# Assume that:

# N and K are integers within the range [0..100];
# each element of array A is an integer within the range [−1,000..1,000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.

# time complexity: O(n)
# space complexity: 2*O(n) => O(n)
def solution(A, K):
    if not A:
        return A

    if K > len(A):
        K = K % len(A) # rotating 3 times is the same as 3*3*3..., etc.

        if K == 0: # will end up at the starting position
            return A

    rotated_array = len(A) * [0]
    for i, num in enumerate(A):
        new_i = (i + K) % len(A)
        rotated_array[new_i] = num

    return rotated_array

if __name__ == "__main__":
    assert solution([1, 2, 3], 1) == [3, 1, 2]
    assert solution([1, 2, 3], 81) == [1, 2, 3]
    assert solution([3, 8, 9, 7, 6], 1) == [6, 3, 8, 9, 7]
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
    assert solution([], 3) == []
    assert solution([1, 2, -300], 0) == [1, 2, -300]
    assert solution([], 0) == []
