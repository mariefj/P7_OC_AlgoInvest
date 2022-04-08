import time

from utils import get_data_opti, print_results

BUDGET = 500

def optimized(data):
    budget = BUDGET * 100

    m = [[0 for x in range(budget + 1)] for x in range(len(data) + 1)]

    for i in range(1, len(data) + 1):
        for j in range(1, budget + 1):
            if data[i-1][1] <= j:
                m[i][j] = max(
                    data[i-1][2] + m[i-1][j-data[i-1][1]],
                    m[i-1][j]
                )
            else:
                m[i][j] = m[i-1][j]

    n = len(data)
    best_comb = []

    while budget >= 0 and n >= 0:
        action = data[n-1]
        if m[n][budget] == m[n-1][budget-action[1]] + action[2]:
            best_comb.append(action)
            budget -= action[1]
        n -= 1

    return  (m[-1][-1],
            sum([action[1]/100 for action in best_comb]),
            [[a[0], a[1]/100, a[2]/(a[1]/100)] for a in best_comb])

def main():
    data = get_data_opti()
    start = time.time()

    print("\nDétermination de la meilleure combinaison en cours...")
    max_benef, total_cost, best_comb = optimized(data)

    stop = time.time()
    print_results(max_benef, total_cost, best_comb, stop - start)

main()