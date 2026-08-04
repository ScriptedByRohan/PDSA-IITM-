#Given two sorted array need to sort each array 

def combination_sort(a,b):
    len_a = len(a)
    len_b = len(b)

    if len_b == 0:
        return
    
    for i in range(len_a):
        if a[i] > b[0]:
            swap(i,b,0)

            j = 0
            while j < len_b - 1 and b[j] > b[j+1]:
                swap(j,b,j+1)
                j += 1


