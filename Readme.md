# USB-Less File Uploader

A simple Tkinter app to upload multiple files and share them over your local network.

## Usage

1. Run the app:
    ```
    python app.py
    ```
2. Upload files using the GUI.
3. Files are served over HTTP for download on your local network.

## Packaging

To build a distributable package:

1. Install setuptools:
    ```
    pip install setuptools
    ```
2. Build the package:
    ```
    python setup.py sdist
    ```

To create a standalone executable (Windows):

1. Install pyinstaller:
    ```
    pip install pyinstaller
    ```
2. Build the executable:
    ```
    pyinstaller --onefile --windowed app.py
    ```

The executable will be in the `dist` folder.

## .gitignore

The `.gitignore` file excludes cache, virtual environments, uploads, and other unnecessary files from version control.