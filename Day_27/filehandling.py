# File handling- Most use full in web application testing.

# r= read file
# w- write file and create new file for write.
# a- open file and append data at the end of file.
# +- open file and updating (reading and writing)


## Write data into the text file.

file= open("C:\\Users\\hp\\PycharmProjects\\Python_basic-to-advance-for-QA\\Day_27\\myfile.txt", "w")

file.write("This is my first file to write \n")
file.write("This is my second file to write \n")
file.write("This is my third file to write \n")

file.close()
print("File handling program completed for: write")


## Reading data from myfile.text which created during write operation.

file=open("C:\\Users\\hp\\PycharmProjects\\Python_basic-to-advance-for-QA\\Day_27\\myfile.txt", "r")

print(file.read())
file.close()

print("Reading successfully done")


## Appending data into myfile.text.

file=open("C:\\Users\\hp\\PycharmProjects\\Python_basic-to-advance-for-QA\\Day_27\\myfile.txt", "a")

file.write("This is my fourth line to append in earlier file \n")
file.write("This is my fifth line to append in earlier file \n")

file.close()

print("Appned is succesfully done in earlier file")


## Write a integer data into a file.

file= open("C:\\Users\\hp\\PycharmProjects\\Python_basic-to-advance-for-QA\\Day_27\\myfile1.txt", "w")

l = [20, 30, 50, 70, 90, 3, 5, 6]

for items in l:
    file.write(str(items)+ "\n")

file.close()
print("Created new file and added integer data")
