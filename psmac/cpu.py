import psutil

def frequencia():
    return round(psutil.cpu_freq().max/1000,1)
def nucleos():
    return  psutil.cpu_count()
def nfisicos():
    return psutil.cpu_count(logical=False)
def porcetagem():
    return  psutil.cpu_times_percent(interval=1)