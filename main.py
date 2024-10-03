import os
import shutil

path = rf"{input("The folder path you want to edit ")}"
files = os.listdir(path = path)
extensions = []

# we are adding the extensions to the list
for item in files:
    if os.path.splitext(item)[1] == "":
        pass
    else:
        extensions.append(os.path.splitext(item))
    
#####################################################################################

# We are creating a file name for unique extension
unique_extensions = list(set([item[1][0:]for item in extensions]))
folder_names = [item[1:] + "_files" for item in unique_extensions]

for item in range(len(folder_names)):
    if not os.path.exists(path + "\\" + folder_names[item]):
        os.makedirs(name = path + "\\" + folder_names[item])

#####################################################################################
# We are moving all the files in the path to the created folders

file_names = os.listdir(path)
for extension in unique_extensions:    
    for item in file_names:
        if item.endswith(extension) and not os.path.exists(path + "\\" + os.path.splitext(item)[1][1:] + "_files" + "\\" + item):
            shutil.move(path + "\\" + item, path + "\\" + os.path.splitext(item)[1][1:] + "_files" + "\\" + item)
                