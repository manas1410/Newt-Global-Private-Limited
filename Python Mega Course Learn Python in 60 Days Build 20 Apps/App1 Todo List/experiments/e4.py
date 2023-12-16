#1 - Importance of types
a = int(input("Enter the Number: "))
print(a * 10)

b = input("Enter the Name: ")
print(b * 10)

#2 - Importance of Types
c = float("120.90")
print(c)

d = str(c)
print(d)

#3 - List Indexing
my_list = ['a','b','c']
print(my_list[1])
print(type(my_list), type(my_list[2]))

my_list.__setitem__(1, 'd')
print(my_list)

my_list[1] = 'e'
print(my_list)

print(my_list.__getitem__(2))
print(my_list[2])