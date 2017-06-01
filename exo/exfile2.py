# Exercice: duplication de fichiers
# écrire une fonction de duplication de fichiers
# arguments nommés et obligatoires srv et dst
# arguments nommés et optionnels (faux par defaut) overwrite et append


def duplique_fichier(src, dst, overwrite=False, append=False):
    """ duplicate fileSource to fileDest """
    if overwrite:
        strmode = 'w'
    if append:
        strmode = 'a'
    try:
        if append and overwrite:
            raise ValueError('Cannot do both append and overwrite')

        with open(src, mode='r') as filesource:
            with open(dst, mode=strmode) as filedest:
                filedest.write(filesource.read())
    except ValueError as error:
        print("Usage error: {} ".format(error))


duplique_fichier("monFichierSource.txt", "monFichierDest.txt", overwrite=True, append=True)
