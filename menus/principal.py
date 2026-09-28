from menus.planetas import menu_planetas
from menus.personagens import menu_personagens
from menus.especies import menu_especies
from menus.veiculos import menu_veiculos
from menus.naves import menu_naves

def exibir_menu_principal(conjuntos):
    """
    NÍVEL 1: O Roteador Principal.
    Define o TIPO de pesquisa (Nome ou Atributo).
    """
    while True:
        print("\n" + "="*40)
        print("BANCO DE DADOS STAR WARS".center(40))
        print("="*40)
        print("[1] Pesquisar por Nome (Uso de Trie)")
        print("[2] Pesquisar por Atributo (Uso de Lista)")
        print("[3] Pesquisar por Prefixo (Uso de Trie)")
        print("[0] Sair do Sistema")
        print("="*40)
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            exibir_menu_classes(conjuntos, tipo="nome")
        elif opcao == "2":
            exibir_menu_classes(conjuntos, tipo="atributo")
        elif opcao == "3":
            exibir_menu_classes(conjuntos, tipo="prefixo")
        elif opcao == "0":
            print("\nEncerrando o sistema. Que a Força esteja com você!")
            break
        else:
            print("\n[x] Opção inválida! Tente novamente.")


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