import json
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import random

class GetHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"{message}"
        return content.encode("utf8")  # NOTE: must return
    def do_GET(self):
        self._set_headers()
        self.wfile.write(self._html(random.randrange(1,10)))

if __name__ == '__main__':
    #from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 3030), GetHandler)
    print ('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()
