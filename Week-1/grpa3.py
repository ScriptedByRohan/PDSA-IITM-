#Given a list which will contain the odd one out we have to tell what is the data type of that odd data 
def odd(l):
    data_type = {}
    for i in l:
        current_data_type = type(i)
        if current_data_type in data_type:
            data_type[current_data_type] += 1
        else:
            data_type[current_data_type] = 1
    for data , count in data_type.items():
        if count == 1:
            return data.__name__

print(odd([1,2,3,56.5.5]))
