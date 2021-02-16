from setuptools import setup

setup(
    name = 'numero_por_extenso',
    version = '1.0.0',
    author = 'Daniel Chaves de Lima',
    author_email = 'danielchaves001@gmail.com',
    packages = ['numero_por_extenso'],
    description = 'Conversor para escrever número por extenso',
    long_description = 'Conversor para escrever números por extenso no formato PT-br',
    url = 'https://github.com/danielcdl/numero_por_extenso',
    project_urls = {
        'Código fonte': 'https://github.com/danielcdl/numero_por_extenso',
    },
    license = 'MIT',
    keywords = 'número por extenso',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Portuguese (Brazilian)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: User Interfaces',
    ]
)