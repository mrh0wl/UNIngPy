try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

NAME = 'UNIngPy'

setup(
    name="UNIngPy", # Replace with your own username
    version="0.3.21",
    author="MrH0wl",
    author_email="secmare@protonmail.com",
    description="API para obtener articulos de la pagina oficial de la UNI Nicaragua",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MrH0wl/UNIngPy",
    keywords=['UNI Nicaragua', 'uni.edu.ni', 'UNI API', 'UNI-RUACS', 'Uni ruacs', 'Articulos UNI'],
    packages=[NAME],
    cclassifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Education',
    ],
)