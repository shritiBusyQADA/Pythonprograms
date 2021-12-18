def times(var):
    return var*2

print(times(6))

#lambda
t = lambda var: var*2

print(t(6))

#map()
seq = [1,2,3,4,5]
print(list(map(times, seq)))


# map and lambda
t=lambda num: num*3
print(tuple(map(t, seq)))

# filter
print(list(filter(lambda num: num%2==0, seq)))


max = lambda a, b: (a*2, b*3)
print(max(1,3))
