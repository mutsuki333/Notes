import os
import glob
import sys

import platform


path_split = '/'
if platform.system() == 'Windows':
    path_split = '\\'


IGNORE = [
    'vendor',
    "README.md",
    "init.py",
    "index.html"
]
HEADER = [
    "* [Overview]()"
]
FOOTER = [
    "",
    "<br><br>",
    "",
    "* [Back](../)"
]

def make_display_name(name):
    name = name.split(".md")[0]  # Remove .md extension
    name = name.replace('-', ' ')  # Add space instead of -
    name = name.replace('_', ' ')  # Add space instead of _
    # Capitalize all words
    # (Exclude some words from capitalization)
    forbidden = ['a', 'on', 'to', 'and', 'with', 'how', 'at', 'the']
    capitalized = ''
    for word in name.split(' '):
        if (word.lower() not in forbidden):
            capitalized += word.capitalize()
        else:
            capitalized += word.lower()
        capitalized += ' '
    name = capitalized.strip()

    return name

def accept(name):
    # if is path
    parts = name.split(path_split)
    if len(parts) > 1:
        for part in parts:
            if part in IGNORE: return False
    # if is filename or dir
    else:    
        if name in IGNORE: return False
        if name.startswith('.') or name.startswith('_'): return False
    return True

def generate_sidebar(path, entries):
    sidebar_file = open(os.path.join(path,'_sidebar.md'), 'w')
    for entry in entries:
        sidebar_file.write(entry+'\n')
    sidebar_file.close()

def scan_dir(path="."):

    for root, dirs, files in os.walk(path):
        entries = []
        if len(root.split(path_split)) == 1:
            entries += HEADER
        elif not accept(root): continue
        else:
            entries.append("* [{}]()".format(make_display_name(root.split(path_split)[-1])) )
        for d in dirs:
            if not accept(d): continue
            entries.append("* [{}](./{}/)".format(make_display_name(d), d))
        for f in files:
            if not accept(f): continue
            entries.append("* [{}]({})".format(make_display_name(f), f))
        if len(root.split(path_split)) > 1:
            entries += FOOTER
        generate_sidebar(root, entries)

if __name__ == "__main__":
    scan_dir()

print('✅ All done!')