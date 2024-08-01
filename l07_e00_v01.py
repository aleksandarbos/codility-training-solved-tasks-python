# Problem: You are given a zero-indexed array A consisting of n integers: a0, a1, . . . , an−1.
# Array A represents a scenario in a grocery store, and contains only 0s and/or 1s:
# • 0 represents the action of a new person joining the line in the grocery store,
# • 1 represents the action of the person at the front of the queue being served and leaving
# the line.
# The goal is to count the minimum number of people who should have been in the line before
# the above scenario, so that the scenario is possible (it is not possible to serve a person if the
# line is empty).

# time complexity: O(n)
# space complexity: O(1)
def solution_01(A):
    missing_people_cnt = 0
    people_cnt = 0

    for op in A:  # O(n)
        if op == 0:
            people_cnt += 1
        elif op == 1:
            if people_cnt <= 0:
                missing_people_cnt += 1
            else:
                people_cnt -= 1

    return missing_people_cnt


# time complexity: O(n)
# space complexity: O(n)
def solution(A):
    N = len(A)
    queue = [0] * N
    head, tail = 0, 0

    def push(x):  # O(1)
        nonlocal tail
        tail = (tail + 1) % N
        queue[tail] = x

    def pop():  # O(1)
        nonlocal head
        head = (head + 1) % N
        return queue[head]

    def size():  # O(1)
        return (tail - head + N) % N

    def empty():  # O(1)
        return head == tail

    missing_people_cnt = 0
    for op in A:  # O(n)
        if op == 0:  # join
            push(op)
        elif op == 1:  # pop
            if empty():
                missing_people_cnt += 1
            else:
                pop()

    return missing_people_cnt


if __name__ == "__main__":
    assert solution([0, 0, 1, 1, 1, 1, 0, 0, 1]) == 2
    assert solution([1, 1, 1, 1]) == 4
    assert solution([0, 0, 0, 0]) == 0
    assert solution([0, 1, 1, 1, 0, 1, 1, 1]) == 4
    assert solution([0, 0, 1, 0, 0, 1, 0, 0]) == 0

    assert solution_01([0, 0, 1, 1, 1, 1, 0, 0, 1]) == 2
    assert solution_01([1, 1, 1, 1]) == 4
    assert solution_01([0, 0, 0, 0]) == 0
    assert solution_01([0, 1, 1, 1, 0, 1, 1, 1]) == 4
    assert solution_01([0, 0, 1, 0, 0, 1, 0, 0]) == 0
