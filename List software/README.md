# List Software

This Python script allows you to list all the software installed on a Windows machine by querying the Windows Registry. It uses the `winreg` module to access and enumerate registry keys in the HKEY_LOCAL_MACHINE/SOFTWARE path.

## How it Works

- The script connects to the registry and opens the `SOFTWARE` key.
- It then iterates over the keys (which represent installed software) and prints out their names.
- This script is intended for educational purposes, allowing users to understand how software installation data can be accessed programmatically on a Windows machine.

## Disclaimer

This tool is provided for educational purposes only. The author does not encourage or support illegal or unethical activities. Use this tool responsibly and only on systems where you have proper authorization to access the registry. The author is not responsible for any misuse of this tool.
