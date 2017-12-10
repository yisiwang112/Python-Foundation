import os

def rename_files():
    file_list = os.listdir(r"/Users/ywang/Documents/AI/prank")
 #   saved_path = os.getcwd()
 #   print(saved_path)
    os.chdir(r"/Users/ywang/Documents/AI/prank")
    for file_name in file_list:
        os.rename(file_name, file_name.strip('0123456789'))

rename_files()
