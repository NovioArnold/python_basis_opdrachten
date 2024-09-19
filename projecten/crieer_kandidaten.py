from protocols import Kandidaat
from typing import List

#aanmaken van kandidaten	
def maak_kandidaten() -> List[Kandidaat]:
    kandidaten = []
    kandidaten.append({"id": 1, "naam": "Jan Janssen", "stemmen": 0})
    kandidaten.append({"id": 2, "naam": "Piet Pietersen", "stemmen": 0})
    kandidaten.append({"id": 3, "naam": "Klaas Klaassen", "stemmen": 0})
    kandidaten.append({"id": 4, "naam": "Henk Henksen", "stemmen": 0})
    kandidaten.append({"id": 5, "naam": "Gert Gertsen", "stemmen": 0})
    return kandidaten

#voeg lijst toe aan kandidaten.txt
def kandidaten_lijst_naar_text_file(kandidaten: List[Kandidaat]) -> None:
    with open("kandidaten.txt", "w") as f:
        for k in kandidaten:
            f.write(f"{k['id']},{k['naam']},{k['stemmen']}\n")

if __name__ == "__main__":
    kandidaten = maak_kandidaten()
    kandidaten_lijst_naar_text_file(kandidaten)
    print("Kandidaten zijn aangemaakt")
    print("Kandidaten zijn opgeslagen in kandidaten.txt")