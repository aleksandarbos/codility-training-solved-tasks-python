# leader implementation
# https://codility.com/media/train/6-Leader.pdf

def get_leader_candidate_via_stack(A):
    N = len(A)
    stack = []
    for i in range(N):
        if not stack:
            stack.append(A[i])
        else:
            if A[i] != stack[-1]:
                stack.pop()
            else:
                stack.append(A[i])
    return stack[-1]


def get_leader_candidate_via_dict(A):
    N = len(A)
    cnt_map = {}
    for i in range(N):
        if not A[i] in cnt_map:
            cnt_map[A[i]] = 1
        else:
            cnt_map[A[i]] += 1

    max_leader_cnt = 0
    max_leader_key = None
    for key in cnt_map:
        if cnt_map[key] > max_leader_cnt:
            max_leader_cnt = cnt_map[key]
            max_leader_key = key

    return -1 if not max_leader_key else max_leader_key


def get_leader_candidate(A):
    N = len(A)

    leader_candidate = -1
    size = 0
    for i in range(0, N):
        if size == 0:
            leader_candidate = A[i]
            size += 1
        else:
            if leader_candidate != A[i]:
                size -= 1
            else:
                size += 1

    if size > 0:
        return leader_candidate
    else:
        return -1


def golden_leader(A):
    N = len(A)
    leader_candidate = get_leader_candidate(A)  # O(n)

    cnt = 0
    for i in range(N):  # O(n)
        if A[i] == leader_candidate:
            cnt += 1

    if cnt > N // 2:
        return leader_candidate
    else:
        return -1


if __name__ == "__main__":
    assert get_leader_candidate_via_stack([1, 2, 4, 4, 7, 7, 7]) == 7
    assert get_leader_candidate_via_stack([1, 2, 7, 7, 7, 4, 4]) == 7

    assert get_leader_candidate_via_dict([1, 2, 4, 4, 7, 7, 7]) == 7
    assert get_leader_candidate_via_dict([1, 2, 7, 7, 7, 4, 4]) == 7

    assert get_leader_candidate([1, 2, 7, 7, 7, 4, 4]) == 7
    assert golden_leader([1, 1, 2, 2, 3]) == -1
    assert golden_leader([5]) == 5
    assert golden_leader([5, 1]) == -1
    assert golden_leader([5, 1, 5]) == 5
