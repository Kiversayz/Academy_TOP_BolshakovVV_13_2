import socket

HOST = '127.0.0.1'
PORT = 12345

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("Подключено к серверу. Введите 'exit' для отключения, 'stop server' для остановки сервера.")

        while True:
            try:
                message = input("Введите сообщение: ").strip()
                if not message:
                    print("Нельзя отправить пустое сообщение!")
                    continue

                client_socket.sendall(message.encode('utf-8'))

                if message.lower() in ["exit", "stop server"]:
                    print("Отключение...")
                    break

                response = client_socket.recv(1024).decode('utf-8')
                if not response:
                    print("Соединение разорвано сервером.")
                    break

                print(f"Ответ сервера: {response}")

            except ConnectionResetError:
                print("Программа на сервере разорвала соединение.")
                break
            except Exception as e:
                print(f"Ошибка: {e}")
                break

        print("Process finished with exit code 0.")

if __name__ == "__main__":
    start_client()
