import socket
import os
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9000))
server.listen(5)
print("Server started, waiting for client to connect...")

while True:
    client_socket, client_address = server.accept()
    print(f"Client {client_address} connected")
    
    try:
        while True:
            command = client_socket.recv(1024).decode()
            if not command:
                break

            if command == 'quit':
                client_socket.send("quit".encode())
                break

            elif command == 'list':
                # List the contents of the current directory
                directory_contents = '\n'.join(os.listdir('.'))
                client_socket.send(directory_contents.encode())

            elif command.startswith('chdir'):
                # Extract the new directory path
                path = command.split(' ', 1)[1]
                try:
                    os.chdir(path)  # Change directory
                    client_socket.send(f"Directory changed to {os.getcwd()}".encode())
                except FileNotFoundError:
                    client_socket.send(f"Error: Directory '{path}' not found.".encode())
                except PermissionError:
                    client_socket.send(f"Error: Permission denied to change to '{path}'.".encode())

            elif command == 'pwd':
                # Print the current working directory
                client_socket.send(os.getcwd().encode())

            elif command.startswith('file'):
                # Extract filename
                filename = command.split(' ', 1)[1]
                if os.path.exists(filename) and os.path.isfile(filename):
                    with open(filename, 'rb') as file:
                        file_data = file.read()
                        client_socket.send(file_data)
                else:
                    client_socket.send(f"Error: File '{filename}' not found.".encode())

            elif command.startswith('cmd'):
                # Extract the user command to run
                user_command = command.split(' ', 1)[1]
                try:
                    # Execute the system command using os.system()
                    result = os.popen(user_command).read()
                    client_socket.send(result.encode())
                except Exception as e:
                    client_socket.send(f"Error executing command: {str(e)}".encode())
                
            else:
                client_socket.send(f"Unknown command: {command}".encode())

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()
