import threading		#biblioteca para funcionar com threads
import time				#biblioteca de funções relativas ao tempo
from random import randint

print("Este é gerador para entradas para o escalonador do tipo Prioridades!")

def read_file():
    result = []
    file_name = input('Digite prioridades.txt:\n')
    proc = open(file_name,'r')
    proc = (proc.read()).splitlines()
    for line in proc:
        line = line.split("|")
        result.append(line)
    return (result) #retorna a matriz de str para representar o arquivo com os processos

def treatment (arquivo):
    for element in arquivo:#converte as str de números da listagem para int
        for it in range(1, 5):
            element[it] = eval(element[it])
    return arquivo


def priority():
    global add
    #print (arquivo)
    arquivo.sort(reverse=True,key = lambda x: x[3]) #listado por prioridades
    #print (arquivo)
    while True:
        if len(arquivo)>0:
            #print (arquivo)
            print("O tempo restante no " + str(arquivo[0][0]) + " é " + str(arquivo[0][2]))
            semaforo.acquire()
            arquivo[0][2] -= quantum
            semaforo.release()
            time.sleep(1)
            if (arquivo[0][2] < 1):
                print (arquivo[0][0] + " concluido")
                arquivo.pop(0)
        if (len(arquivo) <= 0 and add == 2): #se o usuário decidiu sair e não houver mais processos terminar  o loop
            break
        if (add == 1): #caso um processo tenha sido inserido, precisa reordenar a fila.
            arquivo.sort(reverse=True, key=lambda x: x[3])
            add = 0

def insert():
    global add
    global semaforo
    while (True):
        #enquanto  o readchar.readkey() for != "/":

            option = input('insira 1 para adição,2 para sair:\n\n')
            semaforo.acquire() #para a possibilidade de inserção uma thread que assumirá o topo para inserção, obtém o semáforo
            if (option == '1'):
                process = []
                process.append(input('nome:'))
                process.append(int(input('pid:')))
                process.append(int(input('tempo:')))
                process.append(int(input('prioridades:')))
                process.append(int(input('uid:')))
                process.append(int(input('memoria:')))
                arquivo.append(process)
                add = 1
                semaforo.release()

            elif (option =='2'):
                semaforo.release() #libera o semáforo na opção 2
                add = 2
                break
            else:
                semaforo.release() #libera de vez

semaforo = threading.RLock()
add = 0
threads = list()
arquivo = read_file() # extrai a info do cabeçalho e, na sequência exclui o mesmo
method = arquivo[0][0]
quantum = eval(arquivo[0][1])
arquivo.pop(0)
treatment(arquivo)
option = 0

#leitura do arquivo encerra aqui. Suas variaveis extraidas: arquivo, método, quantum
print(arquivo)
print(quantum)
print(method)

threadinput = threading.Thread(target=insert,)
threads.append(threadinput)
threadinput.start()
if (method == "prioridade"):
    threadescalonador =threading.Thread (target=priority,)

threads.append(threadescalonador)
threadescalonador.start()
for thread in threads:
    thread.join()
