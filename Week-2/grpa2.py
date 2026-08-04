#a list is given which is sorted find the max but list rotates n unknown time 

def Largest_element(l):
    left = 0
    right = len(l) - 1

    if l[left] <= l[right]:
        return l[right]
    
    while left < right:
        if left - right == 1:
            return max(l[left],l[right])
        
        mid = (left + right) // 2
        if l[mid] > l[right]:
            left = mid
        else:
            right = mid-1
    return l[left]

sample_input = [7, 8, 2, 4, 5]
print(Largest_element(sample_input))            
