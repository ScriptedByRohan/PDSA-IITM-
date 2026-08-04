#combination sort 
def first_letter(s):
    return s[0]

def second_letter(s):
    return (s[0], -int(s[1:])) #-int so the values are in descending order like 12 < 23 < 34 is ascending using - chages it -34<-23<-12

def combination_sort(str):
    l1 = sorted(str,key = first_letter)
    l2 = sorted(l1,key = second_letter )
    return(l1,l2)

#another way 
def combination_anotherway(str):
    l1 = sorted(str,key = lambda x : x[0])
    l2 = sorted(l1,key = lambda x: (x[0],-int(x[1:])))
    return (l1,l2)

sample_input = ["d34", "g54", "d12", "b87", "g1", "c65", "g40", "g5", "d77"]
L1, L2 = combination_anotherway(sample_input)

print("L1:", ", ".join(L1))
print("L2:", ", ".join(L2))

