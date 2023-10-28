# Server Echo Python para o restreador

### Para rodar o server
```py
  python3 app.py
```
vai rodar o socket na porta 9953

### Teste local do servidor
Para ver funcionando tem que rodar localmente pois o banco de dados esta em um cluster no mongodb atlas

Oque precisa ter para funcionar
- [x] Python 3 ou superios
- [x] Mongodb - Caso não tenha rodar um container docker

Para funcionar tem que rodar os seguintes comandos no terminal.
Em um terminal rodar o servidor com esta escrito no começo, em outra aba do terminal rodar o seguinte codigo em bash
```sh
  nc localhost 9953
```
Quando abrir a conexão mandar estra string que tem todas as informações que o codigo precisa e que o restreador manda.
```txt
*ET,354522186202029,HB,V,160C08,0D3A0B,80BB8262,81F3EF20,0000,0000,00000000,18,10,00,0000008D,0,0000000000,0000000000,0000,3.71,0#
```
### Caso que estiver usando seja noob e utilize ruindows utilizar estre trexo de codigo para testar no terminal

```sh
python -c "import socket; sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM); sock.connect(('localhost', 9953)); sock.send(b'*ET,354522186202029,HB,V,160C08,0D3A0B,80BB8262,81F3EF20,0000,0000,00000000,18,10,00,0000008D,0,0000000000,0000000000,0000,3.71,0#'); sock.close()"
```