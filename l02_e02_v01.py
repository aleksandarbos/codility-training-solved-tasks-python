# find missing number in a sequence from (1..N)

def solution(N):
    xor_n = 0
    xor_all = 0

    for i in range(1, len(N)+1):
        xor_all ^= i

    for num in N:
        xor_n ^= num

    return xor_all ^ xor_n


if __name__ == "__main__":
    assert solution([1,2,4,5]), 3
