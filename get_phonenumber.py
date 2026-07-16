import requests
import json
from openpyxl import Workbook, load_workbook
import os
headers = {"authorization":"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3ODM1NzQxMzkuNDY0LCJkYXRhIjp7Il9pZCI6IjZhMGFjZDA5ZDI4N2JkY2JhYjA3Njg5NiIsInVzZXJuYW1lIjoiNzAxNzI5ODA5NCIsImZpcnN0TmFtZSI6IiIsImxhc3ROYW1lIjoiIiwib3JnYW5pemF0aW9uIjp7Il9pZCI6IjVlYjM5M2VlOTVmYWI3NDY4YTc5ZDE4OSIsIndlYnNpdGUiOiJwaHlzaWNzd2FsbGFoLmNvbSIsIm5hbWUiOiJQaHlzaWNzd2FsbGFoIn0sInJvbGVzIjpbIjViMjdiZDk2NTg0MmY5NTBhNzc4YzZlZiJdLCJjb3VudHJ5R3JvdXAiOiJJTiIsIm9uZVJvbGVzIjpbXSwidHlwZSI6IlVTRVIifSwianRpIjoia3pMRUd0X1JTMmFWU2ZqTzU1anN4UV82YTBhY2QwOWQyODdiZGNiYWIwNzY4OTYiLCJpYXQiOjE3ODI5NjkzMzl9.4GEK1yBSGgci6yUBAI5Z6QLWy6Ndn2fsrdjzgP3ykjk"}
main_api1 = "https://pw-api-gate.penpencil.co/v3/"
comm_url = "community/posts/v2?channelId="
#comm_id = "6a0d5a03a4f9e66563c207be"#"6a0d5a03a4f9e66563c207be"#input("enter id")
def write_unique(post_list):
    excel_file = "details.xlsx"
    id_file = "E:/react-app/pw test/text/user_id.txt"

    user_id = str(post_list[0]).strip()

    if not os.path.exists(id_file):
        open(id_file, "w").close()

    with open(id_file, "r") as f:
        if user_id in {line.strip() for line in f}:
            return

    if not os.path.exists(excel_file):
        wb = Workbook()
        ws = wb.active
        ws.title = "Users"
        ws.append(["User ID", "Name", "Mobile No", "Profile_pic"])
        wb.save(excel_file)

    wb = load_workbook(excel_file)
    ws = wb.active
    ws.append(post_list)
    wb.save(excel_file)
    wb.close()

    # Save new user ID
    with open(id_file, "a") as f:
        f.write(user_id + "\n")

def unfollow(user):
    url = main_api1+"community/followers/"
    payload = {"follow": False}
    response = requests.post(url+user, headers=headers, json=payload)


def save(isunfollow = False):
    url = main_api1+"community/followers/list/6a0acd09d287bdcbab076896"#6099c197bb25c700347f81f5"
    response = requests.get(url, headers=headers)
    json_dict = json.loads(response.text)
    output = json_dict['data']
    for i in range(0,len(output)):
        output_dict = output[i]
        try:
            post_list=[output_dict['follower_id'],output_dict['name'],output_dict['mobile'],output_dict['profileImage']]
        except:
            print("profile image not found of this user.")
            post_list=[output_dict['follower_id'],output_dict['name'],output_dict['mobile'],"null"]
        write_unique(post_list)
        print(post_list)
        if isunfollow:
            unfollow(output_dict['follower_id'])
            print("unfollowed: ",output_dict['follower_id'])
        else:
            print("not unfollowed")
            continue

def follow(usr_id):  #follows a userid and prints if it already followed?
    url = main_api1+"community/followers/"
    payload = {"follow": True}
    response = requests.post(url+usr_id, headers=headers, json=payload)
    json_dict = json.loads(response.text)
    isFollowed = json_dict['success']
    print("is already followed? : ",not(isFollowed))
    

def get_user(comm_id, page_id):  #gets user from a community and page = 1 ,2 ,or more
    response= requests.get(main_api1+comm_url+comm_id+"&page="+page_id,headers=headers)  
    json_dict = json.loads(response.text)
    if json_dict['success']== True:
            #print(json_dict)
            output_dict = json_dict['data']
            post_list=output_dict['posts']
            for i in range(0,len(post_list)):
                post_dict=post_list[i]
                user_id = (post_dict['user_id'])
                follow(user_id)
    

