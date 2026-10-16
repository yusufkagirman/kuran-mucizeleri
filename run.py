"""Yerelde başlat: py run.py  ->  http://localhost:4321 (önce npm run build gerekirse kendisi yapar)."""
import http.server, os, subprocess, webbrowser, functools

root = os.path.dirname(os.path.abspath(__file__))
if not os.path.exists(os.path.join(root, "dist", "index.html")):
    subprocess.run("npm run build", cwd=root, shell=True, check=True)
handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=os.path.join(root, "dist"))
srv = http.server.ThreadingHTTPServer(("127.0.0.1", 4321), handler)
print("http://localhost:4321  (durdurmak için Ctrl+C)")
webbrowser.open("http://localhost:4321")
srv.serve_forever()
