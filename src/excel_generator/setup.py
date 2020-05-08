from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("gui_app.py", base=base, icon="gui\\xcel_gen.ico",)]

packages = ["webbrowser", "PySide2", "openpyxl"]
options = {
    "build_exe": {"packages": packages, "include_files": ["gui"]},
}

setup(
    name="Excel Generator",
    options=options,
    version="v1.1",
    description="Quick Excel Generator that creates and formats a table",
    executables=executables,
)
