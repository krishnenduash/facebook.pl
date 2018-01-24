import os
import computador

def desligar():
    if computador.os() == "Windows":
        os.system('shutdown -s')
    else:
        print('Sistema não identificado')

def reiniciar():
    if computador.os() == "Windows":
        os.system('shutdown -r')
    else:
        print('Sistema não identificado')