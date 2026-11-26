from menus.classes import exibir_menu_classes
from menus.grafos import menu_grafos
from servicos.missaoGulosa import viagem_gulosa

def exibir_menu_principal(conjuntos):
    while True:
        print("\n" + "="*40)
        print("[1] Pesquisar por Nome (Uso de Trie)")
        print("[2] Pesquisar por Atributo (Uso de Hash)")
        print("[3] Pesquisar por Prefixo (Uso de Trie)")
        print("[4] Filtros (Uso de ArvoreB)")
        print("[5] Planejamento de Missão (Algoritmo Guloso)")
        print("[6] Funções de Grafos")
        print("[0] Sair do Sistema")
        print("="*40)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            exibir_menu_classes(conjuntos, tipo="nome")
        elif opcao == "2":
            exibir_menu_classes(conjuntos, tipo="atributo")
        elif opcao == "3":
            exibir_menu_classes(conjuntos, tipo="prefixo")
        elif opcao == "4":
            exibir_menu_classes(conjuntos, tipo="filtro")
        elif opcao == "5":
            viagem_gulosa(conjuntos["planetas"]["lista"])
        elif opcao == "6":
            menu_grafos(conjuntos["grafos"])
        elif opcao == "0":
            print("\nEncerrando o sistema. Que a Força esteja com você!")
            break
        else:
            print("\n[x] Opção inválida! Tente novamente.")

