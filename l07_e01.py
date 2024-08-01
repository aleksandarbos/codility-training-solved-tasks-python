
# A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.

# Write a function:

# def solution(S)

# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

# For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..200,000];
# string S is made only of the following characters: '(', '{', '[', ']', '}' and/or ')'.


# time complexity: O(n)
# space complexity: O(n)
def solution(S):
    N = len(S)

    stack = [0] * N
    size = 0

    endings_map = {'}': '{', ']': '[', ')': '('}

    def push(x):
        nonlocal size
        stack[size] = x
        size += 1

    def pop():
        nonlocal size
        size -= 1
        return stack[size]

    for c in S:
        if c in endings_map:
            if stack[size-1] != endings_map[c]:
                return 0
            pop()
        else:
            push(c)

    return 1 if size == 0 else 0


if __name__ == "__main__":
    assert solution(')(') == 0
    assert solution(')()') == 0
    assert solution('}') == 0
    assert solution('({]})') == 0
    assert solution('{[{{[]}}]}') == 1
    assert solution('}}}}') == 0
