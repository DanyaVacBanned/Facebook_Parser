from fbchat import Client
from fbchat.models import *
import parser
#Данные пользователя
username = 'username'
password = 'password'
#Авторизация
client = Client(username, password)
link_and_text = parser.main()
client.send(message='Есть совпадение по вашему запросу: {link_and_text}', thread_id='100002069809245', thread_type=ThreadType.USER)

#id 100002069809245
client.logout()
