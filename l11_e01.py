# You are given an array A consisting of N integers.

# For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

# For example, consider integer N = 5 and array A such that:

#     A[0] = 3
#     A[1] = 1
#     A[2] = 2
#     A[3] = 3
#     A[4] = 6
# For the following elements:

# A[0] = 3, the non-divisors are: 2, 6,
# A[1] = 1, the non-divisors are: 3, 2, 3, 6,
# A[2] = 2, the non-divisors are: 3, 3, 6,
# A[3] = 3, the non-divisors are: 2, 6,
# A[4] = 6, there aren't any non-divisors.
# Write a function:

# def solution(A)

# that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

# Result array should be returned as an array of integers.

# For example, given:

#     A[0] = 3
#     A[1] = 1
#     A[2] = 2
#     A[3] = 3
#     A[4] = 6
# the function should return [2, 4, 3, 2, 0], as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..50,000];
# each element of array A is an integer within the range [1..2 * N].

# time complexity: O(n^2)
# space complexity: O(n)
def solution_01(A):
    N = len(A)
    result = [0] * N

    for i in range(N):
        for j in range(N):
            if i != j:
                if A[i] % A[j] != 0:
                    result[i] += 1

    return result


# time complexity: O(sqrt(n))
def divisors(n):
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            yield i
            if n // i != i:
                yield n // i


# time complexity: O(n*sqrt(n))
# space complexity: 2*O(n) => O(n)
def solution_02(A):
    N = len(A)
    result = [0] * (N)

    max_el = max(A)  # O(p), p = max(A)
    cnt_array = [0] * (max_el + 1)
    for num in A:  # O(n)
        cnt_array[num] += 1

    cache = {}  # in a case of big repeated numbers
    for idx, num in enumerate(A):  # O(n)
        if not num in cache:
            divisors_cnt = 0
            for divisor in divisors(num):  # O(sqrt(num))
                divisors_cnt += cnt_array[divisor]
            result[idx] = N - divisors_cnt
            cache[num] = N - divisors_cnt
        else:
            result[idx] = cache[num]
    return result


if __name__ == "__main__":
    assert solution_01([3, 1, 2, 3, 6]) == [2, 4, 3, 2, 0]
    assert solution_02([3, 1, 2, 3, 6]) == [2, 4, 3, 2, 0]
    assert solution_02([12, 4, 1, 1, 3, 5]) == [1, 3, 4, 4, 3, 3]
    assert solution_02([5]) == [0]
    assert solution_02([5, 10]) == [1, 0]
    assert solution_02([5, 6]) == [1, 1]
    assert solution_02([5, 5]) == [0, 0]
    assert solution_02([1, 1]) == [0, 0]
    assert solution_02([1, 2]) == [1, 0]
    assert solution_02([1, 1, 1, 1]) == [0, 0, 0, 0]
    assert solution_02([2, 2, 2]) == [0, 0, 0]
    assert solution_02([10*10**4, 10*10**4, 10*10**4, 10 *
                       10**4, 10*10**4]) == [0, 0, 0, 0, 0]
