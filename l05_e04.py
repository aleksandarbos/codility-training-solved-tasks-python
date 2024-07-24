# A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

# For example, array A such that:

#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# contains the following example slices:

# slice (1, 2), whose average is (2 + 2) / 2 = 2;
# slice (3, 4), whose average is (5 + 1) / 2 = 3;
# slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
# The goal is to find the starting position of a slice whose average is minimal.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the starting position of the slice with the minimal average. If there is more than one slice with a minimal average, you should return the smallest starting position of such a slice.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000].


# def solution(A):
#     N = len(A)
#     sums = [0] * (N+1)
#     min_avg_slice = float('inf')
#     min_p_index = float('inf')

#     for i in range(N):
#         sums[i+1] = sums[i] + A[i]

#     for i in range(N):
#         for j in range(i+1, N):
#             avg_slice = (sums[j+1] - sums[i]) / (j-i+1)
#             if avg_slice < min_avg_slice:
#                 min_avg_slice = avg_slice
#                 min_p_index = i

#     return min_p_index


# time complexity: O(n)
# space complexity: O(n)
def solution(A):
    N = len(A)
    sums = [0] * (N+1)
    min_avg_slice = float('inf')
    min_p_index = float('inf')

    for i in range(N):  # O(n)
        sums[i+1] = sums[i] + A[i]

    # well according to some math, most impact of avg comes when having slices of 2 and 3 elements max
    # the other ones will just be more granular, but will average out instead of having greater impact
    for i in range(N-1):  # O(n)
        avg_slice = (sums[i+2] - sums[i]) / 2  # +1 because of 0 index in sums
        # print(f'checking slice: ({A[i]}, {A[i+1]}), avg: {avg_slice}')
        if avg_slice < min_avg_slice:
            min_avg_slice = avg_slice
            min_p_index = i

        if i < N - 2:
            avg_slice = (sums[i+3] - sums[i]) / 3
            if avg_slice < min_avg_slice:
                min_avg_slice = avg_slice
                min_p_index = i

    return min_p_index


if __name__ == "__main__":
    assert solution([5, 1, 3]) == 1
