from setuptools import setup

APP = ['main.py']  # Replace 'your_image_resizer_script.py' with your actual script name
DATA_FILES = []

OPTIONS = {
    'argv_emulation': True,
    'packages': ['PIL', 'tkinter'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
