# -*- coding: utf-8 -*-
# Útiles
# Lección 4
# Archivos: escritura

import os


def main():
    archivo_path = os.getcwd() + os.sep + "Lorem_ipsum.txt"

    with open(archivo_path, "w") as archivo:
        archivo.write("LOREM IPSUM")
        archivo.write("\n\n")
        archivo.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vitae metus quis est feugiat mollis. ")
        archivo.write("Aenean tincidunt justo rutrum, ornare odio at, placerat purus. Sed laoreet non libero eget malesuada.")

    with open(archivo_path, "a") as archivo:
        archivo.write("\n")
        archivo.write("Donec lobortis neque eu vulputate malesuada.")

if __name__ == '__main__':
    main()
