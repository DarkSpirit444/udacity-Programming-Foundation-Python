# -*- coding: utf-8 -*-
import os

def rename_files(folder):
    # (1) get file names from folder
    file_list = os.listdir(folder)
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(folder)
    # (2) for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(None, "0123456789"))
    os.chdir(saved_path)

rename_files("/Users/davidteo/udacity/OOP/prank")

