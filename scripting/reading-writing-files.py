# Reading a File
f = open('file.txt', 'r')
file_data = f.read()
f.close()

print(file_data)


# Writing to a File
f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()


# With Python provides a special syntax that auto-closes a file for you once you're finished using it.

with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()