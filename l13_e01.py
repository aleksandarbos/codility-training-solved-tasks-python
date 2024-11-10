# The Fibonacci sequence is defined using the following recursive formula:

#     F(0) = 0
#     F(1) = 1
#     F(M) = F(M - 1) + F(M - 2) if M >= 2
# A small frog wants to get to the other side of a river. The frog is initially located at one bank of the river (position −1) and wants to get to the other bank (position N). The frog can jump over any distance F(K), where F(K) is the K-th Fibonacci number. Luckily, there are many leaves on the river, and the frog can jump between the leaves, but only in the direction of the bank at position N.

# The leaves on the river are represented in an array A consisting of N integers. Consecutive elements of array A represent consecutive positions from 0 to N − 1 on the river. Array A contains only 0s and/or 1s:

# 0 represents a position without a leaf;
# 1 represents a position containing a leaf.
# The goal is to count the minimum number of jumps in which the frog can get to the other side of the river (from position −1 to position N). The frog can jump between positions −1 and N (the banks of the river) and every position containing a leaf.

# For example, consider array A such that:

#     A[0] = 0
#     A[1] = 0
#     A[2] = 0
#     A[3] = 1
#     A[4] = 1
#     A[5] = 0
#     A[6] = 1
#     A[7] = 0
#     A[8] = 0
#     A[9] = 0
#     A[10] = 0
# The frog can make three jumps of length F(5) = 5, F(3) = 2 and F(5) = 5.

# Write a function:

# def solution(A)

# that, given an array A consisting of N integers, returns the minimum number of jumps by which the frog can get to the other side of the river. If the frog cannot reach the other side of the river, the function should return −1.

# For example, given:

#     A[0] = 0
#     A[1] = 0
#     A[2] = 0
#     A[3] = 1
#     A[4] = 1
#     A[5] = 0
#     A[6] = 1
#     A[7] = 0
#     A[8] = 0
#     A[9] = 0
#     A[10] = 0
# the function should return 3, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer that can have one of the following values: 0, 1.

def fib_array(N):  # O(n)
    arr = [0] * (N+2)
    arr[1] = 1
    for i in range(2, N+1):
        arr[i] = arr[i-1] + arr[i-2]
    return arr


def solution(A):
    N = len(A)

    if not N:
        return 1

    fib_a = fib_array(max(10, N))  # O(n)
    fib_set = set(fib_a)  # O(n)
    fib_set.remove(0)  # remove 0 distance
    min_jumps = -1
    pos = -1

    if N - pos in fib_set:  # jump whole thing
        return 1

    for i in range(N):  # O(N^2) => N*(N-1)/2
        pos = -1
        if A[i] == 1:
            jumps = 0
            jmp = i + 1 if pos == -1 else i - pos
            if not jmp in fib_set:
                continue
            jumps += 1
            pos = i
            # print(f'jump: {pos}', end=' ')
            if N - i in fib_set:
                min_jumps = jumps + 1 if min_jumps == - \
                    1 else min(jumps+1, min_jumps)
                # print(f'jump: {N}')
                continue
            for j in range(i+1, N):
                if A[j] == 1:
                    jmp = j - pos
                    if not jmp in fib_set:
                        continue
                    jumps += 1
                    pos = j
                    # print(f'jump: {pos}', end=' ')
                    if N - j in fib_set:
                        min_jumps = jumps + 1 if min_jumps == - \
                            1 else min(jumps+1, min_jumps)
                        # print(f'jump: {N}')
                        break
    return min_jumps


if __name__ == "__main__":
    assert solution([0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]) == 3

    assert solution([0, 0, 0, 0, 0, 0, 0]) == 1  # jump over whole thing
    assert solution([0, 0, 0, 0, 0, 0, 0, 0]) == -1  # can't jump over

    assert solution([0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 2
    assert solution([0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) == 2

    assert solution([1, 1, 1, 1, 1, 0, 0, 0, 0]
                    ) == 2  # skip first n, use latter

    assert solution([0, 0, 1, 0, 0, 0, 1, 1, 1, 1]
                    ) == 2  # skip last n, use latter

    assert solution([]) == 1
    assert solution([0]) == 1
    assert solution([0, 0]) == 1
    assert solution([0, 0, 0]) == -1
    assert solution([1, 1, 0, 1, 1, 0, 0]) == 1
    assert solution([1, 0, 1, 1, 0, 1]) == 3
    assert solution([1, 1, 1, 0, 1, 0, 1]) == 1
