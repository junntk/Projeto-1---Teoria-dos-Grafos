from grafoLista import Grafo

nome_arquivo = "grafo.txt"



def main():
  grafo = Grafo()
  while True:
    print("\nMenu:")
    print("1. Ler arquivo")
    print("2. Adicionar vértice")
    print("3. Inserir aresta")
    print("4. Remover vértice")
    print("5. Remover aresta")
    print("6. Mostrar grafo")
    print("7. Identificador")
    print("8. Conexidade")
    print("9. Grafo reduzido")
    print("10. Encerrar")

    opcao = input("\nEscolha uma opção: ")

    try:
      if opcao == '1':
        grafo.ler_grafo(nome_arquivo)
      elif opcao == '2':
        nome_peixe = input("Digite o nome do novo vértice: ")
        grafo.adicionar_vertice(nome_arquivo, nome_peixe)
      elif opcao == '3':
        v = int(input("Digite o vértice de origem: "))
        w = int(input("Digite o vértice de destino: "))
        grafo.insereA(v, w)
      elif opcao == '4':
        v = int(input("Digite o vértice a ser removido: "))
        grafo.remover_vertice(v)
      elif opcao == '5':
        v = int(input("Digite o vértice de origem: "))
        w = int(input("Digite o vértice de destino: "))
        grafo.remover_aresta(v, w)
      elif opcao == '6':
        grafo.show()
      elif opcao == '7':
        grafo.identificador()
      elif opcao == '8':
        grafo.conectividade()
      elif opcao == '9':
        grafo_reduzido = grafo.grafo_reduzido()
        grafo_reduzido.show()
      elif opcao == '10':
        print("Encerrando o programa...")
        break
      else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
    except Exception as e:
      print(f"Ocorreu um erro: {e}")


main()
