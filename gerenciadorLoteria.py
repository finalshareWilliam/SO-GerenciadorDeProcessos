import threading		#biblioteca para funcionar com threads
import time				#biblioteca de funções relativas ao tempo
from random import randint

print("Este é gerador para entradas do escalonador do tipo Loteria!")

def read_file():
    result = []
    file_name = input('Digite loteria.txt:\n')
    proc = open(file_name,'r')
    proc = (proc.read()).splitlines()
    for line in proc:
        line = line.split("|")
        result.append(line)
    return (result) #retorna a matriz de str para representar o arquivo com os processos

def treatment (arquivo):
    for element in arquivo:#convert str de num a partir da lista -> int
        for it in range(1, 5):
            element[it] = eval(element[it])
    return arquivo

def lottery():
    global add
    previous = 0
    unsorted = True
    while (True):
        if(unsorted):                         # ordenação e distribuição dos tickets na lista dos processos
            total_tickets = 0
            arquivo.sort(reverse=True, key=lambda x: x[3])
            unsorted = False
            for i in range(len(arquivo)):
                arquivo[i][3] += total_tickets #O total dos bilhetes é somado aos bilhetes do processo
                total_tickets = arquivo[i][3] #total = novo máximo de bilhetes

        sort = randint(1,total_tickets) #percorre o sorteio
        for i in range(0,len(arquivo)):

            if(sort <= arquivo[i][3] ):
                sort = arquivo[i][3]
                if(i>0):
                    previous = arquivo[i-1][3]
                print("O tempo restante no " + str(arquivo[i][0]) + " é " + str(arquivo[i][2]))
                semaforo.acquire()
                arquivo[i][2] -= quantum
                semaforo.release()
                time.sleep(1)
                if (arquivo[i][2] < 1):
                    print(arquivo[i][0] + " concluido")
                    for j in range (i,len(arquivo)):
                        arquivo[j][3] += previous - sort #bilhetes  são removidos do número total dos processos

                    arquivo.pop(i)
                    total_tickets += previous - sort #total sofre decréscimo

                break
        if (add==1): #caso um processo tenha sido inserido, precisa reordenar a fila.
            unsorted = False
            add = 0
        if (len(arquivo)<= 0 and add==2):  #se o usuário decidiu sair e não houver mais processos terminar  o loop
            break

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
                process.append(int(input('prioridade:')))
                process.append(int(input('uid:')))
                process.append(int(input('memoria:')))
                arquivo.append(process)
                add = 1
                semaforo.release()

            elif (option =='2'):
                semaforo.release()
                add = 2
                break
            else:
                semaforo.release()

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

if(method == "loteria"):
    threadescalonador = threading.Thread (target=lottery,)
threads.append(threadescalonador)
threadescalonador.start()
for thread in threads:
    thread.join()