import os
print('t.me/WebSecExplorers')
def process_files(path, key, decode=False):
    os.chdir(path)
    FileList = os.listdir(path)
    EncodedData = []

    for idx, file_name in enumerate(FileList):
        if decode:
            # Decoding the file name
            encoded_name = ''.join(chr(ord(c) ^ ord(key[idx % len(key)])) for idx, c in enumerate(file_name))
        else:
            # Encoding the file name
            encoded_name = ''.join(chr(ord(c) ^ ord(key[idx % len(key)])) for idx, c in enumerate(file_name))

        if '\0' in encoded_name:
            print(f"Error: Encoded name for {file_name} contains null character.")
            continue

        # Rename the file
        try:
            os.rename(file_name, encoded_name)
        except Exception as e:
            print(f"Error renaming {file_name} to {encoded_name}: {e}")
            continue

        EncodedData.append(encoded_name)

        with open(encoded_name, 'rb') as f:
            content = f.read()

        if decode:
            # Decoding the content of the file
            encoded_content = bytes([b ^ ord(key[idx % len(key)]) for idx, b in enumerate(content)])
        else:
            # Encoding the content of the file
            encoded_content = bytes([b ^ ord(key[idx % len(key)]) for idx, b in enumerate(content)])

        with open(encoded_name, 'wb') as f:
            f.write(encoded_content)

    print("Finished . . . . ")
    print("Clear Data = ", FileList)
    print("Encoded Data = ", EncodedData)


path = input('Encoded data pwd: ')
key = "12"
action = input("Do you want to decode the files? (y/n): ")

if action.lower() == 'y':
    process_files(path, key, decode=True)
else:
    process_files(path, key)
