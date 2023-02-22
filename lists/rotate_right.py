from typing import List


def rotate(st: list) -> List:
    return st[-1:] + st[:-1]


print(*rotate(input().split()))
