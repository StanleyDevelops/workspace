from pathlib import Path


# the path object
p = Path("pip_and_modules.py\5_os_and_pathlib\os_module.py")
print(p.name)
print(p.stem)
print(p.suffix)
print(p.parent)
Path("notes.txt").rename("back\notes.txt") 

print(Path("Backup file").exists())
Path("Backup file").rename("Backup")