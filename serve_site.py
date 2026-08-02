import os
import socket
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("PORT", "8080"))
HOST = "0.0.0.0"


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WORKSPACE_DIR, **kwargs)


def get_local_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.connect(("8.8.8.8", 80))
            return sock.getsockname()[0]
    except Exception:
        return "127.0.0.1"


if __name__ == "__main__":
    os.chdir(WORKSPACE_DIR)
    ip = get_local_ip()
    print(f"Serving files from: {WORKSPACE_DIR}")
    print(f"Open this address from another device: http://{ip}:{PORT}/")
    print("Press Ctrl+C to stop the server")
    with ThreadingHTTPServer((HOST, PORT), Handler) as httpd:
        httpd.serve_forever()
