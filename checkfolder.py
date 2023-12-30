import os
import glob

for file in glob.glob("./**/*.gz", recursive=True):
    os.remove(file)	
    print(file)