try:
    # Převod desetinné čárky umožní zadat například 2,5.
    prvni = float(input("První číslo: ").replace(",", "."))
    operator = input("Operátor (+, -, *, /): ").strip()
    druhe = float(input("Druhé číslo: ").replace(",", "."))
except ValueError:
    print("Zadej platná čísla.")
else:
    if operator == "+":
        print(f"Výsledek: {prvni + druhe:g}")
    elif operator == "-":
        print(f"Výsledek: {prvni - druhe:g}")
    elif operator == "*":
        print(f"Výsledek: {prvni * druhe:g}")
    elif operator == "/":
        # Před výpočtem ověříme, že dělitel není nula.
        if druhe == 0:
            print("Nulou nelze dělit.")
        else:
            print(f"Výsledek: {prvni / druhe:g}")
    else:
        print("Neznámý operátor.")
