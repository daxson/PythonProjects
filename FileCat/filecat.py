# File Cataloge
# This script will grab all file names, types, and locations and create a csv file in the parent directory
# of the files being grabbed
#
# By: Daniel Axson
#

import re
import os

'''
rootdir is the directory that the script will begin reading from

Note: When adding in a path, excape all backslashes (\) by adding another backslash in front of it.
'''

rootdir = os.getcwd() # os.getcwd() gets the directory that the .py file is located

'''
ownerdict provides a way to translate initials into a pid for an individual
'''
ownerdict = {'DPA': 'daxson', 'MPC': 'mcarlton', 'EJM': 'emurray', 'ADG': 'agelsone', 'BSB': 'bboaz', 'JTR': 'jrussell'}

# remember to escape characters as needed, separate all patterns with | character
file_patterns = re.compile('.jpg|.JPG') # File patterns to include in search
dir_patterns_includes = re.compile('2015|2016') # Directory patterns to specifically include in search
dir_patterns_excludes = re.compile('_iPad|\[Originals\]') # Directory patterns to exclude from search

for dirs, subdirs, files in os.walk(rootdir):
    if re.search(dir_patterns_includes, dirs) and not re.search(dir_patterns_excludes, dirs):
        for file in files:
            if re.search(file_patterns, file):
                print(os.path.join(dirs, file))

