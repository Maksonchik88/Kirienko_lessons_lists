def IsPointInSquare(x: float, y: float) -> bool:
    return (abs(x) + abs(y)) <= 1


x, y = float(input()), float(input())
print('YES' if IsPointInSquare(x, y) else 'NO')
