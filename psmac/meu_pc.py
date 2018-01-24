import computador
import sys
import cpu
import memoria
import power
argumentos = sys.argv
print('Aqui está algumas informacões sobre o seu computador:')
print()
print('======================================================')
print()
################# a partir daqui começa a ser passado os arguemntos para retornar info do pc do user#############
if len(argumentos) > 1:
    if argumentos[1] == '-s':
        print('Sistema operacional: ', computador.os())
        print('Versao do Sistema: ', computador.version())
    elif argumentos[1] == '-n':
        print('Nome da maquina: ', computador.name())
    elif argumentos[1] == '-p':
        if len(argumentos) == 4 and argumentos[2] == 'porcentagem' and int(argumentos[3]) >= 1:
            for x in range (int(argumentos[3])):
                consumindo = cpu.porcetagem()
                print('Consumindo: ', consumindo.user + consumindo.system, '%')
                print('Livre :', consumindo.idle, '%')
                print('==================================')
        else:
            print('Processador: ', computador.cpu())
            print('Velocidade: ', cpu.frequencia(), 'GHz')
            print('Nucleos: ', cpu.nucleos())
            print('Nucleos fisicos: ', cpu.nfisicos())
    elif argumentos[1] == '-a':
        print('Arquitetura: ', computador.maquina())
    elif argumentos[1] == '-h' or argumentos[1] == 'help':
        print('-h para ajuda', '\n-s para ver o s.o', '\n-n para ver o nome', '\n-p para ver o processador','\n-a para ver a arquitetura', '\n-m para ver memoria ram')
    elif argumentos[1] == '-m':
        if str(argumentos).find('total') > 0:
            print('Tamanho da memoria: ', memoria.tamanho(), 'Gigas')
        if str(argumentos).find('usando') > 0:
            print('Esta sendo usada: ', memoria.usada(), 'Gigas')

    elif str(argumentos).find('Desligar') > 0:
        print('Desligando o computador...')
        power.desligar()
    elif str(argumentos).find('Reiniciar') > 0:
        print('Reiniciando o computador...')
        power.reiniciar()
    else:
        print('Argumento desconhecido')
else:
    print('Você tem que passar mais de 1 argumento')
