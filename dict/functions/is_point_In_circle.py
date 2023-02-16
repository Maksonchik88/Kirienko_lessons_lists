def IsPointInCircle(x: float, y: float, a: float, b: float, r: float) -> bool:
    return (x - a) ** 2 + (y - b) ** 2 <= r ** 2


print('YES' if IsPointInCircle(0.5, 0.5, 0, 0, 1) else 'NO')
