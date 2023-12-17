#1
file = open("data.txt", 'w')

file.write("100.12\n")
file.write("111.23\n")

file.close()

#2
file = open("data.txt", 'w')
file.write("100.12")
file.close()