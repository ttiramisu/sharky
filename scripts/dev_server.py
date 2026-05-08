import os
import time
import subprocess
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import io
import sys
from functools import partial
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
WATCHED_CONTENT_DIR = ROOT_DIR / "content"
WATCHED_WEB_DIR = ROOT_DIR / "web"

DIST_DIR = ROOT_DIR / "dist"
PORT = 6767

last_mtimes = {}
needs_reload = False  


def watched_files():
    yaml_files = WATCHED_CONTENT_DIR.rglob("*.yaml")
    css_files = WATCHED_WEB_DIR.rglob("*.css")
    return list(yaml_files) + list(css_files)

def build():
    global needs_reload
    print("Rebuilding site...")
    subprocess.run([sys.executable, "main.py"], cwd=ROOT_DIR)
    needs_reload = True  
    print("Build done.")

def watch():
    """Return True only if a watched file has changed since last check"""
    global last_mtimes
    changed = False
    for f in watched_files():
        try:
            mtime = os.path.getmtime(f)
        except FileNotFoundError:
            continue
        if f not in last_mtimes:
            last_mtimes[f] = mtime
        elif mtime > last_mtimes[f]:
            last_mtimes[f] = mtime
            changed = True
    return changed

def watch_loop():
    build()
    while True:
        if watch():
            build()
        time.sleep(1)

class LiveReloadHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        global needs_reload
        if self.path == "/reload":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            if needs_reload:
                self.wfile.write(b"reload")
                needs_reload = False
            else:
                self.wfile.write(b"ok")
        else:
            super().do_GET()

    def send_head(self):
        path = self.translate_path(self.path)
        if os.path.isdir(path):
            for index in ("index.html", "index.htm"):
                index_path = os.path.join(path, index)
                if os.path.exists(index_path):
                    path = index_path
                    break
        if path.endswith(".html") and os.path.exists(path):
            with open(path, "rb") as f:
                content = f.read().decode("utf-8", errors="ignore")
            injected = content.replace(
                "</body>",
                """<script>
                async function checkReload() {
                    try {
                        const res = await fetch("/reload");
                        const text = await res.text();
                        if (text === "reload") location.reload();
                    } catch(e){}
                }
                setInterval(checkReload, 1000);
                </script></body>"""
            )
            encoded = injected.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(encoded)))
            self.end_headers()
            return io.BytesIO(encoded)
        return super().send_head()

def serve():
    handler = partial(LiveReloadHandler, directory=str(DIST_DIR))
    httpd = HTTPServer(("localhost", PORT), handler)
    print(f"🌍 Serving at http://localhost:{PORT}")
    httpd.serve_forever()


def main():
    t = threading.Thread(target=watch_loop, daemon=True)
    t.start()
    serve()


if __name__ == "__main__":
    main()
