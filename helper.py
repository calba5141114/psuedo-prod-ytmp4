import os

def clear_dir(download_directory, download_directory_list):
    """Clears Directory."""
    for file in download_directory_list:
        file_path = os.path.join(download_directory, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

def validate_str(str, val_str):
    """Validates Youtube Links."""
    if val_str in str:
        return True
