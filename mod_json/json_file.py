import reprlib
import json
from random import randint
#
# def json_file():
#     try:
#         with open('scratch.json', 'r') as f:
#             print(f.read())
#     except:
#         print('неверна введена функция')
#     print('конец')
#
#
# str_json = '''
# {
#   "response": [
#     {
#       "id": 210700286,
#       "first_name": "Lindsey",
#       "last_name": "Stirling"
#     },
#     {
#       "id": 297428682,
#       "first_name": "Jared",
#       "last_name": "Leto"
#     }
#   ]
# }
# '''
# data = json.loads(str_json) #loads считываем строку json
# # print(data)
# # print(type(data['response']))
# # for item in data['response']: #прошлись по списку
# #     print(item['id'], item['first_name'])
# for item in data['response']:
#      del item['last_name'] #удалили значение
#      item['likes'] = randint(100, 200) #добавили значение
# print(data['response'])


# new_json = json.dumps(data) #dumps создает строку в формате json
# print(new_json)
# with open('new_json.json', 'w') as file: # сохраняем файл
#     json.dump(data, file, indent=3) #метод dump создает файл формата json
#
# with open('new_json.json', 'r') as file: # load считываем данные json
#     data = json.load(file)
#
# print(data)

