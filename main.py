import requests
from fake_useragent import UserAgent
import threading

ua = UserAgent()

url = 'https://api.remanga.org/api/activity/votes/'

token = 'YOUR_TOKEN_HERE'

file_lock = threading.Lock()

def get_next_post_number():
    with file_lock: 
        with open("like_posts.txt", "r+") as file1: #Fill in this file with the chapter id, see example in fill_posts.py
            lines_user = file1.readlines()
            if lines_user:
                last_user = lines_user.pop().strip()  
                file1.seek(0)  
                file1.writelines(lines_user)  
                file1.truncate()  
                return last_user
            else:
                print("File like_posts.txt empty or contains incorrect data.")
                return None

def send_dislike():
    while True:
        try:
            post_number = get_next_post_number()
            if post_number is None:
                break  
            datas_r2 = {
                "chapter": post_number,
                "type": 0
            }
            headers_2 = {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br, zstd",
                "Accept-Language": "en-US,en;q=0.5",
                "Authorization": f"Bearer {token}",
                "Connection": "keep-alive",
                "Content-Length": "29",
                "Content-Type": "application/json",
                "DNT": "1",
                "Host": "api.remanga.org",
                "Origin": "https://remanga.org",
                "Priority": "u=0",
                "Referer": "https://remanga.org/",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-site",
                "Sec-GPC": "1",
                "TE": "trailers",
                "User-Agent": ua.random
            }
            r2 = requests.post(url, headers=headers_2, json=datas_r2)
            if r2.status_code == 200:
                print(f'Done like {post_number}')
            else:
                print(f"An error has occurred: {r2.status_code}")
                print(r2.text)
        except Exception as e:
            print(str(e))

threads = []
for i in range(15): #Optimal number of threads: 10-15 (10-15 likes per second)
    thread = threading.Thread(target=send_dislike)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
