# Problem: You are given an integer m (1 <= m <= 1 000 000) and two non-empty, zero-indexed
# arrays A and B of n integers, a0, a1, . . . , an−1 and b0, b1, . . . , bn−1 respectively (0 <= ai, bi <= m).
# The goal is to check whether there is a swap operation which can be performed on these
# arrays in such a way that the sum of elements in array A equals the sum of elements in
# array B after the swap. By swap operation we mean picking one element from array A and
# one element from array B and exchanging them.


"""
SumA + a - b = SumB - a + b
SumA - SumB = 2*a - 2*b
SumA - SumB = 2*(a-b) # that means that SumA - SumB has to be even num, bc any num * 2 <=> even num
target = (a-b) = (SumA - SumB) / 2
target = a - b
b = a + target
"""


# time complexity: O(n) + O(m) => O(n+m)
# space complexity: O(n+m)
def solution(A, B, m):
    N = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    cnt_a = [0] * (m+1)  # O(m)
    d = sum_a - sum_b

    for i in range(N):  # O(n)
        cnt_a[A[i]] += 1

    if d % 2 != 0:
        return False

    target = d // 2  # whole num division // bc we're looking for closest int

    for i in range(N):  # O(n)
        b = B[i]
        a = b - target
        if 0 <= a <= m and cnt_a[a] > 0:
            return True

    return False


if __name__ == "__main__":
    assert solution([1, 5, 4], [3, 2, 1],  5) == True
