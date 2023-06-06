import os


if __name__ == '__main__':
    print('Welcome to iRobo 1.1 Created by OpenAI')
    while True:
        x = input('Say: ')
        if(x=='q'):
          os.system("say 'bye bye friend'")
          break
        command = f'say "{x}"'
        os.system(command)
