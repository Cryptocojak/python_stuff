import os
import shutil

# Set the directory you want to start from (make sure this ends with "/")
rootDir = '/Users/your_name_here/Downloads/School_Photos/'

# Set the directory where the temp txt file will be written to 
# (Desktop is fine, use a different directory than the pictures.)
temp_file_path = '/Users/your_name_here/Downloads/names_temp_file.txt'

# What is a .DS_Store file?
# A .DS_Store, short for Desktop Services Store,
# is an invisible file on the macOS operating system
# that gets automatically created anytime you look into a folder with ‘Finder.’

# This deletes the .DS_Store file from rootDir if it exists
for root, dirs, files in os.walk(rootDir):
    for file in files:
        if file == ".DS_Store":
            os.remove(os.path.join(root, file))

# Open a temp file for writing names to
with open(temp_file_path, 'w') as f:
    # Walk the directory tree and write the filenames to the file
    for dirName, subdirList, fileList in os.walk(rootDir):
        for fname in fileList:
            f.write(fname + '\n')


# This makes an alphabetical list of filenames 
with open(temp_file_path, 'r') as f:
    filenames = f.readlines()
filenames = [line.strip() for line in filenames]
filenames.sort() 

# This gets rid of the extention from the filename
clean_filenames = filenames
clean_filenames = [os.path.splitext(name)[0] for name in clean_filenames]

# This splits the filename by the '-' into name, and number
nameList = []
for clean_filename in clean_filenames:
    name, number = clean_filename.split('-')
    nameList.append(name)

# This makes directories for each unique person
unique_directory_names = (sorted(set(nameList)))
for dir_name in unique_directory_names:
    dir_path = os.path.join(rootDir, dir_name)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

# Finally the filenames are put into the new directory 
for file_name, directory in zip(filenames, nameList):
    src_file = rootDir + file_name
    dest_dir = os.path.join(rootDir, directory)
    print(f'copy file: {src_file}, to: {dest_dir} ... :)')
    if file_name.startswith(directory) and os.path.exists(src_file) and os.path.exists(dest_dir):
        shutil.copy2(src_file, dest_dir)

# Check if the temp namelist file exists and delete
if os.path.exists(temp_file_path):
    os.remove(temp_file_path)
