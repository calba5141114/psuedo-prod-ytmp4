import os


def clear_dir(current_directory, current_directory_list):
    ''' clears working directory of mp4 and webm files'''
    for item in current_directory_list:
        if item.endswith(".mp4"):
            os.remove(os.path.join(current_directory, item))
        elif item.endswith(".webm"):
            os.remove(os.path.join(current_directory, item))


def validate_str(str, val_str):
    ''' validates string '''
    if val_str in str:
        return True
