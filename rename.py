#program to rename files with any numbers as the filename without the numbers
import os
def rename_files():
    #get file names from a folder
    file_list = os.listdir(r"C:\Users\Akash\Desktop\prank") #r is for raw
    os.chdir(r"C:\Users\Akash\Desktop\prank")
    #for each file, rename
    for file_name in file_list:
        print("\nOld name: " + file_name + "\n")
        print("New name: " + file_name.translate(None, "0123456789"))
        os.rename(file_name, file_name.translate(None, "0123456789"))   #remove numbers from filename
rename_files()
