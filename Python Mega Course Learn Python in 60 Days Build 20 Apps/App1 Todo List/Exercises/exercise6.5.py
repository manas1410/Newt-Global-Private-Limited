file = open("members.txt","r")
read_file = file.readlines()
file.close()
while True:
    new_member = input("Add new Member: ") + "\n"
    file = open("members.txt", "r")
    read_file = file.readlines()
    file.close()

    read_file.append(new_member)

    file = open("members.txt", "w")
    file.writelines(read_file)
    file.close()