import http.server
import ssl

# Specify the address and port for the server
address = ('localhost', 8000)

# Create an HTTPS server with the self-signed certificate and private key
httpd = http.server.HTTPServer(address, http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, certfile="server.crt", keyfile="server.key", server_side=True)

# Start the server
print("Server running at https://{}:{}".format(*address))
httpd.serve_forever()
