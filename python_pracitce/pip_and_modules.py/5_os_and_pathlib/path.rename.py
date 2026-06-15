# Moving Folders
from pathlib import Path

desti_dir = Path("My Files")
desti_dir.mkdir(exist_ok=True)

folders_to_move = {
    "Videos": "videos",
    "Images": "images",
    "Documents": "Docs"
}

for source_name, target_name in folders_to_move.items():
    source_path = Path(source_name)
    target_path = desti_dir/target_name

    if source_path.exists():
        source_path.rename(target_path)
        print(f"Successfully moved {source_name} to {target_path}")
    else:
        print(f"Warning: {source_name} couldn't be found!")