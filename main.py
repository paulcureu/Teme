import random
import csv
import time


def calculeaza_cifra_de_control(cnp):
    key = "279146358279"
    total = sum(int(cnp[i]) * int(key[i]) for i in range(12))
    rest = total % 11
    return '1' if rest == 10 else str(rest)

def genereaza_cnp(sex, an, luna, zi, judet, numar_ordine):
    cnp_initial = f"{sex}{an:02d}{luna:02d}{zi:02d}{judet:02d}{numar_ordine:03d}"
    cifra_control = calculeaza_cifra_de_control(cnp_initial)
    return cnp_initial + cifra_control

def genereaza_nume():
    lista_prenume = ["Andrei", "Maria", "Ion", "Elena", "Alexandru", "Ana", "Cristian", "Ioana"]
    lista_nume = ["Popescu", "Ionescu", "Georgescu", "Dumitrescu", "Marinescu", "Stan", "Dobre"]
    return random.choice(lista_prenume) + " " + random.choice(lista_nume)

def generare_date_csv(nr_records=1000000, nume_fisier="cnpuri.csv"):
    with open(nume_fisier, "w", newline="") as f:
        writer = csv.writer(f)
        for _ in range(nr_records):
            sex = random.choice([1, 2])
            an = random.randint(0, 99)
            luna = random.randint(1, 12)
            zi = random.randint(1, 28)
            judet = random.randint(1, 52)
            numar_ordine = random.randint(0, 999)
            cnp = genereaza_cnp(sex, an, luna, zi, judet, numar_ordine)
            nume_complet = genereaza_nume()
            writer.writerow([cnp, nume_complet])
    print(f"Fișierul '{nume_fisier}' a fost generat cu {nr_records} înregistrări.")


class HashTable:
    def __init__(self, size=1000003):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size

    # Inserarea unui element în hash table
    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index = self.hash_function(key)
        iterations = 0
        for k, v in self.table[index]:
            iterations += 1
            if k == key:
                return v, iterations
        return None, iterations


def populare_hash_table(nume_fisier="cnpuri.csv"):
    hash_table = HashTable()
    with open(nume_fisier, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            cnp, nume = row
            hash_table.insert(cnp, nume)
    print("Hash table-ul a fost populat.")
    return hash_table


def analiza_performanta(hash_table, nume_fisier="cnpuri.csv", nr_cautari=1000):
    # Citim toate înregistrările din CSV
    with open(nume_fisier, "r") as f:
        data = list(csv.reader(f))

    if len(data) < nr_cautari:
        print("Nu există suficiente înregistrări pentru analiza performanței.")
        return

    sample_records = random.sample(data, nr_cautari)
    iteratii_list = []
    for row in sample_records:
        cnp = row[0]
        _, iterations = hash_table.search(cnp)
        iteratii_list.append(iterations)

    average_iterations = sum(iteratii_list) / nr_cautari
    print(f"Media numărului de iterații pentru căutare: {average_iterations:.2f}")



def main():
    fisier_csv = "cnpuri.csv"
    nr_records = 1000000
    print("Încep generarea datelor...")
    start = time.time()
    generare_date_csv(nr_records, fisier_csv)
    print(f"Generarea datelor a durat {time.time() - start:.2f} secunde.\n")

    print("Încep popularea hash table-ului...")
    start = time.time()
    hash_table = populare_hash_table(fisier_csv)
    print(f"Popularea hash table-ului a durat {time.time() - start:.2f} secunde.\n")

    print("Încep analiza performanței pentru 1000 de căutări...")
    analiza_performanta(hash_table, fisier_csv, 1000)


if __name__ == "__main__":
    main()
