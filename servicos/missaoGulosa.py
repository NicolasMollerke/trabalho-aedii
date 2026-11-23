from servicos.resultados import exibir_resultados

def viagem_gulosa(lista_planetas):
    densidade = [(int(p.populacao) / int(p.diametro), p) for p in lista_planetas if p.populacao != "unknown" and p.diametro != "unknown" and p.diametro != "0"]
    
    densidade.sort(key=lambda x: x[0], reverse=True)

    print("""
    ==================================================================
            MISSÃO: OTIMIZAÇÃO DE RECRUTAMENTO REBELDE
    ==================================================================

    Você é um lider da Aliança Rebelde e precisa recrutar aliadois
    para a causa. Para isso você tem que percorrer os planetas visando
    recrutar o máximo de pessoas possíveis

    ESTRATÉGIA (ALGORITMO GULOSO):
    O sistema vai varrer a galáxia e priorizar os planetas com a
    maior DENSIDADE POPULACIONAL (Habitantes por km de diâmetro).
    O objetivo é resgatar o máximo de pessoas gastando o mínimo 
    de combustível possível.

    ------------------------------------------------------------------
    """)

    quilometragem = int(input("Defina quantos km você irá percorrer: "))
    resultados = []

    for d, p in densidade:
        diametro = int(p.diametro)

        if diametro <= quilometragem and d != 0:
            quilometragem -= diametro

            resultados.append(p)
        else:
            continue

    print("\nPlanetas Recrutados:")
    exibir_resultados(resultados)
    

    
