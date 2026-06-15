# "It's easier to ask forgiveness than permission."
import os

print(os.getcwd())
try:
    os.remove("love.txt")
    print("File deleted with success.")
except FileNotFoundError:
    print("File doesn't Exist.")

folder = "backup"
try:
    os.mkdir(folder)
    print(f"{folder} Created.")     
except FileExistsError:
    print("The File Already Exists.")