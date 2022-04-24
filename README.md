# SO-GerenciadorDeProcessos
 Sistema Operacional - Algoritmo de Escalonamento.

 Ao longo da disciplina implementaremos um pequeno sistema operacional. O primeiro passo é o módulo de gerenciamento de processos. Para isso, você deverá implementar um escalonador que realize a seleção de processos utilizando os seguintes algoritmos: alternância circular, por prioridade e loteria. O seu programa receberá como entrada um arquivo no seguinte formato:

algoritmoDeEscalonamento|fraçãoDeCPU
nomeProcesso|PID|tempoDeExecução|prioridade (ou bilhetes)|UID|qtdeMemoria

onde:

    - algoritmoDeEscalonamento é o algoritmo que será utilizado para escalonar os processos
    - fraçãoDeCPU representa o período que um processo pode ficar na CPU por vez
    - nomeProcesso contém o nome do processo (i.e., firefox.exe)
    - PID é o identificador único do processo
    - tempoDeExecução informa a quantidade de tempo que um processo necessita para executar
    - prioridade (ou bilhtes) contém a prioridade do processo (ou número de bilhetes para o algoritmo da loteria)
    - UID ID do usuário dono do processo
    - qtdeMemoria informa a quantidade de memória que o processo precisa para executar (uso futuro)

*o arquivo contém informações sobre múltiplos processos, um em cada linha

O seu programa deverá mostrar qual processo está na CPU naquele momento e quanto tempo falta para ele terminar. Nesta etapa do trabalho um processo somente sairá da CPU quando terminar a sua fatia de tempo. No futuro os processos poderão sair da CPU devido à alguma operação de E/S solicitada por eles.

Além dos processos informados através do arquivo de entrada, o usuário do sistema operacional poderá solicitar a criação de novos processos durante a execução dos demais processos. Para isso, ele deverá informar os mesmos parâmetros contidos no arquivo de entrada. No futuro, essa interface pode ser alterada para deixar a criação de processos de forma mais parecida com um sistema operacional de verdade (i.e., informando apenas o nome do processo a ser criado).
