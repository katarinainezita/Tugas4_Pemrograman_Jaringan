import base64
import socket

def send_request(request):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))
    client.send(request.encode())
    response = client.recv(4096).decode()
    client.close()
    return response

def upload_file(filename):
    with open(filename, 'rb') as file:
        file_content = file.read()
    file_content_base64 = base64.b64encode(file_content).decode()
    request = f"UPLOAD {filename} {file_content_base64}"
    return send_request(request)

def delete_file(filename):
    request = f"DELETE {filename}"
    return send_request(request)

if __name__ == "__main__":
    while True:
        command = input("Enter command (UPLOAD <filename> / DELETE <filename> / EXIT): ")
        if command.startswith("UPLOAD "):
            filename = command.split(' ')[1]
            response = upload_file(filename)
            print(response)
        elif command.startswith("DELETE "):
            filename = command.split(' ')[1]
            response = delete_file(filename)
            print(response)
        elif command == "EXIT":
            break
        else:
            print("Invalid command.")
