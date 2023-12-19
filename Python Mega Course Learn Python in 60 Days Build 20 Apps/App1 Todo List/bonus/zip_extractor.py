import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall((dest_dir))


if __name__ == "__main__":
    extract_archive("/Users/manasranjanmunda/Documents/GitHub/Newt-Global-Private-Limited/Python Mega Course Learn Python in 60 Days Build 20 Apps/App1 Todo List/bonus/compressed.zip", "/Users/manasranjanmunda/Documents/GitHub/Newt-Global-Private-Limited/Python Mega Course Learn Python in 60 Days Build 20 Apps/App1 Todo List/bonus/files")