def nome(ficheiro):

    dados = {}

    try:
        with open(ficheiro, "r", encoding="utf-8") as f:
            for linha in f:
                nome_limpo = linha.strip()
                if not nome_limpo:
                    continue

                partes = nome_limpo.split()

                if len(partes) >= 1:
                    primeiro_nome = partes[0]
                    ultimo_nome = partes[-1]


                if ultimo_nome not in dados:
                    dados[ultimo_nome] = set()
                

                dados[ultimo_nome].add(primeiro_nome)


        print("{:<20} | PRIMEIROS NOMES".format("APELIDOS"))
        print("-" * 50)

        for apelido in sorted(dados.keys()):
            nomes_formatados = ", ".join(sorted(dados[apelido]))
            print("{:<20} : {}".format(apelido, nomes_formatados))

    except FileNotFoundError:
        print("Ficheiro não encontrado")

if __name__ == "__main__":
    nome("names.txt")