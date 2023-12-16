filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.', '-',1)
    print(filename)

filenames = ("1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt")
filename.append()
filename[1] = "Hello"
#these two lines will give error as tuples are immutable
