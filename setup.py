"""Our python packaging stuff."""


from os.path import abspath, dirname, join, normpath

from setuptools import setup


setup(

    # Basic package information:
    name = 'stormpath-seed',
    version = '0.0.1',
    scripts = ['stormpath-seed'],

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['docopt>=0.6.1', 'gevent>=1.0.1', 'stormpath==1.3.6'],

    # Metadata for PyPI:
    author = 'Randall Degges',
    author_email = 'r@rdegges.com',
    license = 'UNLICENSE',
    url = 'https://github.com/rdegges/stormpath-seed',
    keywords = 'user authentication auth security api stormpath utility mock seed',
    description = 'Seed your Stormpath Application with fake user data.',
    long_description = open(normpath(join(dirname(abspath(__file__)), 'README.rst'))).read(),

    # Classifiers:
    platforms = 'any',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Testing :: Traffic Generation',
        'Topic :: Utilities',
    ],

)
