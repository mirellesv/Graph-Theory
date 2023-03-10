class Grafo: # Trata-se de um grafo direcionado e sem arestas múltiplas
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]

    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso # caso fôssemos adicionar arestas múltiplas, poderíamos trocar
                                 # o sinal de = pelo de +=
       # self.Grafo[v-1][u-1] = 1 --> se o grafo fosse não direcionado

    def mostra_matriz(self):
        print('A matriz de adjacências vale: ')
        for i in range (self.vertices):
            print(self.grafo[i])

vertices = int(input('Digite a quantidade de vértices: '))

g = Grafo(vertices)

arestas = int(input('Digite a quantidade de arestas: '))

for i in range (arestas):
    u = int(input('Informe o vértice de partida: '))
    v = int(input('Informe o vértice de chegada: '))
    peso = int(input('Informe o peso: '))
    g.adiciona_aresta(u, v, peso)

g.mostra_matriz()