"""
install_fonts_to_windows.py
Utility script to install the bundled French pedagogical fonts (Marelle and Andika)
directly into Windows System Fonts (C:\\Windows\\Fonts and registry) for use in Word,
LibreOffice, Photoshop, etc.
"""

import os
import shutil
import winreg
import ctypes

def install_fonts():
    fonts_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "fonts")
    if not os.path.exists(fonts_dir):
        print(f"Directory not found: {fonts_dir}")
        return

    win_fonts_dir = os.environ.get("WINDIR", r"C:\Windows") + r"\Fonts"
    reg_path = r"Software\Microsoft\Windows NT\CurrentVersion\Fonts"

    font_files = [f for f in os.listdir(fonts_dir) if f.lower().endswith(('.ttf', '.otf'))]
    print(f"Found {len(font_files)} fonts to install.")

    try:
        reg_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, reg_path, 0, winreg.KEY_SET_VALUE)
    except PermissionError:
        print("Note: To register fonts system-wide, please run this script as Administrator.")
        print("Opening User Fonts registry instead...")
        reg_path_user = r"Software\Microsoft\Windows NT\CurrentVersion\Fonts"
        reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path_user, 0, winreg.KEY_SET_VALUE)

    installed_count = 0
    for font_file in font_files:
        src = os.path.join(fonts_dir, font_file)
        dst = os.path.join(win_fonts_dir, font_file)
        font_name = os.path.splitext(font_file)[0].replace("-", " ")

        try:
            shutil.copy2(src, dst)
            winreg.SetValueEx(reg_key, f"{font_name} (TrueType)", 0, winreg.REG_SZ, font_file)
            installed_count += 1
            print(f"✓ Installed: {font_name}")
        except Exception as e:
            print(f"⚠ Could not copy to Windows\\Fonts directly ({e}). Font remains available inside Séyès Studio!")

    try:
        winreg.CloseKey(reg_key)
    except Exception:
        pass

    # Notify running Windows applications of new font resources
    HWND_BROADCAST = 0xFFFF
    WM_FONTCHANGE = 0x001D
    ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_FONTCHANGE, 0, 0)
    print(f"\nDone! Processed {installed_count} fonts.")

if __name__ == "__main__":
    install_fonts()
