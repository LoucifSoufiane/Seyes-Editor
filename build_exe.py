"""
build_exe.py
Automated build script to compile Seyes Editor into a single standalone Windows .exe.
"""

import os
import sys
import shutil
import subprocess

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SPEC_CONTENT = f'''# -*- mode: python ; coding: utf-8 -*-
import os
import sys

block_cipher = None

base_dir = r"{BASE_DIR}"

added_files = [
    (os.path.join(base_dir, "assets"), "assets"),
]

hidden_imports = [
    "PyQt6",
    "PyQt6.QtCore",
    "PyQt6.QtGui",
    "PyQt6.QtWidgets",
    "PyQt6.QtPrintSupport",
    "seyes_engine",
    "ui",
]

a = Analysis(
    [os.path.join(base_dir, "main.py")],
    pathex=[base_dir],
    binaries=[],
    datas=added_files,
    hiddenimports=hidden_imports,
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=["tkinter", "matplotlib", "scipy", "numpy", "pandas", "pytest"],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="Seyes Editor",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=os.path.join(base_dir, "assets", "icon.ico"),
)
'''

def main():
    print("=" * 60)
    print("BUILDING STANDALONE SEYES EDITOR EXECUTABLE (.EXE)")
    print("=" * 60)

    spec_path = os.path.join(BASE_DIR, "seyes_editor.spec")
    with open(spec_path, "w", encoding="utf-8") as f:
        f.write(SPEC_CONTENT)
    print(f"Generated spec file: {spec_path}")

    # Run PyInstaller
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--clean",
        "--noconfirm",
        spec_path
    ]
    print(f"Running PyInstaller command: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=BASE_DIR)
    if result.returncode != 0:
        print("ERROR: PyInstaller build failed!")
        sys.exit(result.returncode)

    dist_exe = os.path.join(BASE_DIR, "dist", "Seyes Editor.exe")
    if not os.path.exists(dist_exe):
        print(f"ERROR: Expected output {dist_exe} was not found!")
        sys.exit(1)

    file_size_mb = os.path.getsize(dist_exe) / (1024 * 1024)
    print(f"\nSUCCESS: Created {dist_exe} ({file_size_mb:.2f} MB)")

    # Copy to project root directory as requested by the user
    root_exe = os.path.join(BASE_DIR, "Seyes Editor.exe")
    shutil.copy2(dist_exe, root_exe)
    print(f"Copied standalone executable to project root: {root_exe}")
    print("=" * 60)
    print("STANDALONE BUILD COMPLETE AND READY FOR DISTRIBUTION!")
    print("=" * 60)

if __name__ == "__main__":
    main()
