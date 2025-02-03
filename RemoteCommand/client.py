import socket
import os

print('https://t.me/WebSecExplorers')

print('======================= Command ===========================')
print("= list => list directory contents                         =")
print("= chdir => change current directory                       =")
print("= pwd => print name of current/working directory          =")
print("= file => Get File                                        =")
print("= cmd => Run command on server                            =")
print('===========================================================')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created . . . ")
client.connect(("127.0.0.1", 9000))
print("Client connected . . . ")

try:
    while True:
        command = input('What do you want? ')
        
        # If the command is 'chdir', ask for the new path
        if command.startswith('chdir'):
            new_dir = input('Enter the new directory path: ')
            command = f'chdir {new_dir}'
        
        # If the command is 'file', ask for the file name to retrieve
        if command.startswith('file'):
            filename = input('Enter the filename to get: ')
            command = f'file {filename}'

        # If the command is 'cmd', ask for the command to execute on the server
        if command.startswith('cmd'):
            user_command = input('Enter the command to run on the server: ')
            command = f'cmd {user_command}'

        client.send(command.encode())
        
        # Receive and display the server's response
        response = client.recv(1024).decode()
        print(response)

        # If the server sends "quit", break the loop and close connection
        if response.lower() == "quit":
            break

except Exception as e:
    print(f'Failed: {e}')

finally:
    client.close()
    print("Connection closed.")
