# A non-empty array A consisting of N integers is given.

# A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].

# For example, the following array A:

#     A[0] = 1
#     A[1] = 2
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
# has exactly three peaks: 3, 5, 10.

# We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:

# A[0], A[1], ..., A[K − 1],
# A[K], A[K + 1], ..., A[2K − 1],
# ...
# A[N − K], A[N − K + 1], ..., A[N − 1].
# What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).

# The goal is to find the maximum number of blocks into which the array A can be divided.

# Array A can be divided into blocks as follows:

# one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
# two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
# three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.
# However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak. Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].

# The maximum number of blocks that array A can be divided into is three.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.

# If A cannot be divided into some number of blocks, the function should return 0.

# For example, given:

#     A[0] = 1
#     A[1] = 2
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

# time complexity: O(n)
# space complexity: O(n)
def solution(A):
    N = len(A)
    peaks_sum_prefix = [0] * (N+1)

    if N < 3:
        return 0

    s = 0
    for i in range(1, N+1):
        peaks_sum_prefix[i] += s
        if i < N and A[i-1] < A[i] > A[i+1]:
            s += 1

    peaks_cnt = peaks_sum_prefix[-1]
    if peaks_cnt == 0:
        return 0
    elif peaks_cnt == 1:
        return 1

    max_divs = int(N**0.5 + 1)
    i = 0
    max_blocks = 0
    for k in range(1, max_divs+1):  # O(sqrt(N))
        cnt = 0
        has_peaks = False
        while i*k+k+1 <= len(peaks_sum_prefix):
            end_idx, start_idx = i*k+k, i*k+1
            if peaks_sum_prefix[end_idx] - peaks_sum_prefix[start_idx] == 0:
                break
            cnt += 1
            i += 1
            has_peaks = True
        if has_peaks:
            max_blocks = max(max_blocks, cnt)

    return max_blocks


if __name__ == "__main__":
    assert solution([1, 2, 1, 2, 1, 1, 2, 2]) == 2
    assert solution([1, 2, 2, 4, 3, 5, 6, 4, 2]) == 2
    assert solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3
    assert solution([1, 2, 1, 2, 2]) == 1
    assert solution([1]) == 0
    assert solution([1, 2]) == 0
    assert solution([1, 2, 1]) == 1
    assert solution([1, 1, 2, 1, 1, 2, 1, 2, 1]) == 3