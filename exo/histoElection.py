
# nbVoix = "besancenot 1498581 buffet 707268 schivardi 123540 bayrou 6820119 bové 483008 voynet 576666 villiers 818407 royal 9500112 dominique de villepin  0 nihous 420645 le pen 3834530 laguiller 487857 sarkozy 11448663"
nbVoix = "besancenot 1498581 buffet 707268 schivardi 123540 bayrou 6820119 bové 483008 voynet 576666 villiers 818407  royal 9500112 nihous 420645 lepen 3834530 laguiller 487857 sarkozy 11448663"

L = nbVoix.split()
dico = {}

candidats = L[::2]
print(candidats)
voix = L[1::2]
print(voix)
for i in range(len(candidats)):
    dico[candidats[i]]=voix[i]

# ou
dico2 = dict((L[2 * i], int(L[2 * i + 1])) for i in range(len(L) // 2))

"""
name = ""
voix = 0
for e in L:
    if not e.isdigit:
        name += e
    else:
    	voix = e
    	dico[name]=voix
    	name = ""
        voix = 0
"""

print(dico2)
