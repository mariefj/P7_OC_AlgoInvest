import time
from itertools import combinations

from utils import get_data, print_results

BUDGET = 500

def bruteforce(data):
    max_benef = 0
    total_cost = 0
    best_comb = None

    for i in range(1, len(data) + 1):
        for comb in combinations(data, i):
            benef = 0
            cost = 0
            for action in comb:
                benef += action[1] * action[2]
                cost += action[1]
            if benef > max_benef and cost <= BUDGET:
                max_benef, total_cost, best_comb = benef, cost, comb

    return max_benef, total_cost, best_comb

def main():
    data = get_data()
    start = time.time()

    print("\nDétermination de la meilleure combinaison en cours...")
    max_benef, total_cost, best_comb = bruteforce(data)

    stop = time.time()
    print_results(max_benef, total_cost, best_comb, stop - start)

main()