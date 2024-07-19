# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].

# time complexity: O(log*n)
# space complexity: O(log*n)
def solution(N):
    bin_n = format(N, 'b') # O(log*n)
    return max_zeros_gap_len(bin_n)

def max_zeros_gap_len(bin_n):
    gap_start = None
    max_gap_len = 0

    for i, char in enumerate(bin_n): # O(log*n)
        if char == "1":
            if gap_start is not None:
                max_gap_len = max(max_gap_len, i - gap_start - 1) # O(1)
            gap_start = i
    return max_gap_len

if __name__ == "__main__":
    assert max_zeros_gap_len("") == 0
    assert max_zeros_gap_len("0") == 0
    assert max_zeros_gap_len("1") == 0
    assert max_zeros_gap_len("11") == 0
    assert max_zeros_gap_len("00000") == 0
    assert max_zeros_gap_len("1000000") == 0
    assert max_zeros_gap_len("11111") == 0
    assert max_zeros_gap_len("1000001") == 5
    assert max_zeros_gap_len("1011000") == 1
    assert max_zeros_gap_len("1010010") == 2
    assert max_zeros_gap_len("0000001") == 0
    assert max_zeros_gap_len("00000101") == 1
