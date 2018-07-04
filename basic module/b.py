"""Basic Module 1.3.1

This module was created to add comands to simplify advanced often used code.
This module is aimed at begginers but is useful to anyone that uses these functions often.
for more specialized code look ar my other modules.

created by Carson Ott

please send input to carsonott@hotmail.com"""
def delay(seconds):
    """Delays program for specified number of seconds"""
    import time
    time.sleep(seconds)
def line(repeats):
    """prints a specified number of spaces"""
    for i in range(repeats):
        print("")
def pickleEx(filename, message):
    """ simplifies pickle export for beginners can export any object"""
    import pickle
    pickle.dump(message, open(filename, "wb"))
def export(filename, message):
    """ simplifies export can only export strings"""
    open(filename).write(message)
def open_(filename):
    """ simplifies opening file"""
    return open(filename).read()
def pickleOp(filename):
    """ simplifies opening pickle file"""
    import pickle
    return pickle.load(open(filename, "rb"))
def path():
    """ returns path of current file"""
    import sys
    import inspect
    import os
    return inspect.getfile(sys._getframe(1))
def directory():
    """ returns path of current directory"""
    import inspect
    import os
    import sys
    return os.path.dirname(os.path.abspath(inspect.getfile(sys._getframe(1))))
def move_file(startPoss, destination):
    """ moves file to specified destination"""
    import shutil
    if destination == "":
        shutil.move(startPoss, directory())
    shutil.move(startPoss, destination)
def random(min_, max_):
    """generates a random number"""
    import random
    random.randint(min_,max_)
def time():
    """returns a tuple with the current time"""
    import time
    R1 = (int(time.strftime("%I")), int(time.strftime("%M")), int(time.strftime("%S")))
    return R1
def date():
    """returns a tuple with the current date"""
    import time
    R2 = (int(time.strftime("%d")), int(time.strftime("%m")), int(time.strftime("%Y")))
    return R2
def date_time():
    """returns a string with the current date and time"""
    import time
    return time.strftime("%c")
def day_data():
    """returns a tuple with data on the current day"""
    import time
    return (time.strftime("%a"), time.strftime("%A"), int(time.strftime("%d")),int(time.strftime("%j")))
def month_data():
    """returns a tuple with data on the current month"""
    import time
    return (time.strftime("%b"), time.strftime("%B"), int(time.strftime("%m")))
