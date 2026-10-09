from menus.classes import exibir_menu_classes
from servicos.missaoGulosa import viagem_gulosa

def exibir_menu_principal(conjuntos):
    while True:
        print("\n" + "="*40)
        print("[1] Pesquisar por Nome (Uso de Trie)")
        print("[2] Pesquisar por Atributo (Uso de Lista)")
        print("[3] Pesquisar por Prefixo (Uso de Trie)")
        print("[4] Filtros (Uso de Lista)")
        print("[5] Planejamento de Missão (Algoritmo Guloso)")
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
        elif opcao == "0":
            print("\nEncerrando o sistema. Que a Força esteja com você!")
            break
        else:
            print("\n[x] Opção inválida! Tente novamente.")

