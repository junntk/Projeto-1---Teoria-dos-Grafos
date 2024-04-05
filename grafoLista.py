# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 16:01:03 2023

@author: icalc
"""


# Grafo como uma lista de adjacência
class Grafo:
  TAM_MAX_DEFAULT = 200  # qtde de vértices máxima default

  # construtor da classe grafo
  def __init__(self, n=TAM_MAX_DEFAULT):
    self.n = n  # número de vértices
    self.m = 0  # número de arestas
    # lista de adjacência
    self.listaAdj = [[] for i in range(self.n)]
    self.lista_peixes = [
        "Baleia azul", "Tubarão-baleia", "Polvo", "Leão-marinho",
        "Tubarão-Limão", "Tartaruga-marinha", "Enguia", "Foca", "Baiacu",
        "Barracuda", "Camarões", "Cavalo-marinho", "Raia", "Tubarão-martelo",
        "Atum", "Estrela-do-mar", "Caranguejo-eremita", "Caranguejo",
        "Mexilhão", "Moreia", "Albatroz", "Sardinha", "Gaivota", "Lula",
        "Tubarão-cabeça-chata", "Anchova", "Vieira", "Cavalinha", "Água-viva",
        "Lagosta", "Tubarão-branco", "Ouriço-do-mar", "Baleia-cachalote",
        "Salmão", "Arenque", "Manta", "Orca", "Tubarão-mako", "Peixe-espada",
        "Krill", "Lula gigante", "Peixe-lanterna", "Medusa", "Cação",
        "Tubarão-frade", "Tubarão-zebra", "Peixe-voador", "Baleia Jubarte",
        "Tubarão-lixa", "Tubarão-raposa", "Tartaruga-de-couro",
        "Baleia-bicuda-de-cuvier", "Merluza", "Tubarão-tigre", "Polvo-gigante",
        "Baleia cinzenta", "Tubarão-serra", "Peixe-lua", "Golfinho", "Plancton"
    ]

  # Insere uma aresta no Grafo tal que
  # v é adjacente a w
  def insereA(self, v, w):
    self.listaAdj[v].append(w)
    self.m += 1

  # remove uma aresta v->w do Grafo
  def removeA(self, v, w):
    self.listaAdj[v].remove(w)
    self.m -= 1

  def ler_grafo(self, nome_arquivo):
    with open(nome_arquivo, 'r') as file:
      self.n = int(file.readline().strip())  # Atualiza o número de vértices
      self.m = int(file.readline().strip())  # Atualiza o número de arestas

      self.listaAdj = [[] for _ in range(self.n)
                       ]  # Inicializa a lista de adjacência

      for _ in range(self.m):
        line = file.readline().strip().split()
        if len(line) < 2:  # Verifica se há menos de dois valores na linha
          continue
        u, v = map(int, line)
        self.insereA(u, v)

  def escrever_grafo(self, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
      file.write(f"{self.n}\n")
      file.write(f"{self.m}\n")

      for i in range(self.n):
        for w in self.listaAdj[i]:
          file.write(f"{i} {w} \n")

    print(f"Grafo salvo em {nome_arquivo}.")

  def adicionar_vertice(self, nome_arquivo, nome_peixe):
    # Atualiza o valor de 'n' e adiciona o novo vértice
    self.lista_peixes.append(nome_peixe)
    novo_vertice = self.n
    self.n += 1

    # Atualiza o valor de 'n' no arquivo de texto
    with open(nome_arquivo, 'r+') as file:
      lines = file.readlines()
      lines[0] = f"{self.n}\n"  # Atualiza o valor de 'n'
      file.seek(0)
      file.writelines(lines)

    # Adiciona uma linha para representar o novo vértice sem arestas
    with open(nome_arquivo, 'a') as file:
      file.write(f"{novo_vertice} 0\n")

    # Adiciona uma lista vazia para o novo vértice na lista de adjacência
    self.listaAdj.append([])

    print(f"Vértice '{nome_peixe}' adicionado com sucesso.")

  def remover_aresta(self, v, w):
    if w in self.listaAdj[v]:
      self.listaAdj[v].remove(w)
      self.m -= 1
      print(f"Aresta {v}-{w} removida do grafo.")
    else:
      print(f"Aresta {v}-{w} não existe no grafo.")

  def remover_vertice(self, v):
    if v < 0 or v >= self.n:
      print(f"Vértice {v} não existe no grafo.")
      return

    # Remover todas as arestas conectadas ao vértice v
    for i in range(self.n):
      if v in self.listaAdj[i]:
        self.listaAdj[i].remove(v)
        self.m -= 1

    # Remover todas as arestas conectadas a partir do vértice v
    self.listaAdj[v] = []

    print(f"Vértice {v} e todas as suas arestas foram removidos do grafo.")

  def conectividade(self):
    visitados = [False] * self.n

    def dfs(v):
      visitados[v] = True
      for w in self.listaAdj[v]:
        if w < len(visitados) and not visitados[w]:
          dfs(w)

    for i in range(self.n):
      if not visitados[i]:
        dfs(i)

    if all(visitados):
      print("O grafo é conexo.")
    else:
      print("O grafo não é conexo.")

  def grafo_reduzido(self):
    visitados = [False] * self.n
    componente = [-1] * self.n
    num_componentes = 0

    def dfs(v, num_comp):
      visitados[v] = True
      componente[v] = num_comp
      for w in self.listaAdj[v]:
        if not visitados[w]:
          dfs(w, num_comp)

    for i in range(self.n):
      if not visitados[i]:
        dfs(i, num_componentes)
        num_componentes += 1

    # Criar o grafo reduzido
    grafo_reduzido = Grafo(num_componentes)
    for v in range(self.n):
      for w in self.listaAdj[v]:
        if componente[v] != componente[w]:
          grafo_reduzido.insereA(componente[v], componente[w])

    return grafo_reduzido

  def identificador(self):
    print("\n")
    for i in range(len(self.lista_peixes)):
      if i < len(self.listaAdj):
        print(f"\n{self.lista_peixes[i]}: ", end="")
        for w in self.listaAdj[i]:
          print(f"{self.lista_peixes[w]}, ", end="")
        print("\n")
      else:
        print(f"\nVértice {i} não tem adjacências.\n")

    print("\nFim da impressao do grafo.")

  def show(self):
    print(f"\n n: {self.n:2d} ", end="")
    print(f"m: {self.m:2d}")
    for i in range(self.n):
      print(f"\n{i:2d}: ", end="")
      if i < len(self.listaAdj) and self.listaAdj[i]:
        for w in range(len(self.listaAdj[i])):
          val = self.listaAdj[i][w]
          print(f"{val:2d} ", end="")
      else:
        print("Nenhum vértice adjacente", end="")

    print("\n\nfim da impressao do grafo.")
