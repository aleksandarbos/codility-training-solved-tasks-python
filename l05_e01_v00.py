# Problem: You are given a non-empty, zero-indexed array A of n (1 <= n <= 100 000) integers
# a0, a1, . . . , an−1 (0 <= ai <= 1 000). This array represents number of mushrooms growing on the
# consecutive spots along a road. You are also given integers k and m (0 <= k, m < n).
# A mushroom picker is at spot number k on the road and should perform m moves. In
# one move she moves to an adjacent spot. She collects all the mushrooms growing on spots
# she visits. The goal is to calculate the maximum number of mushrooms that the mushroom
# picker can collect in m moves.
# For example, consider array A such that:
# 2 3 7 5  1  3 9
# 0 1 2 3 [4] 5 6
# The mushroom picker starts at spot k = 4 and should perform m = 6 moves. She might
# move to spots 3, 2, 3, 4, 5, 6 and thereby collect 1 + 5 + 7 + 3 + 9 = 25 mushrooms. This is the
# maximal number of mushrooms she can collect.


# TODO
def solution(A, k, m):
    N = len(A)
    max_mushrooms = 0
    walk = set()

    for i in range(N):  # O(n)
        pass


if __name__ == "__main__":
    assert solution([2, 3, 7, 1, 3, 9], 4, 6) == 25
