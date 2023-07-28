import os
size = os.stat(r"C:\Users\WELCOME\Desktop\Interview_quations\python_datatype\file_handle\sample.txt").st_size
if size == 0:
    print("file is empty")
else:
    print("file not empty")


