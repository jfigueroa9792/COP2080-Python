from pathlib import Path
# reading files
# read(), readline(), readlines(); readons entire file, one line, all lines into one list
# with statement ensures proper file closure
# ex: with open(file_path, mode) as file_object: content = file_object.read()

'''
with open("sample.txt", "r") as file:
    content = file.read()
print(content)
'''

# readlines would return a list of strings from sample.txt

# writing to files
# use with statement with 'w' or 'a' mode to write
# write(), writelines(); writes a string, list of strings
# ex: with open("output.exe", 'w') as file: file.write("Hello, python!\n")

# if you wish to write bytes to a file, you can open binary mode.
# use ('rb','wb','ab') for non-text files

'''
with open("example.bin", 'wb') as fw:
    fw.write(b"This is binary data...")
with open("example.bin", 'rb') as f:
    print(f.read())
'''

#################################################################################
# create text files into current directory
'''
for i in range(1,6):
    with open(f'{i}.txt', 'w') as file:
        file.write(f"Writing into {file.name} file")
'''

# working with path files
cur = Path("1.txt")

# show some path attributes
print(cur.absolute()) # absolute path
print(cur.name) # file name
print(cur.absolute().parent) # parent of the file
print(cur.absolute().parent.parent) # Grandparent of the file
print(cur.suffix) # file extension

# methods
print(f'Exist: {cur.exists()}')
print(f'is file: {cur.is_file()}')
print(f'is directory: {cur.is_dir()}')

# create directories
dir_name1 = "dir1"
dir_name2 = "dir2"
dir_name3 = "dir3"
dirs = [dir_name1,dir_name2,dir_name3]
for dir in dirs:
    new_path = Path(cur.absolute().parent / dir)
    if not new_path.exists():   
        new_path.mkdir()

# create a list of files in the current directory
for file in cur.parent.iterdir(): # returns a list of files in current directory
    if file.is_file():
        print(file.name)

files = [x.name for x in cur.parent.iterdir() if x.is_file()]
with open("file_names.txt", 'w') as file:
    file.writelines(files)
    file.write('\n')
