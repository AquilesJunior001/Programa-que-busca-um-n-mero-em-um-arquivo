import time

def procurar(arquivo):
    nome = arquivo.split('.')[0]
    arq = open(arquivo,'r')
    conteudo = arq.read().split('\n')
    n = conteudo[0]
    t = int(conteudo[1])
    exis = False
    pos = -1
    i = 2
    ini = time.time()
    while i<t+2:
        if conteudo[i] == n:
            exis = True
            pos = i-1
            i = t+2
        i+=1
    fim = time.time()
    x = str((fim-ini)*1000)
    arq.close()

    nome = 'resposta-'+nome+'.txt'
    arq = open(nome,'w')
    arq.write(str(exis)+'\n')
    arq.write(str(pos)+'\n')
    arq.write(x)
    arq.close()


procurar('dataset-1-a.csv')
procurar('dataset-1-b.csv')
procurar('dataset-1-c.csv')

