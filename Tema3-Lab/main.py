import json
import random


def update_data_base(data):
    with open('data-base.json', 'w') as file_update:
        json.dump(data, file_update, indent=4)


def gaseste_rest(data_base, rest):
    bancnote = data_base["bancnote"]
    dp = [None] * (rest + 1)
    dp[0] = []

    bancnote_lipsa = set()

    for suma_curenta in range(rest + 1):
        if dp[suma_curenta] is not None:
            for bancnota in bancnote:
                valoare = bancnota['valoare']
                stoc_total = bancnota['stoc']

                if suma_curenta + valoare <= rest:
                    nr_folosiri = dp[suma_curenta].count(valoare)

                    if nr_folosiri < stoc_total:
                        noua_combinație = dp[suma_curenta] + [valoare]

                        if (dp[suma_curenta + valoare] is None) or (len(noua_combinație) < len(dp[suma_curenta + valoare])):
                            dp[suma_curenta + valoare] = noua_combinație
                    else:
                        bancnote_lipsa.add(valoare)

    if dp[rest] is None:
        return None, bancnote_lipsa
    else:
        for valoare_bancnota in dp[rest]:
            for bancnota in bancnote:
                if bancnota['valoare'] == valoare_bancnota:
                    bancnota['stoc'] -= 1
                    break

        update_data_base(data_base)
        return dp[rest], set()



if __name__ == '__main__':
    with open('data-base.json', 'r') as file:
        data_base = json.load(file)

    avemRest = True
    clienti = ["Ion", "Andrei", "Andreea", "Maria", "Vasile", "Marius", "Diana", "Ioana"]

    while avemRest:
        produs_ales = random.choice(data_base['produse'])
        pret = produs_ales['pret']
        suma_platita = random.randint(pret + 1, pret + 20)
        rest = suma_platita - pret

        rest_bancnote, bancnote_lipsa = gaseste_rest(data_base, rest)

        if rest_bancnote is None:
            client = random.choice(clienti)
            print(f'Imi pare rau pentru {client}, el/ea a dorit sa achiziționeze "{produs_ales["nume"]}", cost: {pret} lei. Mi-a oferit: {suma_platita} lei \nDin păcate nu am putut sa-i ofer restul de {rest} lei.\nNu am avut bancnotele de {bancnote_lipsa} lei.')
            avemRest = False
        else:
            client = random.choice(clienti)
            print(
                f'{client} a achizitionat produsul "{produs_ales["nume"]}", a costat {pret} lei. A dat {suma_platita} si a primit rest: {rest} lei.\nBancnote folosite pentru rest: {rest_bancnote}')
