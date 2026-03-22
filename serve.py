#!/usr/bin/env python3
"""
SalesFunnel PWA — Local Server
Run this on your Mac to serve the app to your iPhone over WiFi.

Usage:
  cd SalesFunnelPWA
  python3 serve.py

Then on your iPhone, open Safari and go to:
  http://YOUR-MAC-IP:8080

To find your Mac's IP: System Preferences → Network → Wi-Fi → IP Address
"""
import http.server
import ssl
import socket
import os

PORT = 8080

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        return s.getsockname()[0]
    except:
        return '127.0.0.1'
    finally:
        s.close()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({
    '.json': 'application/json',
    '.js': 'application/javascript',
    '.html': 'text/html',
    '.png': 'image/png',
    '.webmanifest': 'application/manifest+json',
})

ip = get_ip()
print(f"""
╔══════════════════════════════════════════════╗
║         SalesFunnel PWA — Local Server       ║
╠══════════════════════════════════════════════╣
║                                              ║
║  Mac (this computer):                        ║
║    http://localhost:{PORT}                     ║
║                                              ║
║  iPhone (same WiFi):                         ║
║    http://{ip}:{PORT}                     ║
║                                              ║
║  On iPhone Safari:                           ║
║    1. Open the URL above                     ║
║    2. Tap Share (↑) → Add to Home Screen     ║
║    3. App appears with OmG icon              ║
║                                              ║
║  Press Ctrl+C to stop the server             ║
╚══════════════════════════════════════════════╝
""")

with http.server.HTTPServer(('0.0.0.0', PORT), handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
