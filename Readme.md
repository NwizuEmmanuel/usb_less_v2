# USB-Less File Uploader

A simple, cross-platform desktop app built with Python and Tkinter to upload multiple files and share them instantly over your local network—no USB drive required!

## Features

- **Multi-file upload:** Select and upload multiple files at once.
- **Instant sharing:** Files are served over HTTP for easy download from other devices on your network.
- **Custom port:** Choose the port for the local server.
- **Auto server:** The server starts automatically when the app launches and stops when the app closes.
- **Clean UI:** Modern, user-friendly interface.
- **Easy start:** Launch the app with `StartApp.bat` for automatic requirements checking.

## How It Works

1. **Start the app:** Double-click `StartApp.bat` or run it from the command line. The server starts automatically.
2. **Upload files:** Click "Upload Files" and select files to share.
3. **Share:** Other users can download files by visiting `http://<your-ip>:<port>` in their browser.
4. **Stop:** Closing the app stops the server and deletes the uploaded files.

## Installation

### Requirements

- Python 3.7+
- Tkinter (usually included with Python)

### Clone & Run

```sh
git clone https://github.com/yourusername/usb_less_v2.git
cd usb_less_v2
StartApp.bat
```

> **Tip:**  
> If you prefer, you can still run the app directly with `python app.py`.

### Packaging (Optional)

To create a standalone executable (Windows):

```sh
pip install pyinstaller
pyinstaller --onefile --windowed app.py
```

The executable will be in the `dist` folder.

## Usage

1. **Set the port** (optional): Enter your desired port or use the default (`8000`).
2. **Upload files:** Click "Upload Files" and select files.
3. **Share the link:** The app displays your local IP and port. Share this link with others on your network.
4. **Download:** Others can download files via their browser.

## Security

- Files are only accessible on your local network.
- The uploads folder is deleted when the app closes.

## Contributing

Pull requests are welcome! Please open an issue first to discuss changes.

## License

MIT

## Screenshot

![screenshot](screenshots/screenshot.png)

---

**Note:**  
- For best results, ensure your firewall allows incoming connections on the chosen port.
- This app is for local network use only.