# A non-empty array A consisting of N integers is given.

# The leader of this array is the value that occurs in more than half of the elements of A.

# An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# we can find two equi leaders:

# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count the number of equi leaders.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

# For example, given:

#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# the function should return 2, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].

def get_leader_candidate(A):
    N = len(A)

    size = 0
    value = -1
    for i in range(N):
        if size == 0:
            value = A[i]
            size += 1
        else:
            if value != A[i]:
                size -= 1
            else:
                size += 1

    return value if size > 0 else -1


# time complexity: O(n)
# space complexity: O(n) + O(n) => O(n)
def solution(A):
    N = len(A)
    leader = get_leader_candidate(A)  # O(n)
    result_cnt = 0

    if leader == -1:
        return 0

    total_count = sum(1 for i in A if i == leader)  # O(n)
    if total_count < N // 2:
        return 0  # not a real leader, only false candidate

    if len(A) == 1:
        return 0
    else:
        prefix_sum = [0] * N
        s = 0
        for i in range(N):  # O(n)
            if A[i] == leader:
                s += 1
            prefix_sum[i] = s

        total_dominators = prefix_sum[-1]
        for i in range(N):
            if i == N-1 and A[i] == leader:
                result_cnt += 1
            else:
                dominators_left = prefix_sum[i]
                dominators_right = total_dominators - dominators_left

                has_left_equi_leader = dominators_left > (i+1) // 2
                has_right_equi_leader = (
                    N-(i+1)) > 1 and dominators_right > (N-(i+1)) // 2

                if has_left_equi_leader and has_right_equi_leader:
                    result_cnt += 1

        return result_cnt


if __name__ == "__main__":
    assert solution([1, 2, 3, 4, 5]) == 0
    assert solution([4, 3, 4, 4, 4, 2]) == 2
    assert solution([5]) == 0
    assert solution([5, 5]) == 1
    assert solution([1, 1]) == 1
    assert solution([1, 1, 5]) == 0
    assert solution([2, 2, 4, 2]) == 2
    assert solution([3, 3, 3, 3]) == 3
    assert solution([-5, 4, 2, -5, -5, 6, -5, -5]) == 3
    assert solution([1, 1, 2, 2, 3, 3]) == 0
    assert solution([1]) == 0
    assert solution([1, 1]) == 1
    assert solution([1, 2]) == 0
