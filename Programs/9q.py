def extract_rear_elemets(my_tuple):
    return [string[-1]for string in my_tuple]

my_tuple=("python","learn","includehelp")
result=extract_rear_elemets(my_tuple)
print(result)