def filtrar_planetas(lista_planetas):
    while True:
        print("\n=== FILTRAR PLANETAS ===")
        print("[1] Planetas Gigantes (Diâmetro > 15.000 km)")
        print("[2] Planetas Pequenos (Diâmetro < 10.000 km)")
        print("[3] Superpopulosos (População > 1.000.000.000)")
        print("[0] Voltar")
        
        opcao = input("Escolha o filtro: ")

        if opcao == "1":
            resultados = [p for p in lista_planetas if p.diametro != "unknown" and int(p.diametro) > 15000]
        elif opcao == "2":
            resultados = [p for p in lista_planetas if p.diametro != "unknown" and int(p.diametro) < 10000]
        elif opcao == "3":
            resultados = [p for p in lista_planetas if p.populacao != "unknown" and int(p.populacao) > 1000000000]
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
            continue

        return resultados

def filtrar_personagens(lista_personagens):
    while True:
        print("\n=== FILTRAR PERSONAGENS ===")
        print("[1] Personagens Altos (Altura >= 200 cm)")
        print("[2] Personagens Baixos (Altura <= 150 cm)")
        print("[3] Personagens Pesados (Massa > 100 kg)")
        print("[4] Personagens Leves (Massa < 50 kg)")
        print("[0] Voltar")
        
        opcao = input("Escolha o filtro: ")

        if opcao == "1":
            resultados = [p for p in lista_personagens if p.altura != "unknown" and int(p.altura) >= 200]
        elif opcao == "2":
            resultados = [p for p in lista_personagens if p.altura != "unknown" and int(p.altura) <= 150]
        elif opcao == "3":
            resultados = [p for p in lista_personagens if p.peso != "unknown" and int(p.peso) > 100]
        elif opcao == "4":
            resultados = [p for p in lista_personagens if p.peso != "unknown" and int(p.peso) < 50]
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
            continue

        return resultados
    
def filtrar_naves(lista_naves):
    while True:
        print("\n=== FILTRAR NAVES ===")
        print("[1] Naves Caras (Custo >= 1.000.000 créditos)")
        print("[2] Naves Rápidas (Hyperdrive <= 1.0)")
        print("[3] Super Cargueiros (Capacidade >= 50.000 kg)")
        print("[4] Naves de Transporte (Passageiros >= 100)")
        print("[0] Voltar")
        
        opcao = input("Escolha o filtro: ")

        if opcao == "1":
            resultados = [n for n in lista_naves if n.custo_em_creditos != "unknown" and int(n.custo_em_creditos.replace(',', '')) >= 1000000]
        elif opcao == "2":
            resultados = [n for n in lista_naves if n.classe_hiperdrive != "unknown" and float(n.classe_hiperdrive) <= 1.0]
        elif opcao == "3":
            resultados = [n for n in lista_naves if n.capacidade_carga != "unknown" and int(n.capacidade_carga.replace(',', '')) >= 50000]
        elif opcao == "4":
            resultados = [n for n in lista_naves if n.passageiros != "unknown" and n.passageiros != "n/a" and int(n.passageiros.replace(',', '')) >= 100]
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
            continue

        return resultados

def filtrar_veiculos(lista_veiculos):
    while True:
        print("\n=== FILTRAR VEÍCULOS ===")
        print("[1] Veículos Muito Rápidos (Velocidade >= 1.000 km/h)")
        print("[2] Veículos de Transporte (Passageiros >= 30)")
        print("[3] Veículos Caros (Custo >= 50.000 créditos)")
        print("[4] Veículos Individuais (Passageiros == 0)")
        print("[0] Voltar")
        
        opcao = input("Escolha o filtro: ")

        if opcao == "1":
            resultados = [v for v in lista_veiculos if v.velocidade_maxima != "unknown" and int(v.velocidade_maxima) >= 1000]
        elif opcao == "2":
            resultados = [v for v in lista_veiculos if v.passageiros != "unknown" and int(v.passageiros) >= 30]
        elif opcao == "3":
            resultados = [v for v in lista_veiculos if v.custo_em_creditos != "unknown" and int(v.custo_em_creditos.replace(',', '')) >= 50000]
        elif opcao == "4":
            resultados = [v for v in lista_veiculos if v.passageiros != "unknown" and int(v.passageiros) == 0]
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
            continue

        return resultados

def filtrar_especies(lista_especies):
    while True:
        print("\n=== FILTRAR ESPÉCIES ===")
        print("[1] Espécies Longevas (Expectativa de Vida >= 100 anos)")
        print("[2] Espécies de Vida Curta (Expectativa de Vida <= 50 anos)")
        print("[3] Espécies Altas (Altura Média >= 180 cm)")
        print("[4] Espécies Baixas (Altura Média <= 150 cm)")
        print("[0] Voltar")
        
        opcao = input("Escolha o filtro: ")

        if opcao == "1":
            resultados = [e for e in lista_especies if e.expectativa_vida != "unknown" and int(e.expectativa_vida) >= 100]
        elif opcao == "2":
            resultados = [e for e in lista_especies if e.expectativa_vida != "unknown" and int(e.expectativa_vida) <= 50]
        elif opcao == "3":
            resultados = [e for e in lista_especies if e.altura_media != "unknown" and int(e.altura_media) >= 180]
        elif opcao == "4":
            resultados = [e for e in lista_especies if e.altura_media != "unknown" and int(e.altura_media) <= 150]
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")
            continue

        return resultados
    