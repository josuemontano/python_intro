# -*- coding: utf-8 -*-
# Útiles
# Lección 3
# Archivos: escritura

import os


directorio = os.getcwd()
archivo = open(directorio + os.sep + "Lorem_ipsum.txt", "w")

archivo.write("LOREM IPSUM")
archivo.write("\n")
archivo.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque vitae metus quis est feugiat mollis. ")
archivo.write("Aenean tincidunt justo rutrum, ornare odio at, placerat purus. Sed laoreet non libero eget malesuada.")

archivo.close()
