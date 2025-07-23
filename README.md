# Clipboard-Sync
A simple and secure real-time clipboard synchronization system between Android and desktop using WebSockets. Seamlessly sync text copied on one device to the clipboard of another.

---

## 🔧 Features

- 📱 Sync clipboard between Android and PC (bi-directional)
- 🔗 Real-time communication using WebSocket
- 📤 Auto-send copied text to connected device
- 📥 Auto-update local clipboard on receiving text
- 💾 Session-based pairing for multiple users

---

## 🏗️ Project Structure

📂 ClipboardSyncApp/
├── 📱 Android App (Kotlin)
│   ├── MainActivity.kt
│   ├── ClipboardSyncService.kt
│   ├── activity_main.xml
│   └── AndroidManifest.xml
├── 💻 Python WebSocket Client
│   └── app.py
├── 📷 Assets
│   └── App Icon (logo)
└── README.md

---

## 🚀 How It Works

1. Start the **Python WebSocket client** on your desktop or laptop.
2. Launch the **Android app**, enter a unique session ID, and initiate syncing.
3. Any text copied on one device will automatically appear in the clipboard of the other.

---

## 🧪 Tech Stack

- **Android**: Kotlin, OkHttp WebSocket, ClipboardManager
- **Python**: websocket-client, pyperclip
- **Backend**: FastAPI WebSocket server (hosted on Render)
- **Clipboard Access**: `ClipboardManager` (Android), `pyperclip` (Python)

---

## 🔧 Installation

### 📱 Android App

- Open the project in **Android Studio**
- Connect your device or use an emulator
- Build and run the app

### 💻 Python Client

```bash
# Install dependencies
pip install websocket-client pyperclip

# Run the app
python app.py

⚠️ Make sure a WebSocket server (e.g., FastAPI-based) is running and accessible to both devices.

⸻

📝 License

This project is licensed under the MIT License. See the LICENSE file for more details.

⸻

🙋‍♂️ Author

Made by Sezan Agvan

⸻
