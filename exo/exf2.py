# Fonctions: Exercice 2
# écrire une fonction mean calculant la moyenne d'une liste de nombres
def mean(listeNb):
    return sum(listeNb) / len(listeNb) if listeNb != [] else None


print(mean([]))
print(mean([1]))
print(mean([1, 2]))
print(mean([1, 2, 3]))

# écrire une fonction mean calculant la moyenne de ses arguments
def mean2(*a):					 # Packing de tous les arguments dans une liste
    return sum(a) / len(a)


print(mean2(1))
print(mean2(1, 2))
print(mean2(1, 2, 3))

def mean3(*a):
    L = [i for i in a]
    return sum(L) / len(L)


print(mean3(1))
print(mean3(1, 2))
print(mean3(1, 2, 3))
