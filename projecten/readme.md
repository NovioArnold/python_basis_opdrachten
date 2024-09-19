# De digitale stembus

*De overheid heeft de opdracht gegeven voor het inrichten van een digitale stembus.*

Dit is de documentatie van hoe ik deze stembus heb geimplementeerd.

## structuur van de app

```bash
.
├── crieer_kandidaten.py
├── kandidaten.py
├── kandidaten.txt
├── main.py
├── protocols.py
├── readme.md
├── stembus.md
├── test_kandidaten.py
└── tree.txt

1 directory, 11 files
```

### crieer_kandidaten

Hiermee maak je een "***database***" aan genaamd *kandidaten.txt*

Deze database maak je met het volgende commando

```bash
python3 crieer_kandidaten.py
```

Nu wordt automatisch de database aangemaakt

#### technische uitleg crieer_kandidatien.py

Dit is de techinsche documentatie van  hoe het script is opgebouwd

##### de inports

```python
from protocols import Kandidaat
from typing import List
```

**protocols** - Kandidaat bepaalt welk datatype in welk vak geplaatst kan worden zie protocols.py

 1. id is een interger
 2. naam is een string
 3. stem is een interger

**typing** - List geeft typhints voor beter leesbare code

##### Aanmaken_van_de_kandidaten

deze functie zorgt voor het aanmaken van kandidaten.
Hier kan je ook kandidaten toevoegen of juist verwijderen.

```python
def maak_kandidaten() -> List[Kandidaat]:
    kandidaten = []
    kandidaten.append({"id": 1, "naam": "Jan Janssen", "stemmen": 0})
    kandidaten.append({"id": 2, "naam": "Piet Pietersen", "stemmen": 0})
    kandidaten.append({"id": 3, "naam": "Klaas Klaassen", "stemmen": 0})
    kandidaten.append({"id": 4, "naam": "Henk Henksen", "stemmen": 0})
    kandidaten.append({"id": 5, "naam": "Gert Gertsen", "stemmen": 0})
    return kandidaten
```

Wat doet -> List[Kandidaat]
Dit betekend dat deze functie een lijst returned met als architectuur het **protocol Kandidaat**.
***kandidaten = [ ]*** maakt een lege lijst aan met de naam kandidaten.
***kandidaten.append()*** voegd ingegeven kandidaat toe aan lijst
***return kandidaten*** returns de lijst met kandidaten

##### kandidaten_lijst_naar_text_file

Deze functie zorgt ervoor dat de aangemaakte lijst wordt weggeschreven naar de file genaamd: ***kandidaten.txt***

```python
def kandidaten_lijst_naar_text_file(kandidaten: List[Kandidaat]) -> None:
    with open("kandidaten.txt", "w") as f:
        for k in kandidaten:
            f.write(f"{k['id']},{k['naam']},{k['stemmen']}\n")
```