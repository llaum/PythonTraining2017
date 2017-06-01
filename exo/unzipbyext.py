#!/usr/bin/env python3
# Exercice: ecrire un script executable en ligne de commande, argument : nom d'une archive zip
# Extraction des fichiers contenu dans l'archive en les répartissant en sous dossiers par extension
"""
> unzipbyext
error msg: missing zipfile to extract
> unzipbyext file1.zip file2.zip file3.zip
error msg: exactly one argument expected
> unzipbyext file1
error msg: zipfile expected
> unzipbyext corrupted.zip
error msg: zipfile may be corrupted
> unzipbyext archive.zip
archive (extracted).report: nb of files by extension
"""

from sys import argv
from os.path import exists, isdir
from os import mkdir
import zipfile


if len(argv) < 2:
    print('error: missing zipfile to extract')
    exit(1)

if len(argv) > 2:
    print('error: exactly one argument expected')
    exit(1)

FILENAME = argv[1]
if not exists(FILENAME):
    print('error:', FILENAME, 'file not found')
    exit(1)
elif isdir(FILENAME):
    print('error:', FILENAME, 'is a folder')
    exit(1)
elif not zipfile.is_zipfile(FILENAME):
    print('error:', FILENAME, 'file is not a valid zip file')
    exit(1)
else:
    with zipfile.ZipFile(FILENAME, mode='r') as myzipsource:
        if not exists(FILENAME + '.DIR'):
            mkdir(FILENAME + '.DIR')
        DICTEXTENTIONS = {}
        for zippedfile in myzipsource.infolist():
            if not zippedfile.is_dir():
                print(zippedfile.filename)
                if len(zippedfile.filename.split('.')) < 2:
                    zippedfileextention = 'no_extention'
                else:
                    zippedfileextention = zippedfile.filename.split('.')[-1]
                if not exists(FILENAME + '.DIR' + '/' + zippedfileextention):
                    mkdir(FILENAME + '.DIR' + '/' + zippedfileextention)
                with open(FILENAME + '.DIR' + '/' + zippedfileextention + '/' + zippedfile.filename.split('/')[-1], mode='wb') as extractedfile:
                    extractedfile.write(myzipsource.read(zippedfile))
                    if zippedfileextention in DICTEXTENTIONS:
                        DICTEXTENTIONS[zippedfileextention] += 1
                    else:
                        DICTEXTENTIONS[zippedfileextention] = 1
    with open(argv[0] + ".log", mode='w') as logfile:
        for extention in DICTEXTENTIONS:
            logfile.write(extention + ': ' + str(DICTEXTENTIONS[extention]) + ' files\n')
