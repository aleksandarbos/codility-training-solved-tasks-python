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


def is_prime(num):  # O(sqrt(num))
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True


def divisors(N):  # O(sqrt(num))
    result = []
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            result.append(i)
            if i != N // i:
                result.append(N // i)
    return result


# time complexity: O(n)
# space complexity: O(n)
def solution(A):
    N = len(A)
    if N < 3:
        return 0

    peaks_sum_prefix = [0] * (N+1)
    s = 0
    for i in range(1, N+1):
        peaks_sum_prefix[i] += s
        if i < N and A[i-1] < A[i] > A[min(i+1, N-1)]:
            s += 1

    max_div_cnt = 0
    peaks_cnt = peaks_sum_prefix[-1]
    if peaks_cnt == 0:
        return 0
    elif is_prime(N) and peaks_cnt > 0:  # O(sqrt(N))
        return 1
    else:
        divs = divisors(N)
        for k in divs:  # O(sqrt(N))
            j = 0
            has_peaks = True
            while j*k+k < len(peaks_sum_prefix):
                start_idx, end_idx = j*k+1, j*k+k
                if peaks_sum_prefix[end_idx] - peaks_sum_prefix[start_idx] == 0:
                    has_peaks = False
                    break
                j += 1
            if has_peaks:
                max_div_cnt = max(max_div_cnt, j)

    return max_div_cnt


if __name__ == "__main__":
    assert solution([1, 2, 1, 2, 1, 2, 1, 2, 1]) == 3
    assert solution([1, 3, 2, 4]) == 1
    assert solution([1, 2, 2, 4, 3, 5, 6, 4, 2]) == 1
    assert solution([1, 1, 1, 1, 1]) == 0
    assert solution([1, 3, 1, 3, 1, 3, 1]) == 1
    assert solution([1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]) == 3
    assert solution([4, 4, 6, 1, 2, 3, 4]) == 1
    assert solution([4, 4, 4, 1, 2, 3, 4]) == 0
    assert solution([1, 2, 3, 4, 4, 4, 5, 6, 7]) == 0
    assert solution([1, 2, 1, 2, 1, 1, 2, 2]) == 1
    assert solution([1, 2, 1, 2, 2]) == 1
    assert solution([1]) == 0
    assert solution([1, 2]) == 0
    assert solution([1, 2, 1]) == 1
    assert solution([1, 1, 2, 1, 1, 2, 1, 2, 1]) == 3
    assert solution([1, 5, 3, 5, 3, 5, 3, 5, 3, 2, 6,
                    2, 4, 2, 6, 2, 8, 3, 5, 3, 1]) == 3
    assert solution([1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4,
                    1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1]) == 1
