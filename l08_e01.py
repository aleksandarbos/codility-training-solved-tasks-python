# An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

# For example, consider array A such that

#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

# Write a function

# def solution(A)

# that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

# For example, given array A such that

#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# the function may return 0, 2, 4, 6 or 7, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

def get_leader_candidate(A):
    N = len(A)

    size = 0
    value = -1

    for i in range(N):
        if size == 0:
            value = A[i]
            size += 1
        else:
            if A[i] != value:
                size -= 1
            else:
                size += 1

    return value if size > 0 else -1

# time complexity: O(n)
# space complexity: O(1)
def solution(A):
    N = len(A)
    dominator_candidate = get_leader_candidate(A)  # O(n)

    cnt = 0
    last_occurrence_idx = -1
    for i in range(N):  # O(n)
        if A[i] == dominator_candidate:
            cnt += 1
            last_occurrence_idx = i

    return last_occurrence_idx if cnt > N//2 else -1
