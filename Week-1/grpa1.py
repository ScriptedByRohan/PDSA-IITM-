#Given a function min_diff(L,P). L is the list of the numbers and P is a number less than the size of the list L .

# Task
# 1. pick p diff element from list l where the difference between the maximum value and the minimum value in selected elements is minimum compared to other differences in possible subset of p elements. The function returns this minimum difference value.


def min_diff(l,p):
    l.sort()
    minimum_difference = float('inf') #inf is infinity . float because infinity number is not integer we assign a largest value to the minimum 
    for i in range(0,len(l)- p + 1):
        curr_diff = l[i+p-1] - l[i] # l[i+p-1] is the largest 
        if curr_diff < minimum_difference:
            minimum_difference = curr_diff
    return minimum_difference

l = [1,3,2,4,6,3,10,12]
p = 3
print(min_diff(l,p))
