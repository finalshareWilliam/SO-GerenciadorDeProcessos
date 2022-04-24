import threading		#biblioteca para funcionar com threads
import time				#biblioteca de funções relativas ao tempo
from random import randint

print("Este é gerador para entradas do escalonador do tipo Round-Robin!")

def read_file():
    result = []
    file_name = input('Digite roundRobin.txt:\n')
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

def roundrobin():
    while True:
        if len(arquivo)>0:
            #print (arquivo)
            print(" O tempo restante no " + str(arquivo[0][0]) + " é " + str(arquivo[0][2]))
            semaforo.acquire()
            arquivo[0][2] -= quantum
            semaforo.release()
            time.sleep(1)
            if (arquivo[0][2] < 1):
                print (arquivo[0][0] + " concluido")
                arquivo.pop(0)
            else:
                arquivo.append(arquivo.pop(0)) #caso o processo ainda não tenha sido concluido, ele é realocado do inicio para o fim da fila 
        if (len(arquivo) <= 0 and add == 2): #se o usuário decidiu sair e não houver mais processos terminar  o loop
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
                semaforo.release()	#libera o semáforo na opção 2
                add = 2
                break
            else:
                semaforo.release()	#libera de vez

semaforo = threading.RLock()
add = 0
threads = list()
arquivo = read_file() # extrai a info do cabeçalho e, na sequência exclui o mesmo ele
method = arquivo[0][0]
quantum = eval(arquivo[0][1])
arquivo.pop(0)
treatment(arquivo)
option = 0

##leitura do arquivo encerra aqui. Suas variaveis extraidas: arquivo, método, quantum
print(arquivo)
print(quantum)
print(method)

threadinput = threading.Thread(target=insert,)
threads.append(threadinput)
threadinput.start()
if (method == "alternanciaCircular"):
    threadescalonador = threading.Thread (target=roundrobin(),)
threads.append(threadescalonador)
threadescalonador.start()
for thread in threads:
    thread.join()
