from menus.planetas import menu_planetas
from menus.personagens import menu_personagens
from menus.especies import menu_especies
from menus.veiculos import menu_veiculos
from menus.naves import menu_naves

def exibir_menu_classes(conjuntos, tipo):
    while True:
        print("\n" + "-"*40)
        print(f"SELECIONE A CLASSE".center(40))
        print("-" * 40)
        print("[1] Planetas")
        print("[2] Personagens")
        print("[3] Espécies")
        print("[4] Veículos")
        print("[5] Naves")
        print("[0] Voltar ao Menu Anterior")
        
        opcao = input("\nQual classe deseja consultar: ").strip()
        
        if opcao == "1":
            menu_planetas(conjuntos["planetas"]["trie"], conjuntos["planetas"]["lista"], tipo)
        elif opcao == "2":
            menu_personagens(conjuntos["personagens"]["trie"], conjuntos["personagens"]["lista"], tipo)
        elif opcao == "3":
            menu_especies(conjuntos["especies"]["trie"], conjuntos["especies"]["lista"], tipo)
        elif opcao == "4":
            menu_veiculos(conjuntos["veiculos"]["trie"], conjuntos["veiculos"]["lista"], tipo)
        elif opcao == "5":
            menu_naves(conjuntos["naves"]["trie"], conjuntos["naves"]["lista"], tipo)
        elif opcao == "0":
            break 
            
        else:
            print("\n[x] Opção inválida! Tente novamente.")