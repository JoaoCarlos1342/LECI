def allMatches(teams):
    matches = []
    for team1 in teams:
        for team2 in teams:
            if team1 != team2:
                matches.append((team1, team2))
    return matches

def main():
    print(allMatches(["FCP", "SCP", "SLB"]))
    # Esperado: 6 jogos
    # [('FCP','SCP'), ('FCP','SLB'), ('SCP','FCP'), ('SCP','SLB'), ('SLB','FCP'), ('SLB','SCP')]

    print(len(allMatches(["FCP", "SCP", "SLB"])))  # 6
    print(len(allMatches(["FCP", "SCP", "SLB", "SCB"])))  # 12
    print(len(allMatches(["A", "B", "C", "D", "E"])))  # 20


if __name__ == "__main__":
    main()