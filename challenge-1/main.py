import argparse
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

# Application version
VERSION = "1.0.0"

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - [%(levelname)s]: %(message)s')

class CatchAllHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, World!")
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MY Server")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host to bind the server to")
    parser.add_argument("--port", type=int, default=8000, help="Port to bind the server to")
    args = parser.parse_args()

    host = args.host
    port = args.port

    server = HTTPServer((host, port), CatchAllHandler)
    logging.info(f"webserver version {VERSION} listening: http://{host}:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logging.info("Shutting down...")
        server.server_close()
