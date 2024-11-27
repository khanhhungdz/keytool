import json,requests,time
from time import strftime

ngay=int(strftime('%d'))
key=str(ngay*25937+469173)

url=f'https://bandemov1.000webhostapp.com/keytool.php?key={key}'
token_link1s="16eeefa5a1359f8ee8cd7db6fe4a4d6afd969a18"
post_url=requests.get(f'https://link1s.com/api?api={token_link1s}&url={url}').json()
if post_url['status']=="error":
	print(post_url['message'])
	quit()
else:
	link_key=post_url['shortenedUrl']
nhap_key=input(f'''\033[1;32m Link lấy key: \033[1;33m{link_key}
      \033[1;36m▀█▀ █░█ ▄▀█ █▄░█  \033[1;97m ▀█▀ █░█   \033[1;90m\033[0;31m
\033[1;35m      ░█░ █▄█ █▀█ █░▀█  \033[1;97m ░█░ █▄█\033[1;97m


          \033[1;34mQuả Tool Siêu Cấp Pro By: Trương Tuấn Tú 
              [-----------------------------]
               \033[1;31m1.Support TooL:Trương Tuấn Tú .
               \033[1;33m2.YouTube:Trương Tuấn Tú .
               \033[1;36m3.Zalo:.
               \033[1;36m4. Fb.com/tuantu.dev.
               \033[0;35m5. Website:tumongmo.sg.
              [-----------------------------]
                \033[1;32m KeyTooLHôm Nay: \033[1;33m''')
if nhap_key==key:
	print('\033[1;32m Key chính xác Đúng Chúc Bạn Ngày Tốt Lành    ')
else:
	print('\033[1;31m Key Sai Vui Lòng Vượt Link Để lấy')
	quit()