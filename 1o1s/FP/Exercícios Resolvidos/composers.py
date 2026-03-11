import sys

# --- Funções Auxiliares (substituindo o módulo dates5) ---

def parseMDY(date_str):
    """
    Converte uma string 'M/D/Y' ou apenas 'Y' num terno (Ano, Mês, Dia).
    Se tiver apenas Ano, assume 1 de Janeiro.
    """
    if "/" in date_str:
        parts = date_str.split("/")
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])
        return (year, month, day)
    else:
        # Caso seja apenas o ano (ex: "1676")
        return (int(date_str), 1, 1)

def yearsBetween(date1, date2):
    """
    Calcula a idade (diferença em anos) entre data1 e data2.
    As datas são ternos (Ano, Mês, Dia).
    """
    y1, m1, d1 = date1
    y2, m2, d2 = date2
    
    age = y2 - y1
    # Se ainda não fez anos no ano da morte, subtrai 1
    if (m2, d2) < (m1, d1):
        age -= 1
    return age

def format_date(date_tup):
    """Transforma (Y, M, D) numa string formatada YYYY-MM-DD para exibição."""
    return f"{date_tup[0]:04d}-{date_tup[1]:02d}-{date_tup[2]:02d}"

# --- Função Principal de Leitura ---

def load_lifetimes_file(file_name):
    """Load birth, death, name data from a file."""
    lst = []
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                # Ignorar linhas vazias ou comentários
                if line == "" or line.startswith("#"):
                    continue
                
                # Dividir por Tabulação
                parts = line.split('\t')
                
                # Proteção contra linhas mal formatadas
                if len(parts) < 3:
                    continue

                # ALÍNEA A: Parse das datas e criação do terno
                birth_str, death_str, name = parts[0], parts[1], parts[2]
                
                birth_date = parseMDY(birth_str)
                death_date = parseMDY(death_str)
                
                # Guarda o terno: (nascimento, morte, nome)
                lst.append((birth_date, death_date, name))
                
    except FileNotFoundError:
        print(f"Erro: O ficheiro '{file_name}' não foi encontrado.")
        sys.exit(1)
        
    return lst

# --- Função Main ---

def main():
    file_name = 'composers.txt'
    lifes = load_lifetimes_file(file_name)

    print("THE DEAD COMPOSERS SOCIETY (Século XIX)")
    print(f"{'Nome':<35} {'Idade':>5} {'Data Morte':>12}")
    print("=" * 54)

    for birth, death, name in lifes:
        # ALÍNEA C: Filtrar apenas nascidos no século XIX (1801 a 1900)
        birth_year = birth[0]
        if 1801 <= birth_year <= 1900:
            
            # Calcular idade
            age = yearsBetween(birth, death)
            
            # ALÍNEA B: Mostrar em colunas alinhadas
            # :<35 (alinhado à esquerda, ocupa 35 espaços)
            # :>5  (alinhado à direita, ocupa 5 espaços)
            death_str = format_date(death)
            print(f"{name:<35} {age:>5} {death_str:>12}")

if __name__ == "__main__":
    main()