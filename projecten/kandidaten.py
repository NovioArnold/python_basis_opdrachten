from typing import Protocol, List

##TODO: import van text bestand

#definieren van de kandidaat  (protocol)
class Kandidaat(Protocol):
    id: int
    naam: str
    stemmen: int

#aanmaken van kandidaten	
def maak_kandidaten() -> List[Kandidaat]:
    kandidaten = []
    kandidaten.append({"id": 1, "naam": "Jan Janssen", "stemmen": 0})
    kandidaten.append({"id": 2, "naam": "Piet Pietersen", "stemmen": 0})
    kandidaten.append({"id": 3, "naam": "Klaas Klaassen", "stemmen": 0})
    kandidaten.append({"id": 4, "naam": "Henk Henksen", "stemmen": 0})
    kandidaten.append({"id": 5, "naam": "Gert Gertsen", "stemmen": 0})
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
        k.id = k.id + 1
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

#main loop
def main() -> None:
    kandidaten = maak_kandidaten()
    while True:
        print("1: Breng stem uit")
        print("2: Toon kandidaten")
        print("3: Stop")
        try:
            keuze = int(input("Kies een optie: "))
            if keuze == 1:
                breng_stem_uit(kandidaten)
            elif keuze == 2:
                kandidaten = sorteer_kandidaten(kandidaten)
                for k in kandidaten:
                    print(f"{k.naam}: {k.stemmen}")
            elif keuze == 3:
                break
            else:
                raise ValueError
        except ValueError:
            print("Ongeldige invoer")