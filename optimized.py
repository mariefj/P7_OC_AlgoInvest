import time
from itertools import combinations

from utils import get_data, print_results

BUDGET = 500

def getKey(item):
    return item[1] * item[2]

def optimized(data):
    max_benef = 0
    total_cost = 0
    best_comb = []
    i = 0

    data = sorted(data, reverse=True, key=getKey)
    while total_cost < BUDGET and i < len(data):
        cost = data[i][1]
        if total_cost + cost <= BUDGET:
            total_cost += cost
            max_benef += data[i][1] * data[i][2]
            best_comb.append(data[i])
        i += 1

    return max_benef, total_cost, best_comb

def main():
    data = get_data()
    start = time.time()

    print("\nDétermination de la meilleure combinaison en cours...")
    max_benef, total_cost, best_comb = optimized(data)

    stop = time.time()
    print_results(max_benef, total_cost, best_comb, stop - start)

main()