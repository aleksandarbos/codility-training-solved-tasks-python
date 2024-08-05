# An integer N is given, representing the area of some rectangle.

# The area of a rectangle whose sides are of length A and B is A * B, and the perimeter is 2 * (A + B).

# The goal is to find the minimal perimeter of any rectangle whose area equals N. The sides of this rectangle should be only integers.

# For example, given integer N = 30, rectangles of area 30 are:

# (1, 30), with a perimeter of 62,
# (2, 15), with a perimeter of 34,
# (3, 10), with a perimeter of 26,
# (5, 6), with a perimeter of 22.
# Write a function:

# def solution(N)

# that, given an integer N, returns the minimal perimeter of any rectangle whose area is exactly equal to N.

# For example, given an integer N = 30, the function should return 22, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..1,000,000,000].

# time complexity: O(sqrt(N))
# space complexity: O(1)
def solution(N):
    i = 1

    if N == 1:
        return 2 * (1 + 1)

    min_perimeter = float('inf')
    while i * i <= N:  # O(sqrt(N))
        if N % i == 0:
            A = N // i  # divisor
            B = i  # and it's symmetric pair
            perimeter = 2 * (A + B)
            min_perimeter = min(min_perimeter, perimeter)
        i += 1

    return min_perimeter


if __name__ == "__main__":
    assert solution(36) == 24
    assert solution(30) == 22
    assert solution(1) == 4
    assert solution(2) == 6
    assert solution(6) == 10
