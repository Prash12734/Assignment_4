# Write and Append Data to a File

a = input("Enter text to write to the file: ")
print("Data successfully written to output.txt ")

file1 = open('output.txt' , 'w')
appending_file= file1.write(a + '\n')
file1.close()

b = input("Enter additional text to append: ")
print("Data successfully append.")

file1 = open('output.txt' , 'a')
additional_data = file1.write(b)
file1.close()
print("Final content of output.txt :")

file1 = open('output.txt' , 'r')
reading_file = file1.read()
print(reading_file)
file1.close()
