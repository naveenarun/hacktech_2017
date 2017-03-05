import os
import sys

if len(sys.argv) > 1:
	path = sys.argv[1]
else:
	path = os.getcwd()

picture_paths = [os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
        for f in files if max([f.endswith(i) for i in ('.jpeg','.jpg','.png', '.gif', '.bmp')])]

for i in picture_paths:
	os.system('python ' + os.getcwd() + '/test.py ' + '\'' + i + '\'')

