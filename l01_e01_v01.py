# Count the number of zeros in binary representation of int N.


def solution(N):
    bin_n = format(N, 'b') # O(log*n)
    bin_arr = [int(n) for n in bin_n] # O(log*n), bc there are log*n items for input N

    # print(f'N: {N}, bin_arr: {bin_arr}')

    return len(bin_arr) - sum(bin_arr)


if __name__ == "__main__":
    assert solution(7) == 0
    assert solution(1) == 0
    assert solution(32) == 5
    assert solution(20) == 3
