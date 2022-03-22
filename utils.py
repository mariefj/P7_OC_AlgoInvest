import sys
import csv

def get_data():
    try:
        with open(sys.argv[1], newline='') as file:
            data_csv = csv.reader(file, delimiter=',')
            # ignore header
            next(data_csv)
        
            return [
                [action[0], float(action[1]), float(action[2])/100]
                for action in data_csv
                if float(action[1]) > 0
            ]
    except FileNotFoundError:
        print("Fichier non trouvé")

def print_combinations(combs):
    for comb in combs:
        print(comb[0], '|', round(comb[1]), '€ |', round(comb[2]*100), '%')

def print_results(benef, cost, comb, time):
    print("\n\n*********************************************************\n")
    print("Meilleure combinaison :\n")
    print_combinations(comb)
    print("\nBénéfice rapporté : ", round(benef, 2), "€")
    print("\nPour un coût total de : ", cost, "€")
    print("\nTemps du calcul : ", round(time, 2), "s")
    print("\n*********************************************************\n\n")