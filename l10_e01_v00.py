# Problem: Consider n coins aligned in a row. Each coin is showing heads at the beginning.
# 1 2 3 4 5 6 7 8 9 10
# Then, n people turn over corresponding coins as follows. Person i reverses coins with numbers
# that are multiples of i. That is, person i flips coins i, 2 · i, 3 · i, . . . until no more appropriate
# coins remain. The goal is to count the number of coins showing tails.
# Result in this case would be: 1 (flipped) 2 3 4 (flipped) 5 6 7 8 9 (flipped) 10.


def solution(n):
    coins = [0] * (n+1)
    flip_cnt = 0

    for i in range(1, n):  # O(n)
        k = i
        while k <= n:  # O(sqrt(n))
            if k % i == 0:
                coins[k] = (coins[k] + 1) % 2
                k += i
        flip_cnt += coins[i]

    return flip_cnt


if __name__ == "__main__":
    assert solution(10) == 3
