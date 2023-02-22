from typing import List


def rotate(st: list, step=1) -> List:
    return st[-step:] + st[:-step]


print(*rotate(input().split()))
