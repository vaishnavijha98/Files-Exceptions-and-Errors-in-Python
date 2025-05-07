Line = input("Enter text to write to the file: ")

file = open("output.txt", "w")
file.write(Line)
print("Data is successfully written to file 'output.txt'.")

Line1 = input("Enter additional text to append: ")
file.write("\n" + Line1)
print("Data is successfully appended.")
file.close()

file = open("output.txt", "r")
reading_file = file.read()
print("Final content of output.txt: ", reading_file)
file.close()

