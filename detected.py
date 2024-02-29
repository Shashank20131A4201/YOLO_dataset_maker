import os
import json
def check_folders():
    with open("detected.json", "r") as f:
        json_string = f.read()
    d = json.loads(json_string)
    video_folder_path = os.path.join(os.getcwd(), "videos")
    for office in os.listdir(video_folder_path):
        office_path = os.path.join(video_folder_path, office)
        for students in os.listdir(office_path):
            if students not in d:
                d[office+"_"+students] = False
    return d

check_folders()
  
