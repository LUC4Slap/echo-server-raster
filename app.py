import socket
from parserResponse import ParserResponse
from threading import Thread

# EXEMPLO DE ENVIO
# *ET,354522186202029,HB,V,160C08,0D3A0B,80BB8262,81F3EF20,0000,0000,00000000,18,10,00,0000008D,0,0000000000,0000000000,0000,3.71,0#



def on_new_client(client_socket, addr):
    parser = ParserResponse()
    while True:
        try:
            data = client_socket.recv(1024).decode("utf-8")
            if not data:
                break
            parse = parser.parser_afeter_save(data)
            # print(parse)
        except Exception as error:
            print(error)
            break
    client_socket.close()


def main():
    host = "0.0.0.0"  # allow any incoming connections
    port = 9953
    try:
        s = socket.socket()
        s.bind((host, port))  # bind the socket to the port and ip address

        s.listen(5)  # wait for new connections
        while True:
            c, addr = s.accept()  # Establish connection with client.
            # this returns a new socket object and the IP address of the client
            print(f"New connection from: {addr}")
            print(c)
            thread = Thread(target=on_new_client, args=(c, addr))  # create the thread
            thread.start()  # start the thread
        c.close()
        thread.join()
    except KeyboardInterrupt:
        print("Parado pelo usuario")
        s.close()
    except Exception as error:
        print(error)
        s.close()


if __name__ == "__main__":
    main()
