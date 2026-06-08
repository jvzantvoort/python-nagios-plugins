import os

from .errors import *


def sys_exit(errno, msg=None):
    if msg is not None:
        print(msg)
    os.exit(errno)

def exit_ok(msg=None):
    sys_exit(ERRNO_OK, msg)

def exit_warning(msg=None):
    sys_exit(ERRNO_WARNING, msg)

def exit_critical(msg=None):
    sys_exit(ERRNO_CRITICAL, msg)

def exit_unknown(msg=None):
    sys_exit(ERRNO_UNKNOWN, msg)

def exit_dependent(msg=None):
    sys_exit(ERRNO_DEPENDENT, msg)

