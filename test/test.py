liste = ["Hallo", "ich", "bin", "ein", "Test"]

lenListe = []
for element in liste:
    lenListe.append(len(element))

print(lenListe)
print([len(element) for element in liste])