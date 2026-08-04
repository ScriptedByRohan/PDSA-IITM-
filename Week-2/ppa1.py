def BinarySearchIndexAndComparison(l,k):
    left = 0
    right = len(l) - 1
    no_of_comparisons = 0

    while left <= right:
        mid = (left+right) // 2
        no_of_comparisons += 1
        if l[mid]  == k:
            return(True,no_of_comparisons)
        elif l[mid] > k:
            right = mid - 1
        else:
            left = mid + 1
        
    return(False, no_of_comparisons)

L = [2, 6, 8, 11, 17, 23, 33, 44, 46, 50, 65]

print(BinarySearchIndexAndComparison(L, 11))  # Output: (True, 3)
print(BinarySearchIndexAndComparison(L, 23))  # Output: (True, 1)
print(BinarySearchIndexAndComparison(L, 100))  # Output: (False, 4)