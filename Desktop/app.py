import time
import threading
import pyperclip
from websocket import create_connection, WebSocketConnectionClosedException

# --- CONFIGURATION ---
SERVER_URL = "wss://clipboard-synchronization.onrender.com"  # replace with your WebSocket server URL
SESSION_ID = "sezan"  # same ID used by Android
WS_ENDPOINT = f"{SERVER_URL}/ws/{SESSION_ID}"

# --- INITIALIZE WEBSOCKET ---
try:
    ws = create_connection(WS_ENDPOINT)
    print("[✓] Connected to server")
except Exception as e:
    print(f"[!] Failed to connect: {e}")
    exit(1)

# --- SHARED CLIPBOARD STATE ---
last_clipboard = pyperclip.paste()

def watch_clipboard():
    global last_clipboard
    while True:
        try:
            current = pyperclip.paste()
            if current != last_clipboard:
                last_clipboard = current
                try:
                    ws.send(current)
                    print(f"[→] Sent: {current[:30]}...")
                except WebSocketConnectionClosedException:
                    print("[x] WebSocket closed while sending")
                    break
        except Exception as e:
            print(f"[!] Clipboard watch error: {e}")
        time.sleep(0.5)

def listen_server():
    global last_clipboard
    while True:
        try:
            message = ws.recv()
            if message and message != last_clipboard:
                last_clipboard = message
                pyperclip.copy(message)
                print(f"[←] Received: {message[:30]}...")
        except WebSocketConnectionClosedException:
            print("[x] WebSocket closed while receiving")
            break
        except Exception as e:
            print(f"[!] Receive error: {e}")
            break

# --- START THREADS ---
watch_thread = threading.Thread(target=watch_clipboard, daemon=True)
watch_thread.start()

listen_server()  # Main thread blocks here









