# An Armstrong number (also known as a narcissistic number) is a number that equals the sum of its own digits raised to the power of the number of digits.

# Write a function that, given two integers A and B, returns the count of Armstrong numbers within the range [A, B] (inclusive).

# For example:
# - 153 is an Armstrong number because: 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
# - 370 is an Armstrong number because: 3³ + 7³ + 0³ = 27 + 343 + 0 = 370
# - 407 is an Armstrong number because: 4³ + 0³ + 7³ = 64 + 0 + 343 = 407

# Input:
# - Integer A: the start of the range
# - Integer B: the end of the range

# Output:
# - Return the count of Armstrong numbers in range [A, B]

# Constraints:
# - 1 ≤ A ≤ B ≤ 1,000,000
# - B - A ≤ 100,000

# Example:
# Input: A = 100, B = 400
# Output: 2 (153 and 370 are the only Armstrong numbers in this range)

# Performance requirements:
# Expected time complexity: O(N * log N), where N is the range size (B - A)
# Expected space complexity: O(1)

def get_digits(num):
    digits = []

    while num:
        digits.append(num % 10)
        num //= 10

    return digits if digits else [0]


def solution(A, B):
    cnt = 0

    for i in range(A, B+1):
        if i < 10:
            cnt += 1
            print(i)
        else:
            digits = get_digits(i)
            digits_len = len(digits)
            s = 0
            while len(digits):
                d = int(digits.pop())
                s += d ** digits_len
            if s == i:
                cnt += 1
                print(i)
    return cnt


if __name__ == "__main__":
    assert solution(100, 400) == 3
    assert solution(1, 10) == 9
    assert solution(1000, 9000) == 2
    assert solution(50000, 100000) == 3
