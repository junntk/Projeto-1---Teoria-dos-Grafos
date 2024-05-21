class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
        self.fish_list = [
            "Baleia Azul", "Tubarão-baleia", "Polvo", "Leão-marinho",
            "Tubarão-Limão", "Tartaruga-marinha", "Enguia", "Foca", "Baiacu",
            "Barracuda", "Camarões", "Cavalo-marinho", "Raia",
            "Tubarão-martelo", "Atum", "Estrela-do-mar", "Caranguejo-eremita",
            "Caranguejo", "Mexilhão", "Moreia", "Albatroz", "Sardinha",
            "Gaivota", "Lula", "Tubarão-cabeça-chata", "Anchova", "Vieira",
            "Cavalinha", "Água-viva", "Lagosta", "Tubarão-branco",
            "Ouriço-do-mar", "Baleia-cachalote", "Salmão", "Arenque", "Manta",
            "Orca", "Tubarão-mako", "Peixe-espada", "Krill", "Lula gigante",
            "Peixe-lanterna", "Medusa", "Cação", "Tubarão-frade",
            "Tubarão-zebra", "Peixe-voador", "Baleia Jubarte", "Tubarão-lixa",
            "Tubarão-raposa", "Tartaruga-de-couro", "Baleia-bicuda-de-cuvier",
            "Merluza", "Tubarão-tigre", "Polvo-gigante", "Baleia cinzenta",
            "Tubarão-serra", "Peixe-lua", "Golfinho", "Plancton"
        ]

    def degree(self, v):
        if v < 0 or v >= self.V:
            print("Vértice inválido.")
            return None
        return len(self.graph[v])

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def add_vertex(self, vertex):
        self.V += 1
        self.graph.append([])
        print("Vértice adicionado com sucesso.")

    def remove_vertex(self, vertex):
        if vertex < 0 or vertex >= self.V:
            print("Vértice inválido.")
            return

        # Remove todas as arestas conectadas ao vértice
        for v in range(self.V):
            if vertex in self.graph[v]:
                self.graph[v].remove(vertex)

        # Remove o vértice do grafo
        self.graph.pop(vertex)
        self.V -= 1

        print(f"Vértice {vertex} removido com sucesso.")

    def remove_edge(self, u, v):
        if u < 0 or u >= self.V or v < 0 or v >= self.V:
            print("Vértices inválidos.")
            return

        if v in self.graph[u]:
            self.graph[u].remove(v)
            self.graph[v].remove(u)
            print(f"Aresta entre {u} e {v} removida com sucesso.")
        else:
            print(f"Não há aresta entre {u} e {v}.")

    def print_graph_with_indices(self):
        for vertex in range(self.V):
            adjacent_vertices = self.graph[vertex]
            print(f"Vertex {vertex}: {', '.join(map(str, adjacent_vertices))}")

    def print_graph_with_fish_names(self):
        for vertex in range(self.V):
            fish_name = self.fish_list[vertex]
            adjacent_vertices = self.graph[vertex]
            print(
                f"{fish_name}: {', '.join(map(lambda v: self.fish_list[v], adjacent_vertices))}\n"
            )

    def greedy_coloring(self):
        result = [-1] * self.V
        result[0] = 0
        available = [False] * self.V
        for u in range(1, self.V):
            for v in self.graph[u]:
                if result[v] != -1:
                    available[result[v]] = True
            for color in range(self.V):
                if not available[color]:
                    break
            result[u] = color
            for v in self.graph[u]:
                if result[v] != -1:
                    available[result[v]] = False

        # Organize os peixes por cor
        fish_colors = {}
        for i in range(self.V):
            color = result[i]
            fish = self.fish_list[i]
            if color not in fish_colors:
                fish_colors[color] = [fish]
            else:
                fish_colors[color].append(fish)

        # Imprima os grupos de peixes por cor
        for color, fishes in fish_colors.items():
            print(f"Cor {color}: {', '.join(fishes)}\n")


