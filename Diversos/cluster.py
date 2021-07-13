# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 21:28:40 2021

@author: Matheus Yokoyama
"""

from queue import PriorityQueue

Cidade= []
numero_cidade = []
with open('D:\Inteligentes\lista cidades mapa 25.txt', "r") as f:
    lines = f.readlines()



for linha in lines:
    numero = linha.split(".")[0]
    numero = int(numero) - 1
    numero_cidade.append(numero) 
    Cidade.append(linha.split(".")[1].rstrip())

cidade_json = {numero_cidade[i]: Cidade[i] for i in range(0,len(numero_cidade))}



grafo = [ [] for i in range(len(Cidade))]


# Function For Implementing Best First Search
# Gives output path having lowest cost
 
 
def best_first_search(source, target, n):
    visited = [0] * n
    #visited = True
    pq = PriorityQueue()
    lista = []
    pq.put((0, source))
    while pq.empty() == False:
        u = pq.get()[1]
        # Displaying the path having lowest cost
        lista.append(u)
        if u == target:
            break
        
        for v, c in grafo[u]:
            if visited[v] == False:
                visited[v] = True
                pq.put((c, v))
    return lista

def arestas(x, y, custo):
    x = x-1
    y = y-1
    grafo[x].append((y,custo))
    grafo[y].append((x,custo))


# aresta entre todas as cidades
arestas(23,24,16.5)
#arestas(23,24,26)
arestas(23,19,25)
arestas(24,20,19.8)
arestas(24,25,42)
arestas(19,17,25.3)
arestas(19,12,57.8)
arestas(17,13,24)
arestas(17,20,48)
arestas(20,21,21.3)
arestas(22,21,22.7)
arestas(22,18,18.7)
arestas(18,15,21.3)
arestas(18,16,27)
arestas(16,11,38)
arestas(15,16,36)
arestas(15,11,53)
arestas(15,21,43.2)
arestas(21,25,17.2)
arestas(15,10,24.5)
arestas(15,14,14.2)
arestas(14,13,13.5)
arestas(13,12,24)
arestas(13,9,32.5)
arestas(12,9,30)
arestas(8,12,17.2)
arestas(8,9,19.8)
arestas(9,10,30)
arestas(10,5,44.4)
arestas(10,11,40)
arestas(11,6,18)
arestas(11,7,22.4)
arestas(6,7,21)
arestas(4,5,18)
arestas(10,4,32)
arestas(3,8,31)
arestas(3,1,30)
arestas(1,2,24)
arestas(2,4,44.2)
arestas(3,4,28)
arestas(5,6,20)

inicio = 22
chegada = 6

res = best_first_search(inicio,chegada,len(Cidade))
#res.pop(2)
print(res)

# function to return key for any value
def get_val(key):
	for key_c, value in cidade_json.items():
		if int(key) == int(key_c):
			return value

	return "cidade doesn't exist"

# Driver Code

for cidade in res:
    print(get_val(cidade))
