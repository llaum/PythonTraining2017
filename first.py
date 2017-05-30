
from sys import version as v;print(v)


print("La configuration du poste est terminée")

w = "ceci n'est pas un mot"
print(len(w))
B = 'non, '
print(w is B)
print(B+w)
print(w[0])
print(w[-1])
print(w[7 :11])
print(w[9 :-2])
print(w[-2 :3])
print(w[ :-1])
#for i in w: print(i)
print(w.upper())

"""
w.lower()
w.isdigit()
w.isalpha()
w.strip(" ,'-?!")
w.count("e")
w.split(" ")
"""
print(w.join('adding words'))
print(type(w))
# dir liste les methodes possibles sur une variable ou un type
"""
print(dir(w))
print(dir(int))
# eval simule interpreteur python
eval("string")
# exec simule le lancement d'un script python
exec("string")
"""
