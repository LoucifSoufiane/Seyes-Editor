"""
create_shortcut.py
Creates Windows shortcut 'Seyes Editor.lnk' with custom icon and silent launch.
"""

import sys
import os
import subprocess

base_dir = os.path.dirname(os.path.abspath(__file__))
python_dir = os.path.dirname(sys.executable)
pythonw_exe = os.path.join(python_dir, "pythonw.exe")
shortcut_path = os.path.join(base_dir, "Seyes Editor.lnk")
target_script = os.path.join(base_dir, "main.py")
icon_path = os.path.join(base_dir, "assets", "icon.ico")

ps_command = f"""
$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut('{shortcut_path}')
$Shortcut.TargetPath = '{pythonw_exe}'
$Shortcut.Arguments = '"{target_script}"'
$Shortcut.WorkingDirectory = '{base_dir}'
$Shortcut.IconLocation = '{icon_path},0'
$Shortcut.Description = 'Seyes Editor — French Ruled Paper & Penmanship Desktop Generator'
$Shortcut.Save()
"""

subprocess.run(["powershell", "-NoProfile", "-Command", ps_command], check=True)
print(f"Shortcut created successfully at: {shortcut_path}")
print(f"Exists: {os.path.exists(shortcut_path)}")
