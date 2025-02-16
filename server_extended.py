import socket

HOST = '127.0.0.1'
PORT = 12345

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"Сервер запущен на {HOST}:{PORT}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Подключен клиент: {addr}")

                while True:
                    try:
                        data = conn.recv(1024).decode('utf-8')
                        if not data:
                            print("Клиент отправил пустую строку, ждем новый ввод...")
                            continue  # Ждем нового сообщения

                        if data.lower() == "exit":
                            print(f"Клиент {addr} отключился.")
                            break  # Отключаем клиента

                        if data.lower() == "stop server":
                            print("Остановка сервера...")
                            return  # Завершаем сервер

                        print(f"Получено: {data}")
                        conn.sendall(data.encode('utf-8'))

                    except ConnectionResetError:
                        print("Клиент отключился принудительно.")
                        break
                    except Exception as e:
                        print(f"Ошибка: {e}")
                        break

if __name__ == "__main__":
    start_server()
