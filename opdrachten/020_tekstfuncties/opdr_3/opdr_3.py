# Opdracht 3 tekstfuncties
# Naam student: Arnold Hilberink
# Groep:

# Hier komt je code...
def printboom(aantal):
    # De template boom
    template_boom = [
        "    *      ",
        "   ***     ",
        "  ******   ",
        " ********  ",
        "***********",
        "    ***    ",
        "    ***    ",
        "    ***    "
    ]
    
    # Crieer een lijst met lege strings voor het resultaat
    totaal_lijn = [""] * len(template_boom)
    
    # voor het opgegeven aantal, vermenigvuldigen van de template boom
    for i in range(aantal):
        for j in range(len(template_boom)):
            totaal_lijn[j] += template_boom[j]
    
    # print iedere regel om net totaal aantal opgegeven bomebn te printen
    for lijn in totaal_lijn:
        print(lijn)

# Print 5 bomen
printboom(5)