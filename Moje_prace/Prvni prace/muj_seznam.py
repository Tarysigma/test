jmeno = "Sam"
Vek = 15
Oblibeny_Predmet = "Tělocvik a programování"

print(f"Čau jmenuji se {jmeno}, je mi {Vek} let a moje oblíbené předměty jsou {Oblibeny_Predmet}")
# Tento skript ukládá moje jméno, věk a oblíbené předměty do proměnných a následně je vypíše pomocí funkce print().

# Seřazeni čisel
cisla = [5, 3, 15, 11]

cisla.append(25)
cisla.sort()

print("Seřazená čísla:", cisla)
print("První číslo:", cisla[0])

# Výpočet obsahu obdélníku
def vypocet_obsahu_obdelniku(delka, sirka):
    return delka * sirka

print(f"Obsah obdélníku je: {vypocet_obsahu_obdelniku(8, 3)}")



# Tento skript ukládá moje jméno, věk a oblíbené předměty do proměnných a následně je vypisuje pomocí funkce `print()`. Dále pracuje se seznamem čísel, do kterého přidává nové číslo pomocí `append()`. Pomocí `sort()` seřadí čísla od nejmenšího po největší. Obsahuje také vlastní funkci pro výpočet obsahu obdélníku. Skript slouží k procvičení základních funkcí a příkazů v Pythonu.