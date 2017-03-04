import os
import sys
import subprocess

if len(sys.argv) > 1:
	path = sys.argv[1]
else:
	path = os.getcwd()

picture_paths = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
        for f in files if max([f.endswith(i) for i in ('.jpeg','.jpg','.png', '.gif', '.bmp')])]

for i in picture_paths:
	subprocess.call(['python2.7',os.getcwd() + '/test2.py', i])
