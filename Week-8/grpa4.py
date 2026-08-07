def MoM7Pos(arr):
    # Divide into groups of 7
    groups = [arr[i:i+7] for i in range(0, len(arr), 7)]

    # Find median of each group
    medians = []
    for group in groups:
        group.sort()
        medians.append(group[3])   # 4th element is the median of 7

    # Find the UPPER median of the medians
    medians.sort()
    M = medians[len(medians)//2]

    # Sort original array
    sorted_arr = sorted(arr)

    # Return first occurrence of M
    for i in range(len(sorted_arr)):
        if sorted_arr[i] == M:
            return i