# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

# Your goal is to find that missing element.

# Write a function:

# def solution(A)

# that, given an array A, returns the value of the missing element.

# For example, given array A such that:

#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].

# time complexity: O(n) + O(n) => O(n)
# space complexity: O(1)
def solution(A):
    if not A: # A is [], therefore it's missing 1
        return 1
    N = len(A)

    xor_all = 0
    for i in range(1, (N+1)+1): # 2nd arg of range isn't included, therefore +1
        xor_all ^= i

    xor_arr = 0
    for num in A:
        xor_arr ^= num

    return xor_arr ^ xor_all

# time complexity: O(n)
# space complexity: O(1)
def solution_02(A):
    N = len(A)
    total_sum = (N + 1) * (N + 2) // 2
    array_sum = sum(A) # O(n)
    missing_element = total_sum - array_sum
    return missing_element

if __name__ == "__main__":
    assert solution([1, 2, 4, 5]), 3
    assert solution([1, 2, 4, 5]), 3
    assert solution([]), 1
    assert solution([2, 3, 1, 5]), 4

    print(solution([3,4,6,1,5]))
