# -*- coding: utf-8 -*-
# Herramientas para computación científica
# Lección 1
# Módulo os

import os


print(os.getcwd())
print(os.sep)       # '/' para POSIX y '\\' para Windows
print(os.curdir)    # '.' para Windows and POSIX

os.rmdir("test")
os.rename("test", "test2")
os.stat("test/test.py")
