KasparovKarpov = "1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6 8. c3 O-O 9. h3 Bb7 10. d4 Re8 11. Nbd2 Bf8 12. a4 h6 13. Bc2 ed4 14. cd4 Nb4 15. Bb1 c5 16. d5 Nd7 17. Ra3 c4 18. Nd4 Qf6 19. N2f3 Nc5 20. ab5 ab5 21. Nb5 Ra3 22. Na3 Ba6 23. Re3 Rb8 24. e5 de5 25. Ne5 Nbd3 26. Ng4 Qb6 27. Rg3 g6 28. Bh6 Qb2 29. Qf3 Nd7 30. Bf8 Kf8 31. Kh2 Rb3 32. Bd3 cd3 33. Qf4 Qa3 34. Nh6 Qe7 35. Rg6 Qe5 36. Rg8 Ke7 37. d6 Ke6 38. Re8 Kd5 39. Re5 Ne5 40. d7 Rb8 41. Nf7"
# Liste des coups d'une partie d'échec

# Extraire la liste des coups joués par Kasparov
listeK = KasparovKarpov.split(" ")
print("Kasparov")
"""
for i in range(1, len(listeK), 3):
    print(listeK[i], end=" ")
"""
Kasp = listeK[1::3]  # [à partir de:jusqu'à:step]
print(Kasp)
print("end")
#Kasparov = listeK[i] for i in 
# Extraire la liste des coups joués par Karpov
print("Karpov")
for i in range(2, len(listeK), 3):
    print(listeK[i], end=" ")
print("end")

print("Sans coups, reverse")
listeK.reverse()
for i in range(0, len(listeK)):
    if "." not in listeK[i]:
        print(listeK[i], end=" ")
print("end")
spuoc2 = ([i for i in listeK if '.' not in i])[::-1]  # [::-1] équ à [-1:0:-1]
print(spuoc2)
