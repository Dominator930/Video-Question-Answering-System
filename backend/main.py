import os
import shutil
from vdo_2_aud import processor
from vdo_2_aud import file_manager
from transcription import transformer
from config import model
from chunking import manage_chunk
from save_all_chunks import save_chunk
from embeds import create_db
from prompt import prompt
from prompt import inference
from config import output_model

user_path = input("Enter the file/folder location : ")
file_name = user_path.split("\\")[-1].split(".")[0]

if __name__ == "__main__":
    if not user_path.endswith(".parquet"):
        file_manager(user_path)
        for vdo in os.listdir("Video"):
            if not vdo.endswith(".gitkeep"):
                processor(vdo, "".join(vdo.split(".")[0:-1]))
        for aud in os.listdir("Audio"):
            if not aud.endswith(".gitkeep"):
                transformer(aud, model)
        for jsons in os.listdir("Transcripted_json"):
            if not jsons.endswith(".gitkeep"):
                manage_chunk(jsons)
        save_chunk(os.listdir("Managed_chunk"))
        create_db(file_name)
    while True:
        user_query = input("ask anything related to the video you shared (type quit or exit to stop the program) : ")
        if (user_query == "quit") or (user_query=="exit"):
            try :
                shutil.move(os.path.join("parquet_files", f"{file_name}.parquet"), os.path.join("saved_parquets", f"{file_name}.parquet"))
                print(f"Congrats your parquet file is saved in 'saved_parquets' as {file_name}.parquet. now you can use it anytime you want without all that hefty processing!!")
            except:
                pass
            folders = ["Audio", "Video", "Transcripted_json", "Managed_chunk", "parquet_files"]
            for folder in folders:
                for file in os.listdir(folder):
                    if not file.endswith(".gitkeep"):
                        file_path = os.path.join(folder, file)
                        os.remove(file_path)            
            break
        else :
            generated_prompt = prompt(file_name, user_query)
            print(inference(generated_prompt, output_model))
            print('-----------------------------------------------------------------------------------------------')
            