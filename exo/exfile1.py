# Exercice 1: duplication de fichier
# écrire une fonction de duplication de fichier


def duplique_fichier(fileSource, fileDest):
    """ duplicate fileSource to fileDest """
    with open(fileSource, mode='r') as fileSourceRead:
        with open(fileDest, mode='w') as fileDestWrite:
            fileDestWrite.write(fileSourceRead.read())


duplique_fichier("monFichierSource.txt", "monFichierDest.txt")
duplique_fichier("monFichierSource.txt", "monFichierDest2.txt")


# Exercice 2: chiffrement de César
# cryptage d'un simple fichier par décalage constant dans l'alphabet


def chiffrement_de_cesar(fileSource, fileDest, intDecallage=1):
    """ encode <fileSource> to <fileDest> by adding [intDecallage] to source
    intDecallage default value is 1 """
    with open(fileSource, mode='r', encoding='utf8') as fileSourceRead:
        with open(fileDest, mode='w', encoding='utf8') as fileDestWrite:  #
            for line in fileSourceRead.readlines():
                for caracter in line:
                    fileDestWrite.write(chr((ord(caracter) + intDecallage) % 0x110000))  # ajouter modulo nb car utf8 pour ne pas dépasser l'espace


offset = 4

chiffrement_de_cesar("gnuText.py", "monFichierDestCrypt1.txt", offset)
chiffrement_de_cesar("monFichierDestCrypt1.txt", "monFichierDestCrypt-1.txt",
                     -offset)
chiffrement_de_cesar("monFichierSource.txt", "monFichierDestCrypt2.txt", 2)
