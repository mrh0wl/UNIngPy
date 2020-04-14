UNIngPy, un API sobre articulos de uni.edu.ni
====================================
[//]: # (badges)
[![Repo](https://img.shields.io/badge/repo-github-brightgreen)](https://github.com/MrH0wl/UNIngPy)
[![Version](https://img.shields.io/badge/version-0.4.10-brightgreen.svg)](https://github.com/MrH0wl/UNIngPy/releases)
[![PyPI](https://img.shields.io/pypi/v/UNIngPy)](https://pypi.org/project/UNIngPy/#history)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pipenv.svg)
![PyPI - Status](https://img.shields.io/pypi/status/Python)
[![PyPI - License](https://img.shields.io/cran/l/meta)](LICENSE)
![Tweet - Contact](https://img.shields.io/twitter/follow/SecMare?label=Contact&style=social)

## Descripcion

UNIngPy es un package de python que extrae los articulos oficiales de http://archivodenoticias.uni.edu.ni/Articulo/
Fue desarrollado con la intencion de ayudar a la facil extraccion de informacion de la pagina de la UNI-Nicaragua.


## Requisitos

- [Python](https://www.python.org/downloads/) =< 2.7 o 3.7: 
- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/) =< 4.9.0
- [Requests](https://pypi.org/project/requests/) =< 2.23.0

## Instalacion con Pip

```sh
pip install UNIngPy
```

## Uso

```python
>>>from UNIngPy import uniarticles

>>>arts = int(input('Cuantos articulos desea ver? '))

>>>if __name__ == "__main__":
...    res = uniarticles(True).search(arts)
...
...    for entry in res:
...        print((Fore.RED + "Titulo:" + Style.RESET_ALL + "{title}".format(**entry)))
...        print((Fore.RED + "Fecha de publicacion:" + Style.RESET_ALL + "{date}".format(**e...ntry)))...
...        print((Fore.RED + "Contenido:" + Style.RESET_ALL + "{preview}".format(**entry)))
...        print((Fore.RED + "Leer completo:" +Style.RESET_ALL+" {redirect}\n".format(**entry)))
```

```
Con el ejemplo anterior podrán obtener los detalles exactos de los articulos, para usarlos individualmente o en conjunto.
```

<hr/>

El [ejemplo](tools/gen_docs.py) lo pueden encontrar en la carpeta tests, por si desean ojearlo.

## Contribución

El desarrollo del proyecto se lleva a cabo en github, https://github.com/MrH0wl/UNIngPy,
abra un problema allí para informar errores o sugerir mejoras.La colaboración es muy bienvenida, solo `bifurca(fork)` el proyecto en github y envía `pull request` al repositorio principal.

## Licencia

`UNIngPy` se publica bajo la licencia GNU General Public License v3. Mira en [LICENCIA](LICENSE) para mas detalle.

## Desarrolladores

Autor:
------

👤 **Jackson Blandon**


Lista de contribudores: https://github.com/MrH0wl/UNIngPy/graphs/contributors

## Soporte
Si crees que encontraste un bug o tienes problemas con la instalacion, abre un ticket en GitHub:
https://github.com/MrH0wl/UNIngPy/issues


<p align="center">&mdash; ❤️ &mdash;</p>
