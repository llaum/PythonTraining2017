
nbVoix = "besancenot 1498581 buffet 707268 schivardi 123540 bayrou 6820119 bové 483008 voynet 576666 villiers 818407\
 royal 9500112 dominique de villepin  0 nihous 420645 le pen 3834530 laguiller 487857 sarkozy 11448663"
# nbVoix = "besancenot 1498581 buffet 707268 schivardi 123540 bayrou 6820119 bové 483008 voynet 576666 villiers 818407  royal 9500112 nihous 420645 lepen 3834530 laguiller 487857 sarkozy 11448663"
#nbVoix = "besancenot 1498581 buffet 707268 schivardi 123540 bayrou 6820119 bové 483008 voynet 576666 villiers 818407 royal 9500112 dominique-de-villepin  0 nihous 420645 le-pen 3834530 laguiller 487857 sarkozy 11448663"

L = nbVoix.split()
# ou
# retraiter le string pour changer de séparateur afin de gérer les noms avec espaces, possible avec regex: import re

candidats = L[::2]
suffrages = L[1::2]
"""
dicoSuffrages1 = {}
for i in range(len(candidats)):
    dicoSuffrages1[candidats[i]]=int(suffrages[i])
print(dicoSuffrages1)

# ou

dicoSuffrages2 = dict((L[2 * i], int(L[2 * i + 1])) for i in range(len(L) // 2))
print(dicoSuffrages2)

# ou
dicoSuffrages3 = dict((L[i], int(L[i + 1])) for i in range(0, len(L), 2))
print(dicoSuffrages3)
"""
# ou pour gérer le noms avec espaces
dicoSuffrages = {}
name = ""
for element in L:
    if not element.isdigit():
        name += element + " "
    else:
        dicoSuffrages[name.strip()] = int(element)
        name = ""
print(dicoSuffrages)

dicoPercent = {}
for k in dicoSuffrages.keys():
    dicoPercent[k] = dicoSuffrages[k] * 100 / sum(dicoSuffrages.values())

print(dicoPercent)

for k in sorted(dicoPercent.keys()):
    lmax = len(max(dicoPercent.keys(), key=len))
    strTemp = '{:<' + str(lmax) + '} ({:>5}%) : '
    print(strTemp.format(k, round(dicoPercent[k], 2)), "*" * int(dicoPercent[k] + 1))
    #print(("%-25s (%7.4f %%): %s") % (k, dicoPercent[k], "*" * int(dicoPercent[k] + 1)))
