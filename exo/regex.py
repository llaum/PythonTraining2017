# RegExp: extraire la liste des domaines à partir d'une liste d'adresses email

import re
""" execution, res est un objet
texte = 'texte sur lequel on applique la regexp'
res = pattern.match(texte)
res = pattern.search(texte)
res = pattern.findall(texte)
res = pattern.finditer(texte)
res = pattern.sub('new', texte)  # substitution
res = pattern.sub('new', texte, count=n)  # substitution
"""

MY_FILE = 'contacts_regex.txt'
MY_PATTERN = re.compile(r'@([a-zA-Z0-9_\-\.]+)')

with open(MY_FILE, mode='r') as my_file:
    domains_list = re.findall(MY_PATTERN, my_file.read())

print(len(domains_list))

domains_dict = {}
for domain in domains_list:
    if domain in domains_dict:
        domains_dict[domain] += 1
    else:
        domains_dict[domain] = 1

domains_percent_dict = {}
for k in domains_dict:
    domains_percent_dict[k] = domains_dict[k] * 1000 / sum(domains_dict.values())

print(domains_percent_dict)

for k in sorted(domains_percent_dict.keys()):
    lmax = len(max(domains_percent_dict.keys(), key=len))
    strTemp = '{:<' + str(lmax) + '} ({:>5}%) : '
    print(strTemp.format(k, round(domains_percent_dict[k], 2)), "*" * int(domains_percent_dict[k] + 1))
