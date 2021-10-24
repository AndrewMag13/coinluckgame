from http.server import BaseHTTPRequestHandler, HTTPServer, CGIHTTPRequestHandler
import os
import cgi

class ServerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request, Path:", self.path)
        if self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = open('/home/nail/oir/pyServ/index.html')
            html = html.read()
            self.wfile.write(html.encode('utf-8'))
        elif self.path.endswith(".jpg"):
            self.send_response(200)
            self.send_header('Content-type', 'image/jpg')
            self.end_headers()
            with open(os.curdir + os.sep + self.path, 'rb') as file:
                self.wfile.write(file.read())
        elif self.path.endswith(".html"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = open('/home/nail/oir/pyServ/'+self.path)
            html = html.read()
            self.wfile.write(html.encode('utf-8'))
        elif self.path.endswith(".css"):
            self.send_response(200)
            self.send_header('Content-type', 'text/css')
            self.end_headers()
            css = open('/home/nail/oir/pyServ/'+self.path)
            css = css.read()
            self.wfile.write(css.encode('utf-8'))
        elif self.path == "favicon.ico":
            self.send_response(200)
            self.send_header('Content-type', 'image/icon')
            self.end_headers()
            with open(os.curdir + os.sep + self.path, 'rb') as file:
                self.wfile.write(file.read())
        elif ".js" in self.path:
            self.send_response(200)
            self.send_header('Content-type', 'text/javascript')
            self.end_headers()
            javascript = open('/home/nail/oir/pyServ/'+self.path)
            javascript = javascript.read()
            self.wfile.write(javascript.encode('utf-8')) 
        elif '?' in self.path:
             pass
        else:
            self.send_error(404, "Page Not Found {}".format(self.path))

def server_thread(port):
    server_address = ('', port)
    httpd = HTTPServer(server_address, ServerHandler, CGIHTTPRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    port = 8000
    print("Starting server at port %d" % port)
    server_thread(port)