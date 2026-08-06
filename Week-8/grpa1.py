def findOccOf(L, x):
    # Find first occurrence
    low = 0
    high = len(L) - 1
    first = None

    while low <= high:
        mid = (low + high) // 2

        if L[mid] == x:
            first = mid
            high = mid - 1      # Continue searching on the left
        elif L[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    # Find last occurrence
    low = 0
    high = len(L) - 1
    last = None

    while low <= high:
        mid = (low + high) // 2

        if L[mid] == x:
            last = mid
            low = mid + 1       # Continue searching on the right
        elif L[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return (first, last)

print(findOccOf((3,3,5,5,5,5,6,6,6,6,6,6,9,9)
,5))