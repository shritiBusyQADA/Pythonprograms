#Lists
i = [1,2,3]
print(i)

i.insert(1,"hello")
print(i)
#Nested Lists
i1 = ['hi', 1,[1,2]]
print(i1)

nest = [1,2,3,[4,5,['target', 'source']]]
print(nest[3])

print(nest[3][2])

print(nest[3][2][0])

nest.remove(3)
print(nest)
nest.clear()
print(nest)

my_list = ['a', 'b', 'c']
print(my_list)
my_list.append('d')
print(my_list)

print(my_list[3])

print(my_list[1:3])
print(my_list[1:])

print(my_list[:2])

my_list[0] = 'New'
print(my_list)
