class Grafo: # Trata-se de um grafo direcionado e sem arestas múltiplas
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1 # caso fôssemos adicionar arestas múltiplas, poderíamos trocar
                                 # o sinal de = pelo de +=
       # self.Grafo[v-1][u-1] = 1 --> se o grafo fosse não direcionado

    def mostra_matriz(self):
        print('A matriz de adjacências vale: ')
        for i in range (self.vertices):
            print(self.grafo[i])

g = Grafo(4)

g.adiciona_aresta(1, 2)
g.adiciona_aresta(3, 2)
g.adiciona_aresta(2, 4)

g.mostra_matriz()