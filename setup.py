import os
import sys

from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info <= (2, 4):
    error = 'Requires Python Version 2.5 or above... exiting'
    print >> sys.stderr, error
    sys.exit(1)

with open("README.rst", "r") as fh:
    long_description = fh.read()

with open('requirements.txt', 'r') as f:
    requirements = f.read()

with open('test_requirements.txt', 'r') as f:
    test_requirements = f.read()

about = {}

with open(os.path.join(here, "connectwise", '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=long_description,
    author=about['__author__'],
    author_email=about['__author_email__'],
    packages=['test', 'connectwise', 'connectwise.time', 'connectwise.time.entries',
              'connectwise.company',
              'connectwise.company.contacts', 'connectwise.company.companies',
              'connectwise.company.configurations',
              'connectwise.service', 'connectwise.service.boards', 'connectwise.service.tickets',
              'connectwise.service.boardstatuses', 'connectwise.service.priorities',
              'connectwise.service.notes'],
    long_description_content_type="text/markdown",
    scripts=[],
    url=about['__url__'],
    license=about['__license__'],
    platforms="Posix; MacOS X; Windows",
    keywords='connectwise, pyRESTcw, python connectwise',
    setup_requirements=requirements,
    install_requirements=requirements,
    tests_require=test_requirements,
    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: Apache Software License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.2',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Internet',
                 ]
)
