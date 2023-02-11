import json
import time 

# [X] criar arquivo caso não exista
# [X] perguntar a ação ao usuário
# 1 - [X] apresentar arquivo
# 1 - [X] se estiver vazio, mostrar mensagem
# 2 - [X] perguntar novas informações 
# 2 - [X] modifica-las
# 2 - [X] apresentar sucesso e informações salvas


def write_json(data, filename="server.json"):
  with open (filename, "w") as f:
    json.dump(data, f, indent=4)

def get_json(filename="server.json"):
  try:
    with open (filename) as json_file:
      data = json.load(json_file)
      return data
  except:
    new_json = {'name': '', 'ip': '', 'password': ''}
    write_json(new_json)
    return new_json

def modify_json(server_json):
  print('Nos informe algumas informações')
  print('1 - Informe o nome do servidor:')
  server_name = input();
  print('2 - Informe o IP do servidor:')
  server_ip = input();
  print('3 - Informe a senha do servidor')
  server_password = input();

  if(server_name != ''):
    server_json['name'] = server_name
  if(server_ip != ''):
    server_json['ip'] = server_ip
  if(server_password != ''):
    server_json['password'] = server_password
  write_json(server_json)
  
  print('Informações salvas com sucesso!')


def show_json_action():
  json_data = get_json()
  if(json_data['name'] + json_data['ip'] + json_data['password'] != ''):
    print(json_data)
  else:
    print('O arquivo não contem informações, tente escrever novas informações usando a ação "1 - Escrever no arquivo"')

def modify_json_action():
  json_data = get_json()
  modify_json(json_data)
  show_json_action()



action = ''
while( action != '3'):

  print('''

    Nos informe qual ação deseja fazer pelo numero da mesma 
      1 - Escrever no arquivo
      2 - Ler o arquivo
      3 - parar

  ''')
  action = input();

  if(action == '1'):
    modify_json_action()

  if(action == '2'):
    show_json_action()

  time.sleep(0.5)
