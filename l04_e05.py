# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].


# time complexity: 4 *O(n) => O(n)
# space complexity: 2*O(n) => O(n)
def solution(A):
    expected_nums = set(range(1, len(A)+1)) # O(n)
    actual_nums = set(A) # O(n)
    diff = expected_nums.difference(actual_nums) # O(n)
    min_val = float('inf')

    if len(diff):
        for num in diff:
            if 0 <= num < min_val:
                min_val = num
        return min_val
    else:
        max_val = max(actual_nums) # O(n)
        if max_val > 0:
            return max_val + 1
        else:
            return 1

if __name__ == "__main__":
    assert solution([1, 3, 6, 4, 1, 2]) == 5
    assert solution([-1]) == 1
    assert solution([0]) == 1
    assert solution([1]) == 2
    assert solution([0, 2]) == 1
    assert solution([1, -10, 20, -1, -10, 3]) == 2
    assert solution([0, -2]) == 1
    assert solution([1, 2, 3, 4, 5]) == 6
    assert solution([-1, 0, 1, 2]) == 3
