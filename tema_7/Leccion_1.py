# -*- coding: utf-8 -*-
# Útiles
# Lección 1
# Módulo os

import os


def main():
    print(os.getcwd())
    print(os.sep)       # '/' para POSIX y '\\' para Windows
    print(os.curdir)    # '.' para Windows and POSIX

    os.mkdir(os.getcwd() + os.sep + "test")
    os.rename("test", "test2")
    os.rmdir("test2")

    print(os.stat("Leccion_1.py"))

if __name__ == '__main__':
    main()