def read_graph_from_file():
    filename = 'grafo.txt'
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Extrai o número de vértices do primeiro linha
    num_vertices = int(lines[0])

    # Cria um objeto Graph
    graph = Graph(num_vertices)

    # Adiciona as arestas do arquivo ao objeto Graph
    for line in lines[2:]:
        parts = line.split(':')
        vertex = int(parts[0])
        edges = parts[1].strip().split(',')
        # Verifica se há pelo menos uma aresta presente
        if edges[0] != '':
            for edge in edges:
                graph.add_edge(vertex, int(edge))

    return graph


def vertex_degree(graph, v):
    if v < 0 or v >= graph.V:
        print("Vértice inválido.")
        return None
    return len(graph.graph[v])


def is_eulerian(graph):
    odd_count = 0
    for vertex in range(graph.V):
        if len(graph.graph[vertex]) % 2 != 0:
            odd_count += 1
    return odd_count == 0 or odd_count == 2


def has_hamiltonian_cycle(graph):
    return all(graph.degree(v) >= graph.V / 2 for v in range(graph.V))


def print_menu():

    print("-" * 60)
    print("\nCADEIA ALIMENTAR MARINHA: MODELAGEM COM GRAFOS\n")
    print("-" * 60)
    print("\n1. Ler arquivo")
    print("2. Adicionar vértice")
    print("3. Inserir aresta")
    print("4. Remover vértice")
    print("5. Remover aresta")
    print("6. Mostrar grafo com números de vértices")
    print("7. Mostrar grafo com nomes de peixes")
    print("8. Colorir vértices")
    print("9. Grau do vértice")
    print("10. é euleriano")
    print("11. admite ciclo hamiltoniano")
    print("12. Encerrar")


def main():
    graph = None
    while True:
        print_menu()
        choice = input("Escolha uma opção: ")

        if choice == "1":
            graph = read_graph_from_file()
            print("\nGrafo lido do arquivo com sucesso.\n")
        elif choice == "2":
            if graph is None:
                print("Crie um grafo primeiro (Opção 1).")
            else:
                vertex = input("Digite o nome do vértice: ")
                graph.add_vertex(vertex)
                print("\nVértice adicionado com sucesso.\n")
        elif choice == "3":
            if graph is None:
                print("Crie um grafo primeiro (Opção 1).")
            else:
                u = int(input("Digite o índice do primeiro vértice: "))
                v = int(input("Digite o índice do segundo vértice: "))
                graph.add_edge(u, v)
                print("\nAresta inserida com sucesso.\n")
        elif choice == "4":
            if graph is None:
                print("Crie um grafo primeiro (Opção 1).")
            else:
                vertex = int(
                    input("Digite o índice do vértice a ser removido: "))
                graph.remove_vertex(vertex)
        elif choice == "5":
            if graph is None:
                print("Crie um grafo primeiro (Opção 1).")
            else:
                u = int(input("Digite o índice do primeiro vértice: "))
                v = int(input("Digite o índice do segundo vértice: "))
                graph.remove_edge(u, v)
        elif choice == "6":
            if graph is None:
                print("Crie um grafo primeiro (Opção 1).\n")
            else:
                graph.print_graph_with_indices()
        elif choice == "7":
            if graph is None:
                print("Crie um grafo primeiro (Opção 1).\n")
            else:
                graph.print_graph_with_fish_names()
        elif choice == "8":
            if graph is None:
                print("Crie um grafo primeiro (Opção 1).\n")
            else:
                graph.greedy_coloring()
        elif choice == "9":
            if graph is None:
                print("\nGrafo não carregado.\n")
            else:
                v = int(input("Digite o vértice para calcular seu grau: "))
                degree = vertex_degree(graph, v)
                if degree is not None:
                    print(f"\nGrau do vértice {v}: {degree}\n")
        elif choice == "10":
            if graph is None:
                print("\nGrafo não carregado.\n")
            else:
                if is_eulerian(graph):
                    print("\nO grafo é euleriano.\n")
                else:
                    print("\nO grafo não é euleriano\n.")
        elif choice == "11":
            if graph is None:
                print("\nGrafo não carregado\n.")
            else:
                if has_hamiltonian_cycle(graph):
                    print("\nO grafo admite um ciclo hamiltoniano.\n")
                else:
                    print("\nO grafo não admite um ciclo hamiltoniano.\n")
        elif choice == "12":
            print("\nEncerrando o programa.\n")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
