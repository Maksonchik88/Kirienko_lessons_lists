def distance(x1, y1, x2, y2) -> float:
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


print(distance(0, 0, 1, 1))