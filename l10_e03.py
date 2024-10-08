# A non-empty array A consisting of N integers is given.

# A peak is an array element which is larger than its neighbours. More precisely, it is an index P such that 0 < P < N − 1 and A[P − 1] < A[P] > A[P + 1].

# For example, the following array A:

#     A[0] = 1
#     A[1] = 5
#     A[2] = 3
#     A[3] = 4
#     A[4] = 3
#     A[5] = 4
#     A[6] = 1
#     A[7] = 2
#     A[8] = 3
#     A[9] = 4
#     A[10] = 6
#     A[11] = 2
# has exactly four peaks: elements 1, 3, 5 and 10.

# You are going on a trip to a range of mountains whose relative heights are represented by array A, as shown in a figure below. You have to choose how many flags you should take with you. The goal is to set the maximum number of flags on the peaks, according to certain rules.

# https://codility-frontend-prod.s3.amazonaws.com/media/task_static/flags/static/images/auto/6f5e8faa3000c0a74157e6e0bc759b8a.png

# Flags can only be set on peaks. What's more, if you take K flags, then the distance between any two flags should be greater than or equal to K. The distance between indices P and Q is the absolute value |P − Q|.

# For example, given the mountain range represented by array A, above, with N = 12, if you take:

# two flags, you can set them on peaks 1 and 5;
# three flags, you can set them on peaks 1, 5 and 10;
# four flags, you can set only three flags, on peaks 1, 5 and 10.
# You can therefore set a maximum of three flags in this case.

# Write a function:

# def solution(A)

# that, given a non-empty array A of N integers, returns the maximum number of flags that can be set on the peaks of the array.

# For example, the following array A:

#     A[0] = 1
#     A[1] = 5
#     A[2] = 3
#     A[3] = 4
#     A[4] = 3
#     A[5] = 4
#     A[6] = 1
#     A[7] = 2
#     A[8] = 3
#     A[9] = 4
#     A[10] = 6
#     A[11] = 2
# the function should return 3, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..400,000];
# each element of array A is an integer within the range [0..1,000,000,000].

# time complexity: O(n) + O(sqrt(N)) => O(n)
# space complexity: O(P) // P - num of peaks
def solution(A):
    N = len(A)
    peaks = []

    if N < 3:  # need at least 3 points to form a peak
        return 0

    for i in range(1, N-1):  # O(n)
        if A[i-1] < A[i] > A[i+1]:
            peaks.append(i)

    if not peaks:
        return 0
    elif len(peaks) == 1:
        return 1

    max_peaks = min(len(peaks), int((peaks[-1] - peaks[0]) ** 0.5 + 1))
    for flags in range(max_peaks, 0, -1):
        placed = 1
        last_pos = peaks[0]

        for i in range(1, len(peaks)):  # O(sqrt(n))
            if peaks[i] - last_pos >= flags:
                placed += 1
                last_pos = peaks[i]
                if placed == flags:
                    return flags
    return 0


if __name__ == "__main__":
    assert solution([1, 2, 1]) == 1
    assert solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3
    assert solution([1, 5, 1, 1, 5, 1]) == 2
    assert solution([1, 1, 2]) == 0
    assert solution([0]) == 0
    assert solution([1]) == 0
    assert solution([1, 2]) == 0
    assert solution([2, 1]) == 0
