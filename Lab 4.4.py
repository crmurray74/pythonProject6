path = input("Enter a directory path for the text file:")
filename = input("Enter filename: ")
#file structure will differ based on OS
file = open(path+"\\"+filename, "r")
for line in file:
    print(line)
file.close()