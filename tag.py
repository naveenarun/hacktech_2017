import os
import glob

for filename in glob.iglob('/Users/ying2ra/**/*.jpg', recursive=True):
    print(filename)
print ("indise")


