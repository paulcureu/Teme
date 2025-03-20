import csv
import random
from datetime import datetime

judete = {
    "01": "Alba", "02": "Arad", "03": "Argeș", "04": "Bacău", "05": "Bihor",
    "06": "Bistrița-Năsăud", "07": "Botoșani", "08": "Brăila", "09": "Brașov", "10": "Buzău",
    "11": "Caraș-Severin", "12": "Cluj", "13": "Constanța", "14": "Covasna", "15": "Dâmbovița",
    "16": "Dolj", "17": "Galați", "18": "Gorj", "19": "Harghita", "20": "Hunedoara",
    "21": "Ialomița", "22": "Iași", "23": "Ilfov", "24": "Maramureș", "25": "Mehedinți",
    "26": "Mureș", "27": "Neamț", "28": "Olt", "29": "Prahova", "30": "Satu Mare",
    "31": "Sălaj", "32": "Sibiu", "33": "Suceava", "34": "Teleorman", "35": "Timiș",
    "36": "Tulcea", "37": "Vaslui", "38": "Vâlcea", "39": "Vrancea", "40": "București",
    "41": "București S.1", "42": "București S.2", "43": "București S.3", "44": "București S.4",
    "45": "București S.5", "46": "București S.6", "51": "Călărași", "52": "Giurgiu"
}

prenume_masculine = ["Andrei", "Mihai", "Gabriel", "Alexandru", "Florin", "Vlad", "Cristian", "Bogdan", "Radu",
                     "Cătălin"]
prenume_feminine = ["Ana", "Maria", "Elena", "Ioana", "Andreea", "Cristina", "Mihaela", "Alina", "Diana", "Gabriela"]
nume_familie = ["Popescu", "Ionescu", "Dumitrescu", "Georgescu", "Marinescu", "Radu", "Tudor", "Stan", "Dobre",
                "Vasile"]

def genereaza_cnp():
    sex_si_secol = random.choice([1, 2, 5, 6])
    an = random.randint(30, 99) if sex_si_secol in [1, 2] else random.randint(0, 29)
    luna = random.randint(1, 12)
    zi = random.randint(1, 28)
    judet = random.choice(list(judete.keys()))
    nnn = random.randint(100, 999)

    cnp_fara_cif_control = f"{sex_si_secol}{an:02d}{luna:02d}{zi:02d}{judet}{nnn}"

    # Calculăm cifra de control
    multipli = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    suma = sum(int(cnp_fara_cif_control[i]) * multipli[i] for i in range(12))
    cifra_control = suma % 11
    if cifra_control == 10:
        cifra_control = 1  # Regula specială pentru cifra 10

    return cnp_fara_cif_control + str(cifra_control)


# 🔹 Generare 1.000.000  CNP-uri + save CSV
numar_cnp = 1_000_000
nume_fisier = "cnp_nume.csv"

with open(nume_fisier, mode="w", newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["CNP", "Nume complet"])
    for _ in range(numar_cnp):
        cnp = genereaza_cnp()
        if cnp[0] in ["1", "5"]:
            nume_complet = f"{random.choice(prenume_masculine)} {random.choice(nume_familie)}"
        else:
            nume_complet = f"{random.choice(prenume_feminine)} {random.choice(nume_familie)}"
        writer.writerow([cnp, nume_complet])

print(f"✅ Fișierul '{nume_fisier}' a fost generat cu succes!")
