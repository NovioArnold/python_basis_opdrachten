from kandidaten import add_stem, sorteer_kandidaten, save_kandidaten, breng_stem_uit, open_kandidaten
from protocols import Kandidaat
#main loop
def main() -> None:
    kandidaten = open_kandidaten()
    print("Welkom bij de verkiezingen! \n")
    while True:
        print("1: Breng stem uit")
        print("2: Toon kandidaten")
        print("3: Stop")
        print("")
        try:
            keuze = int(input("Kies een optie: \n"))
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

if __name__ == "__main__":
    main()