my_list = [('apple', 3), ('banana', 2), ('cherry', 1)]
my_list.sort(key=lambda x: x[1])
print(my_list)  # [('cherry', 1), ('banana', 2), ('apple', 3)]
