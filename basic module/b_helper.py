import inspect
import os
import shutil
import time
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
destination = "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/"
# os.rename(path + "/b.py", )
print("VERIFYING...")
time.sleep(1)
print("INSTALLING...")
time.sleep(1)
print("INSTALLATION COMPLETE")
shutil.move(path + "/b.py", destination)
shutil.move(path + "/basic.py", destination)
print("")
time.sleep(1)
print("type import b or import basic to begin")
print("then type help(b) or help(basic)")


