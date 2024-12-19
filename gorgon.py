from itertools import combinations

def max_money(n, suitors, gorgon_money):
    max_divorce_money = gorgon_money
    
    
    for r in range(1, n + 1):
        for combo in combinations(suitors, r):
            divorce_money = sum(combo) / 2
            total_money = gorgon_money + divorce_money
            max_divorce_money = max(max_divorce_money, total_money)
    
    return int(max_divorce_money)