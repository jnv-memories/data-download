import requests
import json
from openpyxl import Workbook, load_workbook
import os
headers = {"authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3ODM1NzQxMzkuNDY0LCJkYXRhIjp7Il9pZCI6IjZhMGFjZDA5ZDI4N2JkY2JhYjA3Njg5NiIsInVzZXJuYW1lIjoiNzAxNzI5ODA5NCIsImZpcnN0TmFtZSI6IiIsImxhc3ROYW1lIjoiIiwib3JnYW5pemF0aW9uIjp7Il9pZCI6IjVlYjM5M2VlOTVmYWI3NDY4YTc5ZDE4OSIsIndlYnNpdGUiOiJwaHlzaWNzd2FsbGFoLmNvbSIsIm5hbWUiOiJQaHlzaWNzd2FsbGFoIn0sInJvbGVzIjpbIjViMjdiZDk2NTg0MmY5NTBhNzc4YzZlZiJdLCJjb3VudHJ5R3JvdXAiOiJJTiIsIm9uZVJvbGVzIjpbXSwidHlwZSI6IlVTRVIifSwianRpIjoia3pMRUd0X1JTMmFWU2ZqTzU1anN4UV82YTBhY2QwOWQyODdiZGNiYWIwNzY4OTYiLCJpYXQiOjE3ODI5NjkzMzl9.4GEK1yBSGgci6yUBAI5Z6QLWy6Ndn2fsrdjzgP3ykjk"}
main_api1 = "https://pw-api-gate.penpencil.co/v3/"
comm_url = "community/posts/v2?channelId="

def write_unique(post_list):
    excel_file = "teacher_details.xlsx"
    id_file = "E:/react-app/pw test/text/teacher_id.txt"

    user_id = str(post_list[0]).strip()

    if not os.path.exists(id_file):
        open(id_file, "w").close()

    with open(id_file, "r") as f:
        if user_id in {line.strip() for line in f}:
            return

    if not os.path.exists(excel_file):
        wb = Workbook()
        ws = wb.active
        ws.title = "Teacher"
        ws.append(["Teacher ID", "Name", "Mobile No", "Profile_Pic"])
        wb.save(excel_file)

    wb = load_workbook(excel_file)
    ws = wb.active
    ws.append(post_list)
    wb.save(excel_file)
    wb.close()

    # Save new user ID
    with open(id_file, "a") as f:
        f.write(user_id + "\n")

        
def phone(user_id):
    url = main_api1+"community/followers/list/"+user_id
    response = requests.get(url, headers=headers)
    json_dict = json.loads(response.text)
    if len(json_dict['data'])!= 0:
        output = json_dict['data']
        for i in range(0,len(output)):
            output_dict = output[i]
            try:
                post_list=[output_dict['follower_id'],output_dict['name'],output_dict['mobile'],output_dict['profileImage']]
            except:
                print("no profile image")
                post_list=[output_dict['follower_id'],output_dict['name'],output_dict['mobile'],"null"]
            write_unique(post_list)
            print(post_list)
    else:
        print("empty")

def teacher():
    POINTER_FILE = "E:/react-app/pw test/text/teacher_pointer.txt"
    with open(POINTER_FILE, "r") as pointer:
        content = pointer.read().strip()
        start_position = int(content)
    with open("E:/react-app/pw test/text/user_id.txt") as f:
        f.seek(start_position)
        for line in f:
            phone(line.strip())
        current_position = f.tell()
    with open(POINTER_FILE, "w") as file:
        file.write(str(current_position))
        print("writted")

#teacher()
#phone("65f0f6340c0043f9a787a3a0")
