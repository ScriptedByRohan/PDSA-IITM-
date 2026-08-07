import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest(points_x, points_y):
    n = len(points_x)

    # Base case
    if n <= 3:
        d = float('inf')
        for i in range(n):
            for j in range(i + 1, n):
                d = min(d, distance(points_x[i], points_x[j]))
        return d

    # Divide
    mid = n // 2
    mid_point = points_x[mid]

    left_x = points_x[:mid]
    right_x = points_x[mid:]

    left_y = []
    right_y = []

    for p in points_y:
        if p[0] < mid_point[0]:
            left_y.append(p)
        else:
            right_y.append(p)

    # Find minimum distance in left and right
    dl = closest(left_x, left_y)
    dr = closest(right_x, right_y)

    d = min(dl, dr)

    # Create strip
    strip = []
    for p in points_y:
        if abs(p[0] - mid_point[0]) < d:
            strip.append(p)

    # Check strip
    m = len(strip)
    for i in range(m):
        j = i + 1
        while j < m and (strip[j][1] - strip[i][1]) < d:
            d = min(d, distance(strip[i], strip[j]))
            j += 1

    return d

def minDistance(Points):
    points_x = sorted(Points, key=lambda p: p[0])  # Sort by x
    points_y = sorted(Points, key=lambda p: p[1])  # Sort by y
    return round(closest(points_x, points_y), 2)