import os
import time
import subprocess
from http.server import SimpleHTTPRequestHandler, HTTPServer
import threading
import io

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
WATCHED_FILES = [
    os.path.join(ROOT_DIR, "CONTENTS/CONTENTS.yaml"),
    os.path.join(ROOT_DIR, "CONTENTS/CONFIG.yaml"),
    os.path.join(ROOT_DIR, "CONTENTS/NAVIGATION.yaml"),
    os.path.join(ROOT_DIR, "utils/contents.py"),
]

DIST_DIR = os.path.join(ROOT_DIR, "dist")
PORT = 6767

last_mtimes = {}
needs_reload = False  # reload flag

def build():
    global needs_reload
    print("🔨 Rebuilding site...")
    subprocess.run(['python3', 'main.py'], cwd=ROOT_DIR)
    needs_reload = True  # only set after rebuild finishes
    print("✅ Build done.")

def watch():
    """Return True only if a watched file has changed since last check"""
    global last_mtimes
    changed = False
    for f in WATCHED_FILES:
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
    build()  # initial build
    while True:
        if watch():
            build()
        time.sleep(1)  # 1-second polling

class LiveReloadHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        global needs_reload
        if self.path == "/reload":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            if needs_reload:
                self.wfile.write(b"reload")
                needs_reload = False  # reset only when browser reloads
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
            # inject reload script before </body>
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
    os.chdir(DIST_DIR)
    httpd = HTTPServer(("localhost", PORT), LiveReloadHandler)
    print(f"🌍 Serving at http://localhost:{PORT}")
    httpd.serve_forever()

if __name__ == "__main__":
    t = threading.Thread(target=watch_loop, daemon=True)
    t.start()
    serve()