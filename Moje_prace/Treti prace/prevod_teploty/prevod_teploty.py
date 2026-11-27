vstup = input("Zadej teplotu ve °C: ")

try:
    # float() očekává desetinnou tečku, proto převedeme případnou čárku.
    celsius = float(vstup.replace(",", "."))
except ValueError:
    print("Zadej teplotu jako číslo.")
else:
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{fahrenheit:.1f} °F")
