immutable_var = (1, 2, 3, 'roma', tuple)
print(immutable_var)
#immutable_var[0] = 8

mutable_list = [1, 2, 3, 'roma', len]
mutable_list[0] = ('world')
mutable_list[1] = (8)
mutable_list[2] = ('good')
print(mutable_list)