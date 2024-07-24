# Problem: Count of Specific Character in Substrings
# Given a string of lowercase English letters and multiple queries, each query asks for the number of occurrences of a specific character in a substring.

# Example:

# Input: s = "abacabad", char = 'a', queries = [(0, 4), (2, 6), (0, 7)]
# Output: [3, 3, 4]


def solution(S, char, Q):
    N = len(S)
    sums = [0] * (N+1)
    results = []

    for i in range(N):
        sums[i+1] = sums[i] + (1 if S[i] == char else 0)

    for start, end in Q:
        results.append(sums[end+1] - sums[start])

    return results


if __name__ == "__main__":
    assert solution("abacabad", 'a', [(0, 4), (2, 6), (0, 7)]) == [3, 3, 4]
