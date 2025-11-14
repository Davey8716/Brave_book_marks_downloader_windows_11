"""
export_brave_bookmarks.py
-----------------------------------------------------
Exports all Brave bookmarks into a single HTML file.
Opens a Save As dialog (default name includes date stamp).
No pop-ups after saving.
"""

import os
import json
from datetime import datetime
from html import escape
from tkinter import Tk, filedialog


def netscape_header(title="Bookmarks"):
    return (
        "<!DOCTYPE NETSCAPE-Bookmark-file-1>\n"
        "<META HTTP-EQUIV=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\">\n"
        f"<TITLE>{escape(title)}</TITLE>\n"
        f"<H1>{escape(title)}</H1>\n"
        "<DL><p>\n"
    )


def walk_nodes(node, lines, indent=1):
    IND = "    " * indent
    t = node.get("type")
    if t == "folder":
        title = node.get("name", "Folder")
        add_date = str(node.get("date_added", ""))[:10]
        lines.append(f'{IND}<DT><H3 ADD_DATE="{add_date}">{escape(title)}</H3>')
        lines.append(f"{IND}<DL><p>")
        for child in node.get("children", []):
            walk_nodes(child, lines, indent + 1)
        lines.append(f"{IND}</DL><p>")
    elif t == "url":
        title = node.get("name", "")
        href = node.get("url", "")
        add_date = str(node.get("date_added", ""))[:10]
        lines.append(f'{IND}<DT><A HREF="{escape(href)}" ADD_DATE="{add_date}">{escape(title)}</A>')


def export_chromium_bookmarks(bookmarks_json, lines):
    roots = bookmarks_json.get("roots", {})
    for key in ("bookmark_bar", "other", "synced"):
        section = roots.get(key)
        if section and "children" in section and section["children"]:
            if key != "bookmark_bar":
                lines.append(f'    <DT><H3>{escape(key.title())}</H3>')
                lines.append('    <DL><p>')
            for child in section["children"]:
                walk_nodes(child, lines, indent=2 if key != "bookmark_bar" else 1)
            if key != "bookmark_bar":
                lines.append('    </DL><p>')


def find_brave_profiles():
    local_app = os.environ.get("LOCALAPPDATA", "")
    base = os.path.join(local_app, "BraveSoftware", "Brave-Browser", "User Data")
    if not os.path.isdir(base):
        return []
    paths = []
    for name in os.listdir(base):
        bookmarks_file = os.path.join(base, name, "Bookmarks")
        if os.path.isfile(bookmarks_file):
            paths.append((name, bookmarks_file))
    return paths


def export_bookmarks_to_file(out_path):
    profiles = find_brave_profiles()
    if not profiles:
        return False

    lines = [netscape_header("Brave Bookmarks Export")]

    for profile_name, path in profiles:
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            export_chromium_bookmarks(data, lines)
        except Exception:
            pass

    lines.append("</DL><p>\n")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return True

def main():
    # Hide root Tk window (we only want the Save As dialog)
    root = Tk()
    root.withdraw()

    # Date stamp like 2025-10-11
    today = datetime.now().strftime("%Y-%m-%d")
    default_name = f"Brave_Bookmarks_Export_{today}.html"

    file_path = filedialog.asksaveasfilename(
        defaultextension=".html",
        filetypes=[("HTML files", "*.html")],
        title="Save Brave Bookmarks As",
        initialfile=default_name,
    )

    if not file_path:
        return  # user cancelled

    export_bookmarks_to_file(file_path)

if __name__ == "__main__":
    main()
