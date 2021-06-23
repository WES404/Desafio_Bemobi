import sys
import csv

arquivo = sys.argv[2] #Pega o nome do arquivo direto do prompt

with open(arquivo, "r", encoding = "utf-8") as arquivo:
    
    Brasil = {"Nome": "Brasil", "Visitantes" : 0, "Ativos" : 0}
    Chile = {"Nome": "Chile", "Visitantes" : 0, "Ativos" : 0}
    Mexico = {"Nome": "Mexico", "Visitantes" : 0, "Ativos" : 0}

    paises = [Brasil, Chile, Mexico]


    for linha in arquivo: # Intera linha por linha
        linha = linha.strip().split() # Divide a linha em uma lista

        if linha[0].startswith("55"): 

            Brasil["Visitantes"] += 1

            if linha[1] == "assinado":
                Brasil["Ativos"] += 1

        elif linha[0].startswith("56"):

            Chile["Visitantes"] += 1

            if linha[1] == "assinado":
                Chile["Ativos"] += 1

        else:

            Mexico["Visitantes"] += 1

            if linha[1] == "assinado":
                Mexico["Ativos"] += 1
    
with open("Resultado.csv", "w", newline = "") as arquivo:
    # Arquivo aberto com newline = "" para não criar linha nova a cada interação

    escrever = csv.writer(arquivo, quoting=csv.QUOTE_NONE)
    # quoting=csv.QUOTE_NONE não coloca "" nas palavras

    for linha in paises:
        escrever.writerow([linha["Nome"], linha["Visitantes"], linha["Ativos"]])