try:
  import usocket as socket
except:
  import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  print('Content = %s' % request)
  conn.send('HTTP/1.1 200 OK\r\nAccess-Control-Allow-Origin:http://localhost:3000\r\n')
  conn.send('Content-Type: text/plain\r\n')
  conn.send('Connection: close\n\n')
  log = open("log.txt")
  conn.sendall(log.read())
  log.close()
  conn.close()
