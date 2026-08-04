#combination sort 
def first_letter(s):
    return s[0]

def second_letter(s):
    return (s[0], -int(s[1:])) #-int so the values are in descending order like 12 < 23 < 34 is ascending using - chages it -34<-23<-12

def combination_sort(str):
    l1 = sorted(str,key = first_letter)
    l2 = sorted(l1,key = second_letter )
    return(l1,l2)

