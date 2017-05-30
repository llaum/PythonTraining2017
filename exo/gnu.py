from gnuText import gnu as texte

# Nombre de caractères
print(len(texte))
# Nombre de symboles différents
print(len(set(texte)))  # set() enlève les doublons
# Dictionaire des nombres d'occurences par symboles
dico = {}
for car in set(texte):
    dico[car] = texte.count(car)
print(dico)
# ou
dico2 = dict([car, texte.count(car)] for car in set(texte))  # [] liste
print(dico2)
# ou
dico3 = dict((car, texte.count(car)) for car in set(texte))  # () tuple
print(dico3)

# Symboles par ordre décroissant du nombre d'occurences
liste = list(dico3.items())
liste.sort(key=lambda l: l[1], reverse=True)
print(liste)
# ou
print(sorted(dico3.items(), key=lambda l: l[1], reverse=True))
