import psutil

def tamanho():
    return round(psutil.virtual_memory().total/(1024*1024*1024))
def usada():
    return round(psutil.virtual_memory().used/(1024*1024*1024))
