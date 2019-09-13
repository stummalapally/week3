l = [1, 2, 3, 4]

print(l[2])

nested = [[1,2,3,4], [4,5,56,8]]

#1 2 3 4
#4 5 56 8

print(nested[1][2])

nested[1][2]=44

print(nested)

nested[0] = [1,2,3]

print(nested)

print(nested[0][0:2])