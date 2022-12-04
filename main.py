from fbchat import Client
from fbchat.models import *
import parser
#Данные пользователя
username = 'username'
password = 'password'
#Авторизация
client = Client(username, password)
with open('file_with_urls.txt', 'r', ecnoding='utf-8') as f:
  for i in f.read().strip().split():
    post_result = parser.parsing(i)
    client.send(message=f'Есть совпадение по вашему запросу: {post_result}', thread_id='USER_ID', thread_type=ThreadType.USER)

#id 100002069809245
client.logout()
