try:
    file1 = open('sample.txt', 'r')
    reading_file = file1.readlines()
    for line in reading_file:
        print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
