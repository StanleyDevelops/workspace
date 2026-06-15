# Create a folder "backup", handle the FileNotfounderror gracefully accordingly

import os

folder = "backup"

if not os.path.exists(folder):
    os.mkdir(folder)
    print(f"{folder} created Successfully.")
else:
    print(f"{folder} already exisits. Skipping")