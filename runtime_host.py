
import os
import importlib.util
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT = int(os.environ.get("PORT", "8080"))
USER_FUNC_PATH = os.environ.get("USER_FUNC_PATH", "user_function.py")
FUNC_NAME = os.environ.get("FUNC_NAME", "handle")

def load_user_func(path, name):
    spec = importlib.util.spec_from_file_location("user_module", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, name)

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(length) if length else b''
        try:
            func = load_user_func(USER_FUNC_PATH, FUNC_NAME)
            req = json.loads(body.decode('utf-8')) if body else {}
            res = func(req)
            self.send_response(200)
            self.send_header('Content-Type','application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'result': res}).encode('utf-8'))
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode('utf-8'))

if __name__ == '__main__':
    print(f"Starting runtime host on port {PORT}, loading {USER_FUNC_PATH}::{FUNC_NAME}")
    server = HTTPServer(('0.0.0.0', PORT), Handler)
    server.serve_forever()
