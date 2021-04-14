import os

# Clear function
clf = 'clear'
if os.name == 'posix':
    clf = 'clear'
if os.name == 'nt':
    clf = 'cls'


def clear(): return os.system(clf)
