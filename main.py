import zipfile
import os

output = "ResourcePack.mcpack"
exclude = ["main.py", "README.md", ".gitignore", output]
exclude_dirs = [".git"]

with zipfile.ZipFile(f"./{output}", "w", zipfile.ZIP_DEFLATED) as f:
  for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    for filename in files:
      if filename not in exclude:
        file_path = os.path.join(root, filename)
        f.write(file_path)
