import array as ar

n = ar.array('i',[23,45,12,45,67])
n1 = ar.array('i',[23,34,56])
#n2 = ar.array('b',['e','t','u'])

#print(n2)
print("to append elements to array")
n.append(5)

print(n)

n.extend([1,2,3])

print(n)

print("concat")
print(n+n1)

print("delete elements")
print(n)
del n[1] # delete using index
print("after del")
print(n)

print("delete using value - remove()")
n.remove(67)
print(n)

print("pop() using index")
print(n.pop(2))     
print("pop last element",n.pop())     
print(n)
