try:
    file1 = open('sample.txt', 'r')
    reading = file1.read()
    print(reading)
    file1.close()


except FileNotFoundError:
    print("The file 'sample.txt' was not found")