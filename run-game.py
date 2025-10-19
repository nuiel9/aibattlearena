#!/usr/bin/env python3
"""
Simple HTTP server to run the 3D AI game locally
Usage: python3 run-game.py
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import socket

PORT = 8000

def find_free_port(start_port=8000):
    """Find a free port starting from start_port"""
    for port in range(start_port, start_port + 100):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind(('', port))
                return port
        except OSError:
            continue
    raise Exception("No free port found")

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        super().end_headers()

def main():
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    print(f"🎮 Starting AI Hunter 3D Game Server...")
    print(f"📂 Serving files from: {os.getcwd()}")
    
    # Find a free port
    try:
        free_port = find_free_port(PORT)
    except Exception as e:
        print(f"❌ Error finding free port: {e}")
        return
    
    with socketserver.TCPServer(("", free_port), MyHTTPRequestHandler) as httpd:
        game_url = f"http://localhost:{free_port}/ai-game-3d.html"
        print(f"🚀 Server running at: http://localhost:{free_port}")
        print(f"🎯 Game URL: {game_url}")
        print("👆 Click the game URL above or it will open automatically...")
        print("⏹️  Press Ctrl+C to stop the server")
        
        # Automatically open the game in browser
        try:
            webbrowser.open(game_url)
        except:
            print("⚠️  Could not auto-open browser. Please manually visit the URL above.")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server stopped!")
            sys.exit(0)

if __name__ == "__main__":
    main()