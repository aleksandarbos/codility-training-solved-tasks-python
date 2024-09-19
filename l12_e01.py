# Two positive integers N and M are given. Integer N represents the number of chocolates arranged in a circle, numbered from 0 to N − 1.

# You start to eat the chocolates. After eating a chocolate you leave only a wrapper.

# You begin with eating chocolate number 0. Then you omit the next M − 1 chocolates or wrappers on the circle, and eat the following one.

# More precisely, if you ate chocolate number X, then you will next eat the chocolate with number (X + M) modulo N (remainder of division).

# You stop eating when you encounter an empty wrapper.

# For example, given integers N = 10 and M = 4. You will eat the following chocolates: 0, 4, 8, 2, 6.

# The goal is to count the number of chocolates that you will eat, following the above rules.

# Write a function:

#     def solution(N, M)

# that, given two positive integers N and M, returns the number of chocolates that you will eat.

# For example, given integers N = 10 and M = 4. the function should return 5, as explained above.

# Write an efficient algorithm for the following assumptions:

#         N and M are integers within the range [1..1,000,000,000].

# time complexity: O(N)
# def solution(N, M):
#     chocolates = [0] * N
#     choco_cnt = 0

#     i = 0
#     while chocolates[i] == 0:
#         chocolates[i] = 1
#         choco_cnt += 1
#         i = (i + M) % N

#     return choco_cnt

# time complexity: O(log(min(N,M)))
def gcd_bin(a, b, res=1):
    if a == b:
        return a * res
    elif a % 2 == 0 and b % 2 == 0:
        return gcd_bin(a // 2, b // 2, res * 2)
    elif a % 2 == 0:
        return gcd_bin(a // 2, b, res)
    elif b % 2 == 0:
        return gcd_bin(a, b // 2, res)
    elif a > b:
        return gcd_bin(a-b, b, res)
    else:
        return gcd_bin(a, b-a, res)


# time complexity: O(log(min(N, M)))
def lcm(a, b):
    return (a*b) // gcd_bin(a, b)


# time complexity: O(log(min(N, M)))
def solution(N, M):
    return lcm(N, M) // M
