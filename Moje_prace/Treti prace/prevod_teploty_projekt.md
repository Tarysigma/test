# Převod teploty

## Cíl
Převést teplotu ze stupňů Celsia na stupně Fahrenheita.

## Použití
Ve složce projektu spusť `python prevod_teploty.py` a zadej teplotu ve °C. Můžeš použít desetinnou čárku i tečku. Například při zadání `20` program vypíše `68.0 °F`. Pokud zadáš text, program vypíše chybovou zprávu a skončí.

## Technický popis
Skript používá vestavěné funkce Pythonu. Vstup převede na číslo pomocí `float()`, výsledek spočítá podle vzorce `°F = °C * 9 / 5 + 32` a zobrazí ho na jedno desetinné místo. Chybný vstup zachytí pomocí `except ValueError`.
