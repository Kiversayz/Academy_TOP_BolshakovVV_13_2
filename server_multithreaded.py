import socket
import threading

HOST = '127.0.0.1'
PORT = 12345
server_running = True  # Флаг работы сервера

def handle_client(conn, addr):
    global server_running
    print(f"Подключен клиент: {addr}")
    
    while True:
        try:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                print(f"Клиент {addr} отправил пустую строку, ждем новый ввод...")
                continue  # Ждем новый ввод

            if data.lower() == "exit":
                print(f"Клиент {addr} отключился.")
                break  # Разрываем соединение с клиентом

            if data.lower() == "stop server":
                print("Остановка сервера...")
                server_running = False
                break  # Завершаем сервер

            print(f"Получено от {addr}: {data}")
            conn.sendall(data.encode('utf-8'))

        except ConnectionResetError:
            print(f"Клиент {addr} принудительно отключился.")
            break
        except Exception as e:
            print(f"Ошибка: {e}")
            break

    conn.close()

def start_server():
    global server_running
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        print(f"Сервер запущен на {HOST}:{PORT}")

        while server_running:
            try:
                server_socket.settimeout(1)  # Устанавливаем таймаут для выхода из ожидания при остановке сервера
                conn, addr = server_socket.accept()
                client_thread = threading.Thread(target=handle_client, args=(conn, addr))
                client_thread.start()
            except socket.timeout:
                continue

        print("Сервер завершил работу.")

if __name__ == "__main__":
    start_server()
