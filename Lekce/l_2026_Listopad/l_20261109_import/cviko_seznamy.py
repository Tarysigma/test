import math
# promenne a retezce
jmeno = "Petr"
vek = 25
print(f"Ahoj, jmenuji se {jmeno} a je mi {vek} let.")

numbers = [8, 5, 2, 1, 5]

numbers.append(6)
numbers.sort()
print(f"Serazeny seznam cisel: {numbers}")
print(f"prvni prvek seznamu: {numbers[0]}")
print(f"posledni prvek seznamu: {numbers[-1]}")

# slovniky a množiny

student = {}
student["vek"] = 25
student["jmeno"] = "Petr"
student["predmety"] = ["Matematika", "Fyzika", "Chemie"]

print("student:", student)

data = [3,3,3,4,5,6,7,8,9,9,9,10]
unique_data = set(data)
print(f"Unikatni hodnoty: {unique_data}")

for i in range(1, 11):
    if i % 3 == 0:
        print("delitelne tremi")
    elif i % 5 == 0:
        print("delitelne peti")
    else:
        print(i)

def vypocet_obvodu_obdelniku(dela, sirka):
    return 2 * (dela + sirka)

print(f"Obvod obdelniku s delkou S a sirkou 3 je: {vypocet_obvodu_obdelniku(5, 3)}") 

# odmocnina
odmocnina = math.sqrt(256)
odmocnina2 = math.sqrt(34654646465458896)
print(f"Odmocnina z 256 je: {odmocnina}")
print(f"Odmocnina z 34654646465458896 je: {odmocnina2}")

print(dir(math))  # vypíše všechny atributy a metody modulu math