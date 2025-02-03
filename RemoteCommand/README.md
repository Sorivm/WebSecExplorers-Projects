# Remote Command Execution via Vulnerable Server (Educational Purposes Only)

This project demonstrates a simple **client-server** communication model using socket programming. It allows a **client** to send commands to the **server**, which executes them and returns the output. However, this project is **intentionally vulnerable**, and if deployed on a machine without proper security measures, **hackers could gain full control** over the server.

**⚠️ Disclaimer:**  
This project is for **educational purposes only**. The creators are not responsible for any misuse or illegal activity arising from the use of this code. Use it responsibly and only in controlled, safe environments!

## Features

- **list**: Lists the files and directories in the current directory.
- **chdir**: Changes the directory path on the server.
- **pwd**: Displays the current working directory.
- **file**: Retrieves a file from the server.
- **cmd**: Executes a command on the server and returns the result.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/RemoteCommandExec.git
   cd RemoteCommandExec
