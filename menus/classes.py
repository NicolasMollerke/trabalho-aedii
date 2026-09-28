from menus.planetas import menu_planetas

def exibir_menu_classes(trie, tipo):
    while True:
        print("\n" + "="*30)
        print("BANCO DE DADOS STAR WARS")
        print("="*30)
        print("[1] Personages")
        print("[2] Planetas")
        print("[3] Espécies")
        print("[4] Naves")
        print("[5] Veículos")
        print("[0] Sair do Sistema")
        
        opcao = input("\nQual classe voce deseja operar: ").strip()
        
        if opcao == "1":
            if tipo == "nome":
                menu_planetas(trie, tipo)
        elif opcao == "2":
            print("\n[!] Menu de personagens em construção...")
        elif opcao == "0":
            print("\nEncerrando o sistema. Que a Força esteja com você!")
            break
        else:
            print("\n[x] Opção inválida! Tente novamente.")