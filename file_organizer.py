import os
import shutil

file_directory = {
    "Images": [
        ".jpeg",
        ".jpg",
        ".tiff",
        ".gif",
        ".bmp",
        ".png",
        ".bpg",
        ".svg",
        ".heif",
        ".psd",
    ],
    "Videos": [
        ".avi",
        ".flv",
        ".wmv",
        ".mov",
        ".mp4",
        ".webm",
        ".vob",
        ".mng",
        ".qt",
        ".mpg",
        ".mpeg",
        ".3gp",
        ".mkv",
    ],
    "Documents": [
        ".oxps",
        ".epub",
        ".pages",
        ".docx",
        ".doc",
        ".fdf",
        ".ods",
        ".odt",
        ".pwi",
        ".xsn",
        ".xps",
        ".dotx",
        ".docm",
        ".dox",
        ".rvg",
        ".rtf",
        ".rtfd",
        ".wpd",
        ".xls",
        ".xlsx",
        ".ppt",
        ".pptx",
        ".txt",
    ],
    "Archives": [
        ".a",
        ".ar",
        ".cpio",
        ".iso",
        ".tar",
        ".gz",
        ".rz",
        ".7z",
        ".dmg",
        ".rar",
        ".xar",
        ".zip",
    ],
    "Audio": [
        ".aac",
        ".aa",
        ".aac",
        ".dvf",
        ".m4a",
        ".m4b",
        ".m4p",
        ".mp3",
        ".msv",
        ".ogg",
        ".oga",
        ".raw",
        ".vox",
        ".wav",
        ".wma",
    ],
    "PDFs": [".pdf"],
    "Data": [".py", ".html5", ".html", ".htm", ".xhtml", ".js", ".c"],
    "Apps": [".exe"],
}


path = input("Enter Path: ")


misc_dir = os.path.join(path, "Misc")  # Create a Misc folder for unorganized files
os.makedirs(misc_dir, exist_ok=True)

for item in os.listdir(path):
    item_path = os.path.join(path, item)

    if os.path.isfile(item_path):
        _, file_extension = os.path.splitext(item)

        categorized = False

        for category, extensions in file_directory.items():
            if file_extension.lower() in extensions:
                category_dir = os.path.join(path, category)
                os.makedirs(category_dir, exist_ok=True)

                source_path = item_path
                destination_path = os.path.join(category_dir, item)

                shutil.move(source_path, destination_path)
                categorized = True
                break

        if not categorized:
            source_path = item_path
            destination_path = os.path.join(misc_dir, item)

            shutil.move(source_path, destination_path)

print("Files organized successfully.")
