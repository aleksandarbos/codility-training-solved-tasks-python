# max slice problem

def golden_max_slice(A):
    max_ending, max_slice = 0, 0
    for num in A:
        max_ending = max(0, num + max_ending)
        max_slice = max(max_ending, max_slice)
    return max_slice


def golden_max_slice_2(A):
    max_ending, max_slice = 0, 0
    p, q = 0, 0
    for i, num in enumerate(A):
        if num + max_ending <= 0:
            max_ending = 0
            p = 0
        else:
            max_ending = num + max_ending

        if max_ending > max_slice:
            max_slice = max_ending
            q = i
        max_slice = max(max_ending, max_slice)
    return max_slice, p, q


if __name__ == "__main__":
    assert golden_max_slice_2([3, -2, 5, -1]) == (6, 0, 2)
