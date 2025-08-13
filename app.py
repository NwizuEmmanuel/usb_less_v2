import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
import socket

UPLOAD_DIR = "uploads"
server_thread = None
httpd = None

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def upload_files():
    files = filedialog.askopenfilenames(title="Select files to upload")
    if not files:
        return
    
    for file_path in files:
        filename = os.path.basename(file_path)
        dest_path = os.path.join(filename)
        try:
            shutil.copy(file_path, dest_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to upload {filename}: {e}")
            return
    messagebox.showinfo("Success", f"Uploaded {len(files)} files to '{UPLOAD_DIR}'.")

def run_server(port):
    global httpd
    os.chdir(UPLOAD_DIR)
    server_address = ("", port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()

def start_server_on_app_start():
    global server_thread
    port = get_port()
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
    server_thread = threading.Thread(target=run_server, args=(port,), daemon=True)
    server_thread.start()
    ip = get_local_ip()
    server_label.config(text=f"Server running at http://{ip}:{port}")

def stop_server_on_app_close():
    global httpd
    if httpd:
        # Shutdown in a separate thread to avoid blocking the main thread
        threading.Thread(target=httpd.shutdown, daemon=True).start()
        httpd = None
    if os.path.exists(UPLOAD_DIR):
        shutil.rmtree(UPLOAD_DIR)

def get_port():
    port_str = port_entry.get()
    try:
        port = int(port_str)
        if 1 <= port <= 65535:
            return port
        else:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Port", "Please enter a valid port number (1-65535).")
        return 8000

# --- UI Beautification ---
root = tk.Tk()
root.title("Multi File Uploader")
root.geometry("500x420")  # Increased window size for more space
root.configure(bg="#f5f6fa")

main_frame = tk.Frame(root, bg="#f5f6fa")
main_frame.pack(fill="both", expand=True, padx=15, pady=15)  # Add padding to all sides

title_label = tk.Label(
    main_frame,
    text="USB-Less File Uploader",
    font=("Segoe UI", 18, "bold"),
    bg="#f5f6fa",
    fg="#273c75",
)
title_label.pack(pady=(30, 10))

desc_label = tk.Label(
    main_frame,
    text="Upload multiple files and share them over your local network.",
    font=("Segoe UI", 11),
    bg="#f5f6fa",
    fg="#353b48",
)
desc_label.pack(pady=(0, 10))

# Port Entry
port_frame = tk.Frame(main_frame, bg="#f5f6fa")
port_label = tk.Label(port_frame, text="Port:", font=("Segoe UI", 11), bg="#f5f6fa", fg="#353b48")
port_label.pack(side="left", padx=(0, 5))
port_entry = tk.Entry(port_frame, font=("Segoe UI", 11), width=8)
port_entry.insert(0, "8000")
port_entry.pack(side="left")
port_frame.pack(pady=(0, 10))

upload_btn = tk.Button(
    main_frame,
    text="Upload Files",
    command=upload_files,
    font=("Segoe UI", 12, "bold"),
    bg="#00a8ff",
    fg="white",
    activebackground="#0097e6",
    activeforeground="white",
    relief="flat",
    width=18,
    height=2,
)
upload_btn.pack(pady=10)

server_label = tk.Label(
    main_frame,
    text="Server not running.",
    font=("Segoe UI", 10, "bold"),
    bg="#f5f6fa",
    fg="#e84118",
)
server_label.pack(pady=(10, 0))

footer_label = tk.Label(
    main_frame,
    text="Files will be stored in the 'uploads' folder.",
    font=("Segoe UI", 9),
    bg="#f5f6fa",
    fg="#718093",
)
footer_label.pack(side="bottom", pady=10)

# Delete uploads folder on app start, then create it
# if os.path.exists(UPLOAD_DIR):
#     shutil.rmtree(UPLOAD_DIR)
# os.makedirs(UPLOAD_DIR)

# Start server after UI is loaded
start_server_on_app_start()

root.mainloop()
