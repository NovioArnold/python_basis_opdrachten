from typing import List
from protocols import Kandidaat

#openen van kandidaten.txt
def open_kandidaten() -> List[Kandidaat]:
    kandidaten = []
    with open("kandidaten.txt") as f:
        for line in f:
            id, naam, stemmen = line.strip().split(",")
            kandidaten.append(Kandidaat(int(id), naam, int(stemmen)))
    return kandidaten

#stem toevoegen
def add_stem(kandidaten: List[Kandidaat], id: int) -> List[Kandidaat]:
    for k in kandidaten:
        if k.id == id:
            k.stemmen += 1
    return kandidaten

#functie om stemmen toe te voegen
def sorteer_kandidaten(kandidaten: List[Kandidaat]) -> List[Kandidaat]:
    return sorted(kandidaten, key=lambda k: k.stemmen, reverse=True)

#functie om kandidaten te sorteren op naam
def sorteer_kandidaten_op_naam(kandidaten: List[Kandidaat]) -> List[Kandidaat]:
    return sorted(kandidaten, key=lambda k: k.naam)

#functie om het schrijven van de kandidaten naar een text bestand
def save_kandidaten(kandidaten: List[Kandidaat]) -> None:
    with open("kandidaten.txt", "w") as f:
        for k in kandidaten:
            f.write(f"{k.id},{k.naam},{k.stemmen}\n")

#functie om stem uit te brengen
def breng_stem_uit(kandidaten: List[Kandidaat]) -> None:
    print("Kies een kandidaat:")
    for k in kandidaten:
        print(f"{k.id}: {k.naam}")
    try:
        id = int(input("Kies een id: "))
        if id < 1 or id > len(kandidaten):
            raise ValueError
        kandidaten = add_stem(kandidaten, id)
        save_kandidaten(kandidaten)
    except ValueError:
        print("Ongeldige invoer")
    save_kandidaten(kandidaten)

