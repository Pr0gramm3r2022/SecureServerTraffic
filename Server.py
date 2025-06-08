#server code

from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "123.456.789.0" 
PORT = 9999
class ProtectHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>Backbone Server</h1></body></html>", "utf-8"))

    def do_POST(self):
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' + date + '"}', "utf-8"))
    def do_PUT(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
    '''If the resource exists at the given URI, it is updated with the new data.

    If the resource does not exist, the server can create it at that URI.

    The request includes the data to be stored in the request body.

    It's idempotent, meaning sending the same request multiple 
    times results in the same outcome (unlike POST).'''

    #Universal Resource Identifier. 
    '''a character sequence that identifies a logical (abstract) or physical resource -- 
    usually, but not always, connected to the internet. 
    The strings of characters incorporated in a URI,
    such as a scheme name and a file path, serve as identifiers.'''

    URI = 123

    #make request method
    #check if there is a resource at the URI.
    #if there is, a new resource is created at the URI.
    #includes the data to be stored in the request body

    #make request method
    #use the requests library to do it

       

     





server = HTTPServer((HOST, PORT), ProtectHTTP)
print("Server is running...")

command = input("type 'close server' to close the server")
while (command != 'close server'):

    server.serve_forever()



server.server_close()

'''#if user input(terminal) is close server, run the following line

command = input("type 'close server' to close the server")

if input == 'close server':
    server.server_close()
else:
    continue'''

#write in a command or method to close the server
print("Server is stopped")


         





 
