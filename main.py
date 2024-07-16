from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    """
        A special class responsible for
        processing incoming requests from clients
    """

    def do_GET(self):
        """ Method for processing incoming GET requests """
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        try:
            with open("index.html", "r", encoding="utf-8") as file:
                html_content = file.read()
            self.wfile.write(bytes(html_content, "utf-8"))
        except FileNotFoundError:
            self.wfile.write(bytes("<html><body><h1>File not found</h1></body></html>", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
