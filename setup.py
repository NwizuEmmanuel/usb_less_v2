from setuptools import setup

setup(
    name="usb_less_file_uploader",
    version="1.0.0",
    description="A simple Tkinter app to upload and share files over local network.",
    author="Onyeka Nwizu",
    author_email="onwizu.ics.com",
    py_modules=["app"],
    install_requires=[],
    entry_points={
        "gui_scripts": [
            "usb_less_file_uploader=app:main"
        ]
    },
)