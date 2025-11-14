SUPPORTED SYSTEMS

Works on:
• Windows 11
• Brave installed in the default location:
%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\

EXE version:
• Works even if the user does NOT have Python installed
• Tkinter is bundled automatically

NOT SUPPORTED (if you want to modify it go ahead)

This version does NOT work on:
• macOS
• Linux
• Brave Portable editions
• Chrome, Edge, Vivaldi (unless support is added later)

REQUIREMENTS (FOR .PY SCRIPT)

If running the Python script directly:
• Python 3.8 or newer
• Tkinter module (included in most Windows Python installs)

HOW TO USE

Run the script
Double-click export_brave_bookmarks.py
Or run in terminal:
python export_brave_bookmarks.py

Choose the save location
A Save-As dialog will appear.
Default filename:
Brave_Bookmarks_Export_YYYY-MM-DD.html

Done
The HTML file will contain all bookmarks from all Brave profiles.

HOW IT WORKS

• Scans Brave’s User Data folder for all profiles
• Reads each profile’s Bookmarks JSON file
• Converts everything into Netscape-format HTML
• Writes all profiles into one clean export file

BUILDING AN EXE (OPTIONAL)

*Before building keep all the files bundled in the same folder and the dist and build will build inside it. An exe will be built to desktop and also inside the built dist folder*

Option A — Build manually using PyInstaller:

Install PyInstaller:
pip install pyinstaller

Build the EXE:
pyinstaller --noconsole --onefile export_brave_bookmarks.py

The executable will appear in:
dist/export_brave_bookmarks.exe

Option B — Use the included BAT file:

Rename export_brave_exe.txt → export_brave_exe.bat

Ensure “Save as type: All Files” is selected

Run the batch file to automatically build the EXE

Run it 

Choose the save location
A Save-As dialog will appear.
Default filename:
Brave_Bookmarks_Export_YYYY-MM-DD.html


ABOUT THIS TOOL

I made this to save time(a few clicks) manually exporting Brave bookmarks.
Run the EXE from anywhere and save the exported HTML wherever you like.

LICENSE

MIT License — free to use, modify, and share.