import subprocess
import os
import shutil

def file_manager(user_path):
    file_name = user_path.split("\\")[-1]
    try :
        shutil.copy(user_path, os.path.join("Video", file_name))
    except :
        files = os.listdir(user_path)
        for file in files :
            shutil.copy(os.path.join(user_path, file), os.path.join("Video", file))
        
def processor(input_file, output_file):
    subprocess.run(
        ["ffmpeg", "-i", os.path.join("Video", input_file), os.path.join("Audio", f"{output_file}.mp3")],
        check=True
    )
