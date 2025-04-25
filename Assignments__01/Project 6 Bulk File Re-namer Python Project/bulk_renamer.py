import os

def bulk_rename(folder_path, prefix):
    files = os.listdir(folder_path)  # Folder ke files list karo
    files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]  # Sirf files lena

    for count, filename in enumerate(files, start=1):
        ext = os.path.splitext(filename)[1]  # File extension nikaalo (.txt, .jpg, etc.)
        new_name = f"{prefix}_{count}{ext}"  # Naya naam banao
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, new_name)

        os.rename(src, dst)  # Rename command
        print(f"Renamed: {filename} --> {new_name}")

# User inputs
folder = input("Enter folder path: ")
prefix = input("Enter new prefix for files: ")

bulk_rename(folder, prefix)
