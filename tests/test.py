from __future__ import absolute_import

from UNIngPy.UNIngPy import uniarticles
from colorama import Fore, Back, Style

ans = int(input('Cuantos articulos desea ver? '))

res = uniarticles(True).search(ans)

for entry in res:
    print((Fore.RED + "Titulo:" + Style.RESET_ALL + "{title}".format(**entry)))
    print((Fore.RED + "Fecha de publicacion:" + Style.RESET_ALL + "{date}".format(**entry)))
    print((Fore.RED + "Contenido:" + Style.RESET_ALL + "{preview}".format(**entry)))
    print((Fore.RED + "Leer completo:" +Style.RESET_ALL+" {redirect}\n".format(**entry)))