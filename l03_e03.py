# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.

# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].

# The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|

# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.

# For example, consider array A such that:

#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# We can split this tape in four places:

# P = 1, difference = |3 − 10| = 7
# P = 2, difference = |4 − 9| = 5
# P = 3, difference = |6 − 7| = 1
# P = 4, difference = |10 − 3| = 7
# Write a function:

# def solution(A)

# that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.

# For example, given:

#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−1,000..1,000].


# time complexity:  3* O(n) => O(n)
# space complexity: 2* O(n) => O(n)
def solution_01(A):
    import math
    sum_dict = {}
    sum_a = 0
    sum_dict_reverse = {}
    sum_a_reversed = 0
    min_diff = math.inf

    for i, num in enumerate(A): # O(n)
        sum_a += num
        sum_dict[i] = sum_a if not i in sum_dict else sum_dict[i] + sum_a

    for i in range(len(A)-1, -1, -1): # O(n)
        num = A[i]
        sum_a_reversed += num
        sum_dict_reverse[i] = sum_a_reversed if not i in sum_dict_reverse else sum_dict_reverse[i] + sum_a_reversed

    for i in range(len(A)-1): # O(n-1)
        diff_val = abs(sum_dict[i] - sum_dict_reverse[i+1])
        if diff_val < min_diff:
            min_diff = diff_val

    return min_diff


# time complexity: O(n)
# space complexity: O(1)

def solution(A):
    total_sum = sum(A) # O(n)
    sum_left = 0
    min_diff = float('inf')

    for i in range(1, len(A)): # O(n)
        sum_left += A[i-1]
        sum_right = total_sum - sum_left

        p = abs(sum_left - sum_right)
        if p < min_diff:
            min_diff = p

    return min_diff

if __name__ == "__main__":
    assert solution_01([3, 1, 2, 4, 3]) == 1
    assert solution([3, 1, 2, 4, 3]) == 1
