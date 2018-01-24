import platform
import psutil
def os():
    return platform.uname().system
def name():
    return  platform.uname().node
def version():
    return  platform.uname().version
def maquina():
    return platform.uname().machine
def cpu():
    return platform.uname().processor
def distro():
    if os() == "Linux":
        return platform.linux_distribution()
    else:
        return "Sistema invalido"