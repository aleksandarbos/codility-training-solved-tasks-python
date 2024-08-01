# We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

# We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

# The figure below shows discs drawn for N = 6 and A as follows:

#   A[0] = 1
#   A[1] = 5
#   A[2] = 2
#   A[3] = 1
#   A[4] = 4
#   A[5] = 0


# There are eleven (unordered) pairs of discs that intersect, namely:

# discs 1 and 4 intersect, and both intersect with all the other discs;
# disc 2 also intersects with discs 0 and 3.
# Write a function:

# def solution(A)

# that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

# Given array A shown above, the function should return 11, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [0..2,147,483,647].

# time complexity: O(n*logn)
def solution(A):
    N = len(A)
    start_points = []
    end_points = []

    for i in range(N):
        start_points.append(i - A[i])
        end_points.append(i + A[i])

    start_points.sort()
    end_points.sort()
    num_of_intersections = 0

    start_index = 0
    end_index = 0
    active_circles = 0

    while start_index < N:
        # keeps in sep arrays bc of constant time access
        if start_points[start_index] <= end_points[end_index]:
            num_of_intersections += active_circles
            if num_of_intersections > 10**7:
                return -1
            active_circles += 1
            start_index += 1
        else:
            active_circles -= 1
            end_index += 1

    return num_of_intersections


if __name__ == "__main__":
    assert solution([1, 5, 2, 1, 4, 0]) == 11
